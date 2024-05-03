# **Task 2**
   #### *  Create a new database named website.
       create database website;
       ![image](https://github.com/Amelia147957/Amelia147957.github.io/blob/main/WeHelp/Assignment_5/pic/task2-1.jpg)
       ![Amelia147957.github.io](task2-1.jpg)
       
        <img src="[src-url](https://github.com/Amelia147957/Amelia147957.github.io/blob/main/WeHelp/Assignment_5/pic/task2-1.jpg)" height="240px" width="160px" />
   #### *  Create a new table named member, in the website database, designed as below:
        CREATE TABLE member(id BIGINT PRIMARY KEY AUTO_INCREMENT COMMENT 'Unique ID',name VARCHAR(255) NOT NULL COMMENT 'Name',username VARCHAR(255) NOT NULL COMMENT 'Username',password VARCHAR(255) NOT NULL COMMENT 'Password',follower_count INT UNSIGNED NOT NULL DEFAULT 0 COMMENT 'Follower Count',time DATETIME NOT NULL DEFAULT(CURRENT_TIME) COMMENT 'Signup Time')
