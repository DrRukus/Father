<?php
    include "scripts/menu.php";
?>
<html>
    <head>
        <title>Menu</title>
        <link rel="stylesheet", type="text/css" href="styles/main.css" />
        <link rel="stylesheet", type="text/css" href="styles/mainLink.css" />
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
                <div id="mainLink"><a id="main" href="menuCalc.html">Back</a></div>
                <?php
                    $order = new Order($_POST["num"], $_POST["orders"]);
                    if ($order->table != 0) {
                        $order->calculateBill();
                        $order->updateTable();
                    } else {
                        echo "\t\t<h2>Unable to accept reservations at this time.</h2><br>\n";
                    }
                ?>
            </div>
        </div>
    </body>
</html>