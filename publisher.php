<!DOCTYPE html>
<html lang="en"><head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">
    
    <link rel="icon" href="http://getbootstrap.com/favicon.ico">

    <title>BoiledWaterDB</title>

    <!-- Bootstrap core CSS -->
    <link href="Jumbotron Template for Bootstrap_files/bootstrap.min.css" rel="stylesheet">

  </head>

    
    
  <body>


    <div class="container-fluid">
      <div class="row">
        <nav class="col-sm-3 col-md-2 d-none d-sm-block bg-light sidebar">
          <ul class="nav nav-pills flex-column">
            <li class="nav-item">
              <a class="nav-link active" href="index.php">Home <span class="sr-only">(current)</span></a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="games.php">Games</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="dlc.php">DLC</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="developer.php">Developer</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="publisher.php">Publisher</a>
            </li> 
            <li class="nav-item">
              <a class="nav-link" href="history.php">History</a>
            </li>
              
            <li class="nav-item">
              <a class="nav-link" href="view1.php">View 1</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="view2.php">View 2</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="view3.php">View 3</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="view4.php">View 4</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="view5.php">View 5</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="view6.php">View 6</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="view7.php">View 7</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="view8.php">View 8</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="view9.php">View 9</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="view10.php">View 10</a>
            </li>
              
            <li class="nav-item">
              <a class="nav-link" href="Search.php">Search Games</a>
            </li>
              
          </ul>
          </nav>


 

        <main role="main" class="col-sm-9 ml-sm-auto col-md-10 pt-3">
    <center><img src=logo2.png width="50%" height="50%"></center><br>
        
    <p> Values of the Publisher Table in our Database</p>
            

    <?php 
    $conn = pg_connect("host=localhost port=5432 dbname=boiledwaterdb user=root password=root"); //Connects to boiledwaterdb
    if (!$conn) {
        echo "An error occurred.\n";
        exit;
    }
    $result = pg_query($conn, "SELECT * FROM publisher");
    if (!$result) {
        echo "An error occurred.\n";
        exit;
    }
    // check if the query succeeded
    if (!$result) {
      die('There was an error running the query[' . $db->error . ']');
    }
    // Display the results of the query for each row
    echo "<div class='table-responsive'><table id='database' class='table table-striped'> <tr> <th> Publisher ID </th> <th> Publisher Name </th> </tr>";
    $i = 0;
    //Print out query table from SQL Query
    while ($row = pg_fetch_row($result)) 
    {
        echo '<tr>';
        $count = count($row);
        $y = 0;
        while ($y < $count)
        {
            $c_row = current($row);
            echo '<td>' . $c_row . '</td>';
            next($row);
            $y = $y + 1;
        }
        echo '</tr>';
        $i = $i + 1;
    }

    echo '</table></div>'
    ?>
            
           
</div>
</div>            
        

    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="Index2_files/jquery-3.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script>window.jQuery || document.write('<script src="../../../../assets/js/vendor/jquery.min.js"><\/script>')</script>
    <script src="Index2_files/popper.js"></script>
    <script src="Index2_files/bootstrap.js"></script>
  

</body>
</html>