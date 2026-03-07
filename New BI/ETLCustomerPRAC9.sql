CREATE DATABASE CustomerOLTP;
CREATE DATABASE CustomerStaging;
CREATE DATABASE CustomerDW;

USE CustomerOLTP;

CREATE TABLE CustOLTP(
custid INT,
custname VARCHAR(50),
address VARCHAR(50),
sal INT
);

INSERT INTO CustOLTP VALUES
(1,'Rahul','Mumbai',50000),
(2,'Amit','Delhi',60000),
(3,'Sneha','Pune',55000),
(4,'Riya','Nashik',65000),
(5,'Karan','Thane',70000);


USE CustomerStaging;

CREATE TABLE CustStaging(
custid INT,
custname VARCHAR(50),
address VARCHAR(50),
sal INT
);

INSERT INTO CustomerStaging.dbo.CustStaging
SELECT * FROM CustomerOLTP.dbo.CustOLTP;

USE CustomerDW;

CREATE TABLE CustDW(
cid INT,
cname VARCHAR(50),
addrs VARCHAR(50),
salINR INT,
salDollar FLOAT
);


INSERT INTO CustDW
SELECT
custid,
UPPER(custname),
address,
sal,
sal/70
FROM CustomerStaging.dbo.CustStaging;



SELECT * FROM CustomerOLTP.dbo.CustOLTP;
SELECT * FROM CustomerStaging.dbo.CustStaging;
SELECT * FROM CustDW;