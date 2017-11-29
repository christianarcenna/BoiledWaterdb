<?php 
    $conn = pg_connect("host=localhost port=5432 dbname=boiledwaterdb user=root password=root"); //Connects to boiledwaterdb
    if (!$conn) {
        echo "An error occurred.\n";
        exit;
    }


    $url_name = $_GET["name"];

    $result = pg_query($conn, "SELECT * FROM games
                                WHERE app_name='$url_name'");
    if (!$result) {
        echo "An error occurred.\n";
        exit;
    }
    // check if the query succeeded
    if (!$result) {
      die('There was an error running the query[' . $db->error . ']');
    }
    // Display the results of the query for each row

    //Print out= json from SQL Query
    while ($row = pg_fetch_assoc($result)) 
    {
		$rows[] = $row;
    }  
	$boiled_json = json_encode($rows, JSON_FORCE_OBJECT);
	print $boiled_json;
    
?>