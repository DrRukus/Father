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
            echo "\t\t\t$headline$col_value$headlineStop\n";
        }
        echo "\t\t</tr>\n";
    }

    function printTable($db) {
        $fields = array('No', 'Name', 'Type', 'Price');
        $query = 'SELECT * FROM menu;';
        $result = mysqli_query($db, $query) or die('Query failed!');

        // Printing results in HTML
        echo "\t<table id=\"items\">\n";
        printRecord($fields, true);
        while ($line = mysqli_fetch_array($result, MYSQLI_ASSOC)) {
            printRecord($line, false);
        }
        echo "\t</table>\n";
    }

    function getNum($db) {
        $query = "SELECT num FROM menu;";
        $result = mysqli_query($db, $query) or die('\"Largest ID\" query failed!');
        $numsRaw = array();
        while($value = mysqli_fetch_array($result, MYSQLI_ASSOC)) {
            array_push($numsRaw, $value[num]);
        }
        $new_num = max($numsRaw) + 1;
        return $new_num;
    }

    function addItem($db, $itemData) {
        $num = getNum($db);
        $name = $itemData["name"];
        $type = $itemData["type"];
        $price = $itemData["price"];
        $query = "INSERT INTO menu (num, name, type, price) " .
            "VALUES ('$num', '$name', '$type', '$price');";
        mysqli_query($db, $query) or die('\"INSERT\" query failed!');
    }

    function deleteItem($db, $name) {
        $query = "DELETE FROM menu WHERE name=\"$name\";";
        mysqli_query($db, $query) or die('\"DELETE\" query failed!');
    }

    function searchItemByNum($db, $field, $value) {
        $query = "SELECT '$field' FROM menu;";
        echo $query;
        $result = mysqli_query($db, $query) or die("\"Num SELECT\" query failed!");
        // Printing results in HTML
        echo "\t<table id=\"items\">\n";
        printRecord($fields, true);
        while ($line = mysqli_fetch_array($result, MYSQLI_ASSOC)) {
            printRecord($line[num], false);
        }
        echo "\t</table>\n";
    }
?>