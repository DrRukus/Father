<?php
    define('DBHOST', 'localhost');
    define('DBUSER', 'root');
    define('DBPASS', '');
    define('TABLENAME', 'menu');

    function connectToMenu() {
        $db = mysqli_connect(DBHOST, DBUSER, DBPASS, TABLENAME)
            or die("Error conecting to MySQL server");
        return $db;
    }

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

    function getNum($db, $type) {
        $query = "SELECT num FROM menu WHERE type=\"$type\";";
        $result = mysqli_query($db, $query) or die('\"Largest ID\" query failed!');
        $numsRaw = array();
        while($value = mysqli_fetch_array($result, MYSQLI_ASSOC)) {
            $itemNum = explode(".", $value[num])[1];
            array_push($numsRaw, (int)$itemNum);
        }
        $new_int = max($numsRaw) + 1;
        $new_num = substr($type, 0, 1) . "." . (string)$new_int;
        return $new_num;
    }

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

    function deleteItem($name) {
        $db = connectToMenu();
        $query = "DELETE FROM menu WHERE name=\"$name\";";
        mysqli_query($db, $query) or die('\"DELETE\" query failed!');
    }

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

    class Order {
        public $db;
        public $tableNum;
        public $bill;
        public $selections;
        public $tax = 1.08;
        
        function __construct($tableNum, $selections) {
            $this->table = $tableNum;
            $this->bill = 0;
            $this->db = connectToMenu();
            $this->createOrderTable();
            $this->selections = explode(",", $selections);
        }
        
        function createOrderTable() {
            $tableName = "table" . (string)$this->table;
            $query = "CREATE TABLE $tableName (num VARCHAR (5), price FLOAT(5,2));";
            //echo $query;
            mysqli_query($this->db, $query) or die("Search query failed!");
        }
        
        public function addToBill($price) {
            $this->bill += $price;
        }
        
        public function getPrice($itemNum) {
            $db = connectToMenu();
            $query = "SELECT price FROM menu WHERE num=\"$itemNum\";";
            //echo $query;
            $result = mysqli_query($db, $query) or die("Search query failed!");
            $price = array();
            while($row = mysqli_fetch_array($result, MYSQLI_ASSOC)) {
                //print_r($row);
                array_push($price, $row[price]);
            }
            return round($price[0] * $this->tax, 2);
        }
        
        public function calculateBill() {
            echo "\t<h1>Order for table #$this->table</h1><br>\n";
            foreach ($this->selections as $select) {
                echo "\t<h2>Item No: $select</h2><br>\n";
                $price = $this->getPrice($select);
                echo "\t<h2>Price: $$price</h2><br><br>\n";
                $this->addToBill($this->getPrice($select));
            }
            echo "\t<h2>Total: </h2><br>\n";
            echo "\t<h2>$$this->bill</h2><br>\n";
        }
        
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