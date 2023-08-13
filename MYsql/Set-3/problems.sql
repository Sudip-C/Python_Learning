--problem 1
CREATE TABLE Rides (
    id INT PRIMARY KEY,
    driver_id INT,
    passenger_id INT,
    ride_date DATE,
    start_location VARCHAR(255),
    end_location VARCHAR(255),
    distance DECIMAL(5,2),
    ride_time DECIMAL(5,2),
    fare DECIMAL(6,2)
);
CREATE TABLE Drivers (
    driver_id INT,
    name VARCHAR(100)
);

CREATE TABLE Passengers (
    passenger_id INT,
    name VARCHAR(100)
);

INSERT INTO Drivers VALUES (1,'John Doe');
INSERT INTO Drivers VALUES (2, 'Bonny');
INSERT INTO Drivers VALUES (3, 'Clyde');

INSERT INTO Passengers VALUES (1,"Sudip");
INSERT INTO Passengers VALUES (2,"Rahul");
INSERT INTO Passengers VALUES (3,"Jhonny");
INSERT INTO Passengers VALUES (4,"Alex");
INSERT INTO Passengers VALUES (5,"Rakesh");
INSERT INTO Passengers VALUES (6,"Bob");

--problems 2
INSERT INTO Rides VALUES (1,1,1,'2023-08-12',"Kolkata","Belgharia",10.75,1.5,300);
INSERT INTO Rides VALUES (2,2,2,'2023-08-13',"Downtown","Sikkim",90,3,600);
INSERT INTO Rides VALUES (3,1,3,'2023-08-10',"Howrah","Downtown",20,2,300);
INSERT INTO Rides VALUES (4,2,4,'2023-08-10',"Kolkata","Howrah",10.75,1,150);
INSERT INTO Rides VALUES (5,3,5,'2023-08-10',"Central Avenue","Barasat",30,3.5,450);
INSERT INTO Rides VALUES (6,3,6,'2023-08-10',"Barasat","Howrah",10.75,2,200);
INSERT INTO Rides VALUES (7,1,1,'2023-08-10',"Kolkata","",10.75,1.5,300);
INSERT INTO Rides VALUES (8,1,2,'2023-08-06',"Kolkata","Belgharia",10.75,1.5,300);
INSERT INTO Rides VALUES (9,1,3,'2023-08-12',"Kolkata","Belgharia",10.75,1.5,300);
INSERT INTO Rides VALUES (10,1,3,'2023-08-12',"Kolkata","",10.75,1.5,300);

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

--problems 11
SELECT MAX(fare), MIN(fare) FROM Rides

--problem 12
SELECT driver_id, AVG(fare) AS avg_fare , AVG(distance) AS avg_dist FROM Rides GROUP BY driver_id;

--probblem 13
SELECT driver_id, COUNT(*) AS ride_count FROM Rides GROUP BY driver_id HAVING COUNT(*) > 5;

--problem 14
SELECT d.name
FROM Drivers AS d
WHERE d.driver_id = (
    SELECT r.driver_id
    FROM Rides AS r
    ORDER BY r.fare DESC
    LIMIT 1
);

--problem 15
SELECT
    r.driver_id,
    d.name,
    SUM(r.fare) AS total_earnings
FROM
    Rides AS r
JOIN
    Drivers AS d ON r.driver_id = d.driver_id
GROUP BY
    r.driver_id, d.name
ORDER BY
    total_earnings DESC
LIMIT 3;

--problem 16


--problem 17
SELECT * FROM Rides WHERE end_location=''OR end_location IS NULL

--problem 18
SELECT id AS ride_id,  fare / distance AS fare_per_mile FROM Rides WHERE distance > 0 ORDER BY fare_per_mile DESC;

--problem 19
SELECT R.id AS ride_id, D.name AS driver_name, P.name AS passenger_name FROM Rides AS R
JOIN 
    Drivers AS D ON R.driver_id = D.driver_id
JOIN
    Passengers AS P ON R.passenger_id = P.passenger_id;

--problem 20
ALTER TABLE Rides
ADD COLUMN tip DECIMAL(6, 2);

--add new rides with tip
INSERT INTO Rides VALUES (11,1,3,'2023-08-12',"Kolkata","",10.75,1.5,300,25);