<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
<!-- Font Awesome -->
<link href="https://use.fontawesome.com/releases/v5.8.2/css/all.css"rel="stylesheet"/>
<!-- Google Fonts -->
<link href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap" rel="stylesheet"/>
<!-- MDB -->
<link href="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/2.2.1/mdb.min.css" rel="stylesheet" />
<!-- MDB -->
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/2.2.1/mdb.min.js"></script>
<!--CSS-->
<link href="styles.css" rel="stylesheet">
<link rel="stylesheet" href="css/styles.css">

<title>Google Pricing</title>
<link rel="manifest" href="manifest.json">
</head>
<body style="background-color: #1E093C;">
    <header>  
        <div class="row header">
            <div class="col-1"></div>
            <div class="col-2">
                <a href="#" class="d-flex flex-column hover-zoom">
                    <img  src="css/money-graph-with-up-arrow.svg" width="30em" >
                    Flow
                </a>
            </div>
            <div class="col-2">
                <a href="#" class="d-flex flex-column flex-grow-1  hover-zoom">
                    <img  src="css/pot.svg" width="30em">
                    Objects
                </a>
            </div>
            <div class="col-4"></div>
            <div class="col-2 ">
                <a href="index.php" class="d-flex flex-column  hover-zoom">
                    <img  src="css/search.svg" width="30em">
                    Search
                </a>
            </div>
        </div>
    </header>
    <div class="col-md-12" style="text-align:center;">
        <div class="titre" style="margin-top:40px;">
            Veuillez entrer un produit à monitorer :
        </div><br>
        <div>
            <form action="traitement.php" method="POST" class="form-group" id="choose-product-form" style="margin-bottom:40px;">
                <input type="text" placeholder="Nom du produit" class="form-control" name="productName"><br> 
                <input type="submit" value="Rechercher" class="btn btn-primary">                 
            </form>
        </div>
        <div id="products"></div>
    </div>
      
      <script src="main.js"></script>
      <?php
          if(isset($_GET["flag"])){
            ?>
            <script>
              changeFlag();
            </script>
            <?php
          }
        ?>
</body>
</html>