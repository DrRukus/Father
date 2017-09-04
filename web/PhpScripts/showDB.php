<html>
    <head>
        <title>And now I have it</title>
        <link rel="shortcut icon" href="images/favicon.ico" type="favicon/ico" />
        <link rel="stylesheet" type="text/css" href="../styles/main.css" />
        <link rel="stylesheet" type="text/css" href="../styles/welcome.css" />
    </head>
    <body>
        <div id="page">
            <div id="header">
                <h1>
                    <img src="images/left.gif" alt="" />
                    Paige O'Daniel
                    <img src="images/right.gif" alt="" />
                </h1>
                <h3 id="date"></h3>
				<script type="text/javascript" src="../scripts/script1.js"></script>
            </div>
            <?php
                $fields = array('First', 'Last', 'user ID', 'Email', 'Occupation');
                function tableRow($data, $isHeader) {
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
            
                $dbhost = 'localhost';
                $dbuser = 'root';
                $dbpass = '';
                $db = mysqli_connect($dbhost, $dbuser, $dbpass, 'users')
                    or die("Error conecting to MySQL server");
            
                $query = 'SELECT * FROM basics;';
                $result = mysqli_query($db, $query) or die('Query failed!');

                // Printing results in HTML
                echo "\t<table>\n";
                tableRow($fields, true);
                while ($line = mysqli_fetch_array($result, MYSQLI_ASSOC)) {
                    tableRow($line, false);
                }
                echo "\t</table>\n";
            ?>
            <a id="return" href="../form.html">Return to form</a>
        </div>
    </body>
</html>
