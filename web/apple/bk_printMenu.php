<html>
    <head>
        <title>Menu</title>
        <link rel="stylesheet", type="text/css" href="styles/main.css" />
        <link rel="shortcut icon" href="images/favicon.ico" type="favicon/ico" />
    </head>
    <body>
        <div id="menu">
            <div id="header">
                <h1>
                    <img src="images/left.gif" alt="" />
                    Elzar's Fine Cuisine
                    <img src="images/right.gif" alt="" />
                </h1>
                <h3 id="date"></h3>
                <script type="text/javascript" src="scripts/date.js"></script>
            </div>
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
            <a id="main" href="main.html">Main page</a>
        </div>
    </body>
</html>