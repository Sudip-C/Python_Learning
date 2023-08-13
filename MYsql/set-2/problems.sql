--problem 1
CREATE TABLE Restaurants (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    cuisine_type VARCHAR(100),
    location VARCHAR(255),
    average_rating DECIMAL(3,2),
    delivery_available BOOLEAN
);

--problem 2
INSERT INTO Restaurants VALUES (1, 'Ryan', 'Indian', 'Kolkata' , 4.9,true);
INSERT INTO Restaurants VALUES (2, 'Arnold', 'Continental', 'New york' , 4.1,false);
INSERT INTO Restaurants VALUES (4, 'Johns', 'Chinese', 'Kolkata' , 3.9,true);
INSERT INTO Restaurants VALUES (3, 'Bonny', 'Korean', 'Bangalore' , 4.3,true);
INSERT INTO Restaurants VALUES (5, 'Ateve', 'Japanese', 'Mumbai' , 4.7,false);

--problem 3
 SELECT * FROM Restaurants ORDER BY average_rating DESC

--problem 4
SELECT * FROM Restaurants WHERE delivery_available=true AND average_rating > 4

--problem 5
SELECT * FROM Restaurants WHERE cuisine_type='' OR cuisine_type IS NULL 

--problem 6
SELECT COUNT(*) FROM Restaurants WHERE delivery_available = true

--problem 7
SELECT * FROM Restaurants WHERE location ='New york'

--problem 8
SELECT AVG(average_rating) AS average FROM Restaurants;
