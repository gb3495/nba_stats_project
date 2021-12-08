LOAD DATA LOCAL INFILE 'C:/Users/butle/OneDrive/Desktop/School/Fall 2021/Database Design & Applications (CS 286)/Final Project/Raw Data/atlantaHawks.csv'
INTO TABLE atlhawks
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;