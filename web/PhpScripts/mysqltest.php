<?php
   
    $dbhost = 'localhost';
    $dbuser = 'root';
    $dbpass = '';
    //$conn = mysqli_connect($dbhost, $dbuser, $dbpass);
    $db = mysqli_connect($dbhost, $dbuser, $dbpass, 'users');
         
    if (mysqli_connect_errno()) {
        echo "Error: Could not connect!";
        exit;
    }
   
    echo 'Connected successfully';
    mysqli_close($conn);
?>