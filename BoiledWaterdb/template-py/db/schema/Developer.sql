CREATE TABLE Developer (

D_name varchar(255) PRIMARY KEY  NOT NULL,

FOREIGN KEY (D_name) REFERENCES Games(D_name)
)

