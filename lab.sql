use mini;
create table doner(dno integer primary key auto_increment,name varchar(40),age integer,address varchar(40),username varchar(40),contactnumber varchar(15),bloodgroup varchar(5),email varchar(40),password varchar(20),status varchar(10));
create table stock(stkid integer primary key,blood varchar(10),stk integer);
insert into stock values
(1,"O+",0),
(2,"AB+",0),
(3,"A+",0),
(4,"B+",0),
(5,"O-",0),
(6,"AB-",0),
(7,"A-",0),
(8,"B-",0);
create table login(loginid varchar(10) primary key,password varchar(20),ename varchar(20));
create table employee(employee_id varchar(10) primary key references login(loginid),ename varchar(20),address varchar(20),emailid varchar(40),phone varchar(20));
create table seekers(s_id integer primary key auto_increment,name varchar(20),phone varchar(20),requested varchar(10),given varchar(10),sdate date,quantity integer);
create table stk_collection(stk_id integer references stock(stkid),quanity integer,day date);
-- select * from employee;
insert into employee values
select * from stock;
select * from doner;











