WELCOME TO BOILEDWATERDB

Steps to installing the Database:
You Will Need: 

Python

Xamp

PostgreSQL with PG Admin 4

The BoiledWaterDB repository


Simplified install:
1. Install Postgre following the lab7. https://github.com/sealneaward/data-management-lab-7
2. Install Xamp with default settings
3. Create the tables in Postgre

	a. See the example query provided

	b. Manually add in the foreign key contraints if query with foreign key constraints do not work

		i. This can be done by removing the foreign key constraints in the create table query and manually add it in

4. Download the repository
5. Click boiledwaterdbpopulate.py

	a. Wait for it to finish

6. Put the php file in the :PATH:\Xamp\htdocs

In Depth install:
1. Create a database called boiledwaterdb, and create the 5 tables. In the folder this read me is in, in "SQL Captures" There is a txt file with all create table statements.
2. To populate the database, run boiledwaterdbpopulate.py in template-py\db

	a. Make sure that the file username and passwords are correct

	b. This file will only populate until app_id reaches 500. This is to temporarily limit the amount of games listed

		i. You can change the amount to any number. The higher the number, the longer it will take to populate

		ii. make sure to change all instances of 500 to your number in the code when changing it

3. Put the .php files along with the connected files located in template-py\web\htdocs to the path of your Xamp\htdocs folder


sss



