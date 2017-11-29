WELCOME TO BOILEDWATERDB

Steps to installing the Database:

You Will Need: 

Python

Xamp

PostgreSQL with PG Admin 4

The BoiledWaterDB repository




Simplified install:


1. Install Postgre following the lab7 https://github.com/sealneaward/data-management-lab-7
2. Install Xamp with default settings
3. Create the tables in Postgre

	a. See the example query provided

	b. Manually add in the foreign key contraints if query with foreign key constraints do not work

		i. This can be done by removing the foreign key constraints in the create table query and manually add it in

4. Download the repository, the master branch.
5. Click boiledwaterdbpopulate.py

	a. Wait for it to finish

6. Put the php file in the :PATH:\Xamp\htdocs




In Depth install:

1. Follow the instructions to install PostgreSQL https://github.com/sealneaward/data-management-lab-7
2. Install Xamp with default settings
3. Download the repository from the master branch
4. Create a database called boiledwaterdb, and create the 5 tables. In the folder this read me is in, in "SQL Captures" There is a txt file with all create table statements.
5. To populate the database, run boiledwaterdbpopulate.py

	a. Make sure that the file username and passwords are correct

	b. This file will only populate until app_id reaches 500. This is to temporarily limit the amount of games listed

		i. You can change the amount to any number. The higher the number, the longer it will take to populate

		ii. make sure to change all instances of 500 to your number in the code when changing it

6. Put connect.php file and the contents of the htdocs folder to the path of your Xamp\htdocs folder




THATS IT!








