CREATE DATABASE PRAC9;
GO

USE PRAC9;
GO

CREATE TABLE SalesStage (
SalesID INT PRIMARY KEY,
OrderDate DATE,
ProductName VARCHAR(100),
Category VARCHAR(50),
Region VARCHAR(50),
SalesAmount DECIMAL(10,2),
Profit DECIMAL(10,2),
Quantity INT,
LoadDate DATETIME DEFAULT CURRENT_TIMESTAMP,
BatchID INT
);
GO

INSERT INTO SalesStage
(SalesID, OrderDate, ProductName, Category, Region, SalesAmount, Profit, Quantity, BatchID)
VALUES
(1,'2024-01-01','Laptop','Electronics','North',1200,200,3,101),
(2,'2024-01-02','Smartphone','Electronics','South',800,150,2,101),
(3,'2024-01-03','Tablet','Electronics','East',600,100,5,101);
GO

SELECT  FROM SalesStage;
GO

DELETE FROM SalesStage
WHERE SalesID NOT IN (
SELECT MIN(SalesID)
FROM SalesStage
GROUP BY OrderDate, ProductName, Region
);
GO

UPDATE SalesStage
SET Profit = 0
WHERE Profit IS NULL;
GO

DELETE FROM SalesStage
WHERE BatchID = 101;
GO