<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html>
    <head>
        <title>Database Test</title>
        <meta http-equiv="content-type" content="text/html; charset=utf-8" />
        <link rel="shortcut icon" href="images/favicon.ico" type="favicon/ico" />
        <link rel="stylesheet" type="text/css" href="styles/databaseTest.css" />
    </head>
    <body>
        <h1>Database is here!</h1>
        <?php
            function tableRow($data, $isHeader) {
                if ($isHeader == true) {
                    $headline = '<th>';
                    $headlineStop = '</th>';
                } else {
                    $headline = "<td>";
                    $headlineStop = "</td>";
                }
                echo "\t<tr>\n";
                foreach ($data as $col_value) {
                    echo "\t\t$headline$col_value$headlineStop\n";
                }   
                echo "\t</tr>\n"; 
            }

            $fields = array("City", "Low", "High", "Prec", "Date");
            // Connecting, selecting database
            $dbconn = pg_connect("host=localhost dbname=test_db user=dschmidt password=kgjtRif#d9")
                or die('Could not connect: ' . pg_last_error());

            // Performing SQL query
            $query = 'SELECT * FROM weather';
            $result = pg_query($query) or die('Query failed: ' . pg_last_error());

            // Printing results in HTML
            echo "<table>\n";
            tableRow($fields, true);
            while ($line = pg_fetch_array($result, null, PGSQL_ASSOC)) {
                tableRow($line, false);
            }
            echo "</table>\n";

            // Free resultset
            pg_free_result($result);

            // Closing connection
            pg_close($dbconn);
        ?>
    </body>
</html>
