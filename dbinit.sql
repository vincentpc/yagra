
CREATE DATABASE IF NOT EXISTS `yagra`;

DROP TABLE IF EXISTS `yagra`.`yagra_user`;


-- 用户表
CREATE TABLE `yagra`.`yagra_user` (
  `ID` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `user_login` varchar(60) NOT NULL DEFAULT '',
  `user_passwd` varchar(64) NOT NULL DEFAULT '',
  `user_email` varchar(100) NOT NULL DEFAULT '',
  `user_time` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `user_status` int(11) NOT NULL DEFAULT '0',
  `display_name` varchar(256) NOT NULL DEFAULT '',
  PRIMARY KEY (`ID`),
  KEY `user_login_key` (`user_login`),
  KEY `user_email_key` (`user_email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



-- 添加用户
GRANT select, update, insert, delete ON yagra.* to `yagra`@`localhost` IDENTIFIED BY 'abcd!1234';
FLUSH PRIVILEGES;
