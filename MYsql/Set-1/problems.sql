--problem 1

CREATE TABLE Customers (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  email TEXT NOT NULL,
  address TEXT NOT NULL,
  phone TEXT NOT NULL
)

--problem 2
INSERT INTO Customers VALUES (1, 'Ryan', 'M@gmail.com', 'Kolkata' , '6291847283');
INSERT INTO Customers VALUES (2, 'Arnold', 'M@gmail.com', 'Kolkata' , '6291847283');
INSERT INTO Customers VALUES (4, 'Johns', 'M@gmail.com', 'Kolkata' , '6291847283');
INSERT INTO Customers VALUES (3, 'Bonny', 'M@gmail.com', 'Kolkata' , '6291847283');
INSERT INTO Customers VALUES (5, 'Ateve', 'M@gmail.com', 'Kolkata' , '6291847283');
--problem 3
SELECT * FROM Customers 

--problem 4
SELECT name, email FROM Customers 

--problem 5
SELECT * FROM Customers WHERE id=3

--problem 6
SELECT * FROM Customers WHERE name LIKE 'A%';

--problem 7
SELECT * FROM Customers ORDER BY name DESC;

--problem 8
UPDATE Customers SET address ='Barasat' WHERE id = 4;

--problems 9
SELECT * FROM Customers
ORDER BY id ASC
LIMIT 3;

--problem 10
DELETE  FROM Customers WHERE id=2;

--problem 11
SELECT COUNT(*) FROM Customers;

--problem 12
SELECT * FROM Customers
WHERE id NOT IN (
  SELECT id FROM Customers
  ORDER BY id ASC
  LIMIT 2
);

--problem 13
SELECT * FROM Customers WHERE name LIKE 'B%'AND id> 2;

--problem 14
SELECT * FROM Customers WHERE name LIKE '%s'

--problem 15
SELECT * FROM Customers WHERE phone IS NULL OR phone=''
