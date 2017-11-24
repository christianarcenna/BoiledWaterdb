CREATE TABLE DLC (

DLC_id int PRIMARY KEY NOT NULL,
App_Id varchar(255) NOT NULL,
DLC_name varchar(255) NOT NULL,
Price float NOT NULL,
Release_date varchar(255),
sales int NOT NULL,

FOREIGN KEY (App_Id) REFERENCES Games (App_Id)
)

