WELCOME TO BOILEDWATERDB

Steps to installing the Database:

You Will Need: 

Python 2.7

XAMPP

PostgreSQL with PG Admin 4

The BoiledWaterDB repository




Simplified install:


1. Install Postgre following the lab7 https://github.com/sealneaward/data-management-lab-7
2. Install XAMPP with default settings
3. Install Python 2.7 and the required packages in the boiledwaterpopulate.py
4. Create the tables in Postgre

	a. See the example query provided

	b. Manually add in the foreign key contraints if query with foreign key constraints do not work

		i. This can be done by removing the foreign key constraints in the create table query and manually add it in

5. Download the repository, the master branch.
6. Click boiledwaterdbpopulate.py

	a. Wait for it to finish

7. Put the php file in the :PATH:\Xampp\htdocs




In Depth install:

1. Install Postgre following the lab7 https://github.com/sealneaward/data-management-lab-7
2. Install XAMPP with default settings
3. Install Python 2.7 and the required packages in the boiledwaterpopulate.py 
4. Download the repository from the master branch
5. Create a database called boiledwaterdb, and create the 5 tables. In the folder "SQL Captures" there is a txt file with all create table statements.
6. To populate the database, run boiledwaterdbpopulate.py

	a. Make sure that the file username and passwords are correct

	b. This file will only populate until app_id reaches 500. This is to temporarily limit the amount of games listed

		i. You can change the amount to any number. The higher the number, the longer it will take to populate

		ii. make sure to change all instances of 500 to your number in the code when changing it

7. Put connect.php file and the contents of the htdocs folder to the path of your Xampp\htdocs folder




THATS IT!








