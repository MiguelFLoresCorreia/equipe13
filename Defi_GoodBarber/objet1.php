<!DOCTYPE html>
<html>
<head>
<!-- Font Awesome -->
<link href="https://use.fontawesome.com/releases/v5.8.2/css/all.css"rel="stylesheet"/>
<!-- Google Fonts -->
<link href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap" rel="stylesheet"/>
<!-- MDB -->
<link href="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/2.2.1/mdb.min.css" rel="stylesheet" />
<!-- MDB -->
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/2.2.1/mdb.min.js"></script>
<!--CSS-->
<link rel="stylesheet" href="css/styles.css">

<title>Google Pricing</title>
</head>
<body style="background-color: #1E093C;" style="text-align: center;">
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
    <div class="row">
        <div style="margin-top: 40px; text-align: center; col-md-6 col-sm-10">
            <h1>My Graphic</h1>
                <div style="width: 85%; margin-top: 40px;display: inline-block;background-color:white;">
                    <canvas id="myChart"></canvas>
                </div>
        </div>
    </div>

        <script src="https://cdn.jsdelivr.net/npm/chart.js@2.8.0"></script>
        <script src="main.js"></script>
        <script src="secondary.js"></script>
</body>
</html>