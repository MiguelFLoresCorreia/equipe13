<?php

    $name = htmlspecialchars($_POST["productName"]);
    $output = system("python test001.py .$name");
    echo $name;
    $file = fopen("test.txt","w");
    echo fwrite($file,"Hello World. Testing!");
    fclose($file);

    header('Location:http://localhost/equipe13/Defi_GoodBarber/index.php?flag=1');
?>