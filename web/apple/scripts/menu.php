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

    $db = connectToMenu();
    printTable($db);
?>