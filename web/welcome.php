<html>
    <head>
        <title>And now I have it</title>
        <link rel="shortcut icon" href="images/favicon.ico" type="favicon/ico" />
        <link rel="stylesheet" type="text/css" href="styles/main.css" />
    </head>
    <body>
        <div id="page">
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

            $name = $_POST["name"];
            $email = $_POST["email"];
            $occupation = $_POST["occupation"];
            $age = $_POST["age"];
            
            echo "\t<h2>Welcome $name</h2>\n";
            echo "\t<h3>Your email address is $email</h2>\n";
            echo "\t<h3>Your occupation is $occupation</h2>\n";
            echo "\t<h3>Your age is $age</h2>\n";

            $dbconn = pg_connect("host=localhost dbname=users user=dschmidt password=kgjtRif#d9")
                    or die('Could not connect: ' . pg_last_error());

            // Performing SQL query
            //$query = 'SELECT * FROM weather';
            $query = "INSERT INTO users (name, email, occupation, age) " .
                          "VALUES ('$name', '$email', '$occupation', $age);";
            $result = pg_query($query) or die('Query failed: ' . pg_last_error());
            
            $query = 'SELECT * FROM users';
            $result = pg_query($query) or die('Query failed: ' . pg_last_error());

            // Printing results in HTML
            echo "<table>\n";
            tableRow($fields, true);
            while ($line = pg_fetch_array($result, null, PGSQL_ASSOC)) {
                tableRow($line, false);
            }
            echo "</table>\n";
            ?>
            <a id="return" href="form.html">Return to form</a>
        </div>
    </body>
</html>
