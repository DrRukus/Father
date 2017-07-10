<?php
    define('DBHOST', 'localhost');
    define('DBUSER', 'root');
    define('DBPASS', '');
    define('TABLENAME', 'menu');
    define('MAX_TABLES', 20);

    // Connect to table "menu"
    function connectToMenu() {
        $db = mysqli_connect(DBHOST, DBUSER, DBPASS, TABLENAME)
            or die("Error conecting to MySQL server");
        return $db;
    }

    // Print singel record as HTML table row
    function printRecord($data, $isHeader) {
        if ($isHeader == true) {
            $headline = '<th>';
            $headlineStop = '</th>';
        } else {
            $headline = "<td>";
            $headlineStop = "</td>";
        }
        echo "\t\t<tr>\n";
        foreach ($data as $col_value) {
            echo "\t\t\t$headline<h2>$col_value</h2>$headlineStop\n";
        }
        echo "\t\t</tr>\n";
    }

    // Get list of all current item types in menu DB
    function getTypes() {
        $db = connectToMenu();
        $query = "SELECT DISTINCT(type) AS type FROM menu;";
        $result = mysqli_query($db, $query) or die('DISTINCT(type) query failed!');
        $types = array();
        while($row = mysqli_fetch_array($result, MYSQLI_ASSOC)) {
            array_push($types, $row[type]);
        }
        return $types;
    }

    // Print out entire menu table, grouped by item type
    function printMenu() {
        $db = connectToMenu();
        $fields = array('No', 'Name', 'Price');
        $types = getTypes();
        foreach ($types as $type) {
            $query = "SELECT num, name, price FROM menu WHERE type=\"$type\";";
            //echo $query;
            $result = mysqli_query($db, $query) or die('Query failed!');

            // Printing results in HTML
            echo "\t<h2 id=\"type\">$type</h2><br>\n";
            echo "\t<table id=\"items\">\n";
            printRecord($fields, true);
            while ($line = mysqli_fetch_array($result, MYSQLI_ASSOC)) {
                printRecord($line, false);
            }
            echo "\t</table>\n<br><br>";
        }
    }

    // Determine current max item # for type $typ4 and increment for item being added
    function getNum($db, $type) {
        $query = "SELECT num FROM menu WHERE type=\"$type\";";
        $result = mysqli_query($db, $query) or die('\"Largest ID\" query failed!');
        $numsRaw = array();
        while($value = mysqli_fetch_array($result, MYSQLI_ASSOC)) {
            $itemNum = explode(".", $value['num'])[1];
            array_push($numsRaw, (int)$itemNum);
        }
        $new_int = max($numsRaw) + 1;
        $new_num = substr($type, 0, 1) . "." . (string)$new_int;
        return $new_num;
    }

    // Add an item to menu table from HTML form
    function addItem($itemData) {
        $db = connectToMenu();
        $num = getNum($db, $itemData["type"]);
        $name = $itemData["name"];
        $type = $itemData["type"];
        $price = $itemData["price"];
        $query = "INSERT INTO menu (num, name, type, price) " .
            "VALUES ('$num', '$name', '$type', '$price');";
        mysqli_query($db, $query) or die('\"INSERT\" query failed!');
    }

    // Delete item with name $name from menu table
    function deleteItem($name) {
        $db = connectToMenu();
        $query = "DELETE FROM menu WHERE name=\"$name\";";
        mysqli_query($db, $query) or die('\"DELETE\" query failed!');
    }

    // Search for item as entered itno HTML form
    function searchItem($field, $value) {
        $db = connectToMenu();
        $fields = array('No', 'Name', 'Type', 'Price');
        $query = "SELECT * FROM menu WHERE $field=\"$value\";";
        //echo $query;
        $result = mysqli_query($db, $query) or die("Search query failed!");
        
        // Printing results in HTML
        echo "\t<table id=\"items\">\n";
        printRecord($fields, true);
        $numsRaw = array();
        while ($line = mysqli_fetch_array($result, MYSQLI_ASSOC)) {
            printRecord($line, false);
        }
        echo "\t</table>\n";
    }

    // Order class
    // Used to create order type to store table #, menu item selections,
    //  and calculate total bill.  Values are stored in table<table#> table.
    class Order {
        public $db;
        public $table;
        public $tableName;
        public $bill;
        public $selections;
        public $tax = 1.08;
        
        // Get table number and menu selections from HTML form
        // Generate table name string and connect to menu table.
        function __construct($tableNum, $selections) {
            $this->table = (int)$tableNum;
            $this->tableName = "table" . (string)$this->table;
            $this->bill = 0.0;
            $this->db = connectToMenu();
            $this->createOrderTable();
            $this->selections = explode(",", $selections);
        }
        
        // Create table for an order in DB
        // Verify that there are tables available (MAX_TABLES has not been exceeded),
        //   if not print that out
        function createOrderTable() {
            $tableIsTaken = false;
            do {
                $this->tableName = "table" . (string)$this->table;
                $query = "SHOW TABLES;";
                $result = mysqli_query($this->db, $query) or die("SHOW TABLES query failed!");
                while($row = mysqli_fetch_array($result, MYSQLI_ASSOC)) {
                    if ($row['Tables_in_menu'] == $this->tableName) {
                        $tableIsTaken = true;
                    }
                }
                if ($tableIsTaken) {
                    ++$this->table;
                }
            } while ($tableIsTaken && ($this->table <= MAX_TABLES));
            if (!$tableIsTaken) {
                $query = "CREATE TABLE $this->tableName (num VARCHAR (5), price FLOAT(5,2));";
                //echo $query;
                mysqli_query($this->db, $query) or die("CREATE TABLE query failed!");
            } else {
                echo "\t\t<h2>All tables are taken!</h2>\n";
                $this->table = 0;
            }
        }
        
        // Add $price to current value of $this->bill
        public function addToBill($price) {
            $this->bill += $price;
        }
        
        // Get price of item with number $itemNum
        public function getPrice($itemNum) {
            $db = connectToMenu();
            $query = "SELECT price FROM menu WHERE num=\"$itemNum\";";
            //echo $query;
            $result = mysqli_query($db, $query) or die("Price search query failed!");
            $price = array();
            while($row = mysqli_fetch_array($result, MYSQLI_ASSOC)) {
                array_push($price, $row['price']);
            }
            return round($price[0] * $this->tax, 2);
        }
        
        // Add up prices of all menu selections and print to HTML file
        public function calculateBill() {
            echo "\t<h1>Order for table #$this->table</h1><br>\n";
            foreach ($this->selections as $select) {
                $price = $this->getPrice($select);
                $this->addToBill($this->getPrice($select));
                echo "\t<h2>Item No: $select</h2><br>\n";
                echo "\t<h2>Price: $$price</h2><br><br>\n";
            }
            echo "\t<h2>Total: </h2><br>\n";
            echo "\t<h2>$$this->bill</h2><br>\n";
        }
        
        // Update table<table#> table with menu selections
        public function updateTable() {
            foreach($this->selections as $select) {
                $price = $this->getPrice($select);
                $query = "INSERT INTO table$this->table (num, price) " .
                    "VALUES (\"$select\", $price);";
                //echo $query;
                $result = mysqli_query($this->db, $query) or die("INSERT query failed!");
            }
        }
    }
?>