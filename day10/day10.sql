/*
SQLyog Ultimate v11.33 (64 bit)
MySQL - 5.7.26 
*********************************************************************
*/
/*!40101 SET NAMES utf8 */;

create table `user` (
	`account` varchar (60),
	`username` char (60),
	`password` char (24),
	`country` varchar (60),
	`province` varchar (60),
	`street` varchar (60),
	`door` varchar (60),
	`money` int (8),
	`registerDate` timestamp ,
	`bankname` varchar (60)
); 
insert into `user` (`account`, `username`, `password`, `country`, `province`, `street`, `door`, `money`, `registerDate`, `bankname`) values('01566624','1','1','1','1','1','1','1','2021-03-23 14:42:23','中国工商银行回龙观支行');
insert into `user` (`account`, `username`, `password`, `country`, `province`, `street`, `door`, `money`, `registerDate`, `bankname`) values('33097988','1','1','1','1','1','1','2','2021-03-23 14:42:24','中国工商银行回龙观支行');
insert into `user` (`account`, `username`, `password`, `country`, `province`, `street`, `door`, `money`, `registerDate`, `bankname`) values('1','1','1','1','1','1','1','1','2021-03-23 14:47:51','中国工商银行回龙观支行');
