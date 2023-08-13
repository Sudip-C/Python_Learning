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
INSERT INTO Restaurants VALUES (2, 'Arnold', 'Continental', 'Mumbai' , 4.1,false);
INSERT INTO Restaurants VALUES (4, 'Johns', 'Chinese', 'Kolkata' , 4.2,true);
INSERT INTO Restaurants VALUES (3, 'Bonny', 'Korean', 'Bangalore' , 4.3,true);
INSERT INTO Restaurants VALUES (5, 'Ateve', 'Japanese', 'Mumbai' , 4.7,false);

--problem 3
 SELECT * FROM Restaurants ORDER BY average_rating DESC