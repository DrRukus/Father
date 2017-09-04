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
            $fields = array('Name', 'Email', 'user ID', 'Occupation', 'Age');
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
            
            function getIds($db) {
                $query = "SELECT id FROM basics;";
                $result = mysqli_query($db, $query) or die('ID query failed!');
                $id_array = array();
                while($row = mysqli_fetch_array($result, MYSQLI_ASSOC)){
                    array_push($id_array, $row);
                }
                $ids = array();
                foreach($id_array as $miny_arr) {
                    array_push($ids, $miny_arr[id]);
                }
                return $ids;
            }
            
            function newId($db) {
                $ids = getIds($db);
                $new_id = rand(0, 1000);
                while(in_array((string)$new_id, $ids)) {
                    $new_id = rand(0, 1000);
                }
                return $new_id;
            }

            $first = $_POST["first"];
            $last = $_POST["last"];
            $email = $_POST["email"];
            $occupation = $_POST["occupation"];
            
            echo "\t<h2>Welcome $first $last</h2>\n";
            echo "\t<h3>Your email address is $email</h2>\n";
            echo "\t<h3>Your occupation is $occupation</h2>\n";

            $dbhost = 'localhost';
            $dbuser = 'root';
            $dbpass = '';
            $db = mysqli_connect($dbhost, $dbuser, $dbpass, 'users')
                or die("Error conecting to MySQL server");
            
            $new_id = newId($db);

            // Performing SQL query
            $query = "INSERT INTO basics (first, last, id, email, occupation) " .
                          "VALUES ('$first', '$last', $new_id, '$email', '$occupation');";
            $result = mysqli_query($db, $query) or die('INSERT query failed!');
            
            $query = 'SELECT * FROM basics;';
            $result = mysqli_query($db, $query) or die('Full table query failed!');

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
