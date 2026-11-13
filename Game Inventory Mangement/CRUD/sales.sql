 -- Create Database
create database sales;

-- Activate Databse
use sales;

-- Create Table
Create table tblGameProduct (
GameCode varchar (10) not null primary key,
GameName varchar (100) not null,
GamePrice int not null);

Create table tblGameAccessoryProduct (
AccessoryCode varchar (30) not null primary key,
AccessoryName varchar (50) not null,
AccessoryPrice int not null);

Create table tblEmployees (
EmployeeID varchar (10) not null primary key,
Fname varchar (50) not null,
Lname varchar (50) not null);

-- add Records
Insert Into  tblGameProduct values ('Game-01', "Assassin's Creed Syndicate", 3500 ),
('Game-02', 'Horizon Zero Dawn', 2545), ('Game-03', 'Apex Legends', 1000),
('Game-04', 'Spider-man', 1995), ('Game-05', 'Spider-man 2', 3490);

Insert Into  tblGameAccessoryProduct values ('Accessory-01', 'Gaming Headset', 4895),
('Accessory-02', 'Controller Charging Dock', 400), ('Accessory-03', 'External Hard Drive', 1028),
('Accessory-04', 'Disc Storage', 190), ('Accessory-05', 'Gaming Chair', 36000);

Insert Into tblEmployees values ('ID-01', 'John', 'Smith'),
('ID-02','Sarah','Taylor'), ('ID-03', 'Juan', 'Dela Cruz'),
('ID-04', 'Maria','Clara'), ('ID-05', 'Tom', 'Anderson');        

SELECT * FROM sales.tblgameproduct;
SELECT * FROM sales.tblgameaccessoryproduct;
SELECT * FROM sales.tblemployees;