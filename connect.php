<?php 
$conn = pg_connect("host=localhost port=5432 dbname=boiledwaterdb user=root password=root"); //Connects to boiledwaterdb
if (!$conn) {
    echo "An error occurred.\n";
    exit;
}
$result = pg_query($conn, "SELECT * FROM games");
if (!$result) {
    echo "An error occurred.\n";
    exit;
}
// check if the query succeeded
if (!$result) {
  die('There was an error running the query[' . $db->error . ']');
}
// Display the results of the query for each row
echo "<table id='database'> <tr> <th> App ID </th> <th> App Name </th> <th> Release Date </th> <th> Genre </th> <th> Sales </th> <th> Developer ID </th>
		<th> Publisher ID </th> <th> Price </th> <th> Metacritic </th> </tr>";
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
?>