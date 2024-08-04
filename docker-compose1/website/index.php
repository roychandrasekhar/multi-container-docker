<html>
    <head>
        <title>My Shop</title>
    </head>
    <body>
        <h1>welcome to my shop</h1>
        <ul>
            <?php
                $jsonData = file_get_contents('http://product-service');
                $obj = json_decode($jsonData);

                $products = $obj->product;
                foreach($products as $product) {
                    echo "<li>$product</li>";
                }
            ?>
        </ul>
    </body>
</html>