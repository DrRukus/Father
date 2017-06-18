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
            </div>
            <?php 
            $fields = array('Name', 'Email', 'Occupation', 'Age');
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

            $first = $_POST["first"];
            $last = $_POST["last"];
            $email = $_POST["email"];
            $occupation = $_POST["occupation"];
            
            echo "\t<h2>Welcome $first $last</h2>\n";
            echo "\t<h3>Your email address is $email</h2>\n";
            echo "\t<h3>Your occupation is $occupation</h2>\n";

            $dbconn = pg_connect("host=localhost dbname=users user=users password=users")
                    or die('Could not connect: ' . pg_last_error());

            // Performing SQL query
            //$query = 'SELECT * FROM weather';
            $query = "INSERT INTO user_info (first, last, email, occupation) " .
                          "VALUES ('$first', '$last', '$email', '$occupation');";
            $result = pg_query($query) or die('Query failed: ' . pg_last_error());
            
            $query = 'SELECT * FROM user_info';
            $result = pg_query($query) or die('Query failed: ' . pg_last_error());

            // Printing results in HTML
            echo "\t<table>\n";
            tableRow($fields, true);
            while ($line = pg_fetch_array($result, null, PGSQL_ASSOC)) {
                tableRow($line, false);
            }
            echo "\t</table>\n";
            ?>
            <a id="return" href="../form.html">Return to form</a>
        </div>
    </body>
</html>
