CREATE TABLE Publisher (

Publisher_name varchar(255) PRIMARY KEY NOT NULL,

FOREIGN KEY (Publisher_name) REFERENCES Games(publisher_name)

)

