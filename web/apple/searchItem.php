<?php
    include "scripts/menu.php";
?>
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
            <div id="center">
                <?php
                    if ($_POST["num"]) {
                        searchItem("num", $_POST["num"]);
                    } else if ($_POST["name"]) {
                        searchItem("name", $_POST["name"]);
                    } else if ($_POST["type"]) {
                        searchItem("type", $_POST["type"]);
                    }
                ?>
            </div>
            <a id="main" href="menuOptions.html">Back</a>
        </div>
    </body>
</html>