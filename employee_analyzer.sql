CREATE DATABASE IF NOT EXISTS employee_analyzer;
USE employee_analyzer;

DROP TABLE IF EXISTS attendances;
DROP TABLE IF EXISTS performance;
DROP TABLE IF EXISTS departments;
DROP TABLE IF EXISTS employees;

CREATE TABLE employees (
    emp_id VARCHAR(10) PRIMARY KEY,
    department_id VARCHAR(10),
    name VARCHAR(100),
    salary DECIMAL(10,2),
    designation VARCHAR(50),
    contact_no VARCHAR(15)
);

INSERT INTO employees VALUES
('E001','D01','Neha Varma',25000,'Software Developer','9876543210'),
('E002','D02','Tanuja Singh',20000,'Data Analyst','1234567890'),
('E003','D03','Aman Kapoor',22000,'HR Executive','2134567800'),
('E004','D04','Nita Pawar',73000,'Accountant','3214567891'),
('E005','D01','Jyoti Bellad',350000,'Software Developer','4321567899'),
('E006','D02','Nitya Bilur',99000,'Data Analyst','7541567899'),
('E007','D03','Jyoti Bellad',59000,'HR Executive','4321567899'),
('E008','D04','Divya Kamble',43000,'Accountant','1009876567'),
('E009','D01','Pooja Bhairodgi',64000,'Software Developer','964890242'),
('E010','D01','Srushti Gugwad',78000,'Data Analyst','7856020768'),
('E011','D02','Tejsvi Gaikwad',88000,'HR Executive','8654234526'),
('E012','D03','Ganesh Suryawanshi',30000,'Accountant','8875428910'),
('E013','D04','Shreyash Salunke',82000,'Software Developer','9634278231'),
('E014','D01','Avdhut Walande',58000,'Data Analyst','9234571891'),
('E015','D02','Nilam Sharma',53000,'HR Executive','9256283217'),
('E016','D03','Naina Talwad',94000,'Accountant','8974261781'),
('E017','D04','Rohan Pise',84000,'Software Developer','1267418902'),
('E018','D01','Suhas Gone',77000,'Data Analyst','9527850140'),
('E019','D02','Gauri Bagali',37000,'HR Executive','9247178900'),
('E020','D03','Shreya Patil',88000,'Accountant','2356189079'),
('E021','D04','Amit Chavan',71000,'Software Developer','4230016501'),
('E022','D01','Atish More',45000,'Data Analyst','9042014568'),
('E023','D02','Omkar Ingle',51000,'HR Executive','9261680065'),
('E024','D03','Kiran Mandana',67000,'Accountant','2315278254'),
('E025','D04','Riya Hakkapki',44000,'Software Developer','9614591563'),
('E026','D01','Ritika Badage',65000,'Data Analyst','2542895640'),
('E027','D02','Sakshi Chaugule',56000,'HR Executive','1249615678'),
('E028','D03','Aditya Sharma',34000,'Accountant','9649851567'),
('E029','D04','Govind Salunke',37000,'Software Developer','8764389421'),
('E030','D01','Shifa Khan',60000,'Data Analyst','5678321444');

CREATE TABLE departments (
    dept_id VARCHAR(10) PRIMARY KEY,
    dept_name VARCHAR(30)
);

INSERT INTO departments VALUES
('D01','Finance'),
('D02','Marketing'),
('D03','IT'),
('D04','HR');

CREATE TABLE attendances (
    attendance_id VARCHAR(10) PRIMARY KEY,
    emp_id VARCHAR(10),
    attendance_date DATE,
    status VARCHAR(10),
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id)
);

INSERT INTO attendances VALUES
('A001','E001','2026-01-08','Present'),
('A002','E002','2026-02-09','Present'),
('A003','E003','2026-01-02','Present'),
('A004','E004','2026-02-11','Absent'),
('A005','E005','2026-03-16','Absent'),
('A006','E006','2026-02-11','Absent'),
('A007','E007','2026-01-11','Present'),
('A008','E008','2026-02-11','Present'),
('A009','E009','2026-03-05','Present'),
('A010','E010','2026-01-06','Absent'),
('A011','E011','2026-02-12','Absent'),
('A012','E012','2026-02-22','Absent'),
('A013','E013','2026-06-11','Present'),
('A014','E014','2026-04-01','Present'),
('A015','E015','2026-04-02','Present'),
('A016','E016','2026-04-03','Absent'),
('A017','E017','2026-04-04','Absent'),
('A018','E018','2026-04-05','Absent'),
('A019','E019','2026-04-06','Present'),
('A020','E020','2026-04-07','Present'),
('A021','E021','2026-04-08','Present'),
('A022','E022','2026-04-09','Absent'),
('A023','E023','2026-04-10','Absent'),
('A024','E024','2026-04-11','Absent'),
('A025','E025','2026-04-12','Present'),
('A026','E026','2026-04-13','Present'),
('A027','E027','2026-04-14','Present'),
('A028','E028','2026-04-15','Absent'),
('A029','E029','2026-04-16','Absent'),
('A030','E030','2026-04-17','Absent');

CREATE TABLE performance (
    performance_id VARCHAR(10) PRIMARY KEY,
    emp_id VARCHAR(10),
    performance_date DATE,
    task_assigned INT,
    task_completed INT,
    quality_score INT,
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id)
);

INSERT INTO performance VALUES
('P001','E001','2026-03-02',11,9,85),
('P002','E002','2026-03-03',18,11,80),
('P003','E003','2026-03-04',12,9,90),
('P004','E004','2026-03-05',10,9,85),
('P005','E005','2026-03-06',20,14,90),
('P006','E006','2026-03-07',11,19,75),
('P007','E007','2026-03-08',12,7,67),
('P008','E008','2026-03-09',20,18,87),
('P009','E009','2026-03-10',10,7,80),
('P010','E010','2026-03-11',19,11,54),
('P011','E011','2026-03-12',14,9,78),
('P012','E012','2026-03-13',10,8,90),
('P013','E013','2026-03-14',15,12,73),
('P014','E014','2026-03-15',12,8,79),
('P015','E015','2026-03-16',20,19,98),
('P016','E016','2026-03-17',14,11,74),
('P017','E017','2026-03-18',11,10,80),
('P018','E018','2026-03-19',13,9,77),
('P019','E019','2026-03-20',12,5,59),
('P020','E020','2026-03-21',10,7,74),
('P021','E021','2026-03-22',15,14,89),
('P022','E022','2026-03-23',20,9,59),
('P023','E023','2026-03-23',12,18,71),
('P024','E024','2026-03-25',16,12,80),
('P025','E025','2026-03-26',17,15,82),
('P026','E026','2026-03-27',16,9,64),
('P027','E027','2026-03-28',15,11,69),
('P028','E028','2026-02-28',12,8,62),
('P029','E029','2026-02-03',24,20,87),
('P030','E030','2026-07-05',10,9,80);

SHOW TABLES;