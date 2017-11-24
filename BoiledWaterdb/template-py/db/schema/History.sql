CREATE TABLE History (
    History_ID int PRIMARY KEY NOT NULL AUTO_INCREMENT,
    App_id int NOT NULL,
    Score double NOT NULL,
    Price float NOT NULL,
    YearMonth int NOT NULL,
     
   FOREIGN KEY (App_id) REFERENCES Games(App_id)
   
)

