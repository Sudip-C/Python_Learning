--problem 1
CREATE TABLE Rides (
    id INT AUTO_INCREMENT PRIMARY KEY,
    driver_id INT,
    passenger_id INT,
    start_location VARCHAR(255),
    end_location VARCHAR(255),
    distance DECIMAL(5,2),
    ride_time DECIMAL(5,2),
    fare DECIMAL(6,2)
)

--problem 2
INSERT INTO Rides VALUES (1,1,1,"Kolkata","Belgharia",10.75,1.5,300);
INSERT INTO Rides VALUES (2,2,2,"Downtown","Sikkim",90,3,300);
INSERT INTO Rides VALUES (3,1,3,"Howrah","Downtown",20,2,300);
INSERT INTO Rides VALUES (4,2,4,"Kolkata","Howrah",10.75,1,300);
INSERT INTO Rides VALUES (5,3,5,"Central Avenue","Barasat",30,3.5,300);
INSERT INTO Rides VALUES (6,3,6,"Barasat","Howrah",10.75,2,300);

--problem 3
SELECT * FROM Rides

--problem 4
SELECT SUM(distance) as total_distance , SUM(fare) as Total_fare  FROM Rides

--problem 5
SELECT AVG( ride_time) as total_ride_time FROM Rides

--[problem 6]
SELECT * FROM Rides WHERE start_location = 'Downtown' OR end_location = 'Downtown'

--problem 7
SELECT COUNT(*) FROM Rides WHERE driver_id = 2 

--problem 8
UPDATE Rides SET fare=500 WHERE id = 4

--problem 9
SELECT driver_id, SUM(fare) AS total_fare FROM Rides GROUP BY driver_id;

--problem 10
DELETE FROM Rides WHERE id= 2;