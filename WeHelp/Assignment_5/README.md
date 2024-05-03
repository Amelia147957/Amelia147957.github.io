# **Task 2**
   #### * Create a new database named website
   <pre><code>
      create database website;
   </code>
   </pre>
   ![task2-1](https://github.com/Amelia147957/Amelia147957.github.io/blob/main/WeHelp/Assignment_5/pic/task2-1.jpg)
   #### * Create a new table named member, in the website database, designed as below:
   <pre><code>CREATE TABLE member(id BIGINT PRIMARY KEY AUTO_INCREMENT COMMENT 'Unique ID',name VARCHAR(255) NOT NULL COMMENT 'Name',username VARCHAR(255) NOT NULL COMMENT 'Username',password VARCHAR(255) NOT NULL COMMENT 'Password',follower_count INT UNSIGNED NOT NULL DEFAULT 0 COMMENT 'Follower Count',time DATETIME NOT NULL DEFAULT(CURRENT_TIME) COMMENT 'Signup Time')
   </code>
   </pre>
   ![task2-2](https://github.com/Amelia147957/Amelia147957.github.io/blob/main/WeHelp/Assignment_5/pic/task2-2.jpg)
   
# **Task 3**
   #### * INSERT a new row to the member table where name, username and password must be set to test. INSERT additional 4 rows with arbitrary data.
   <pre><code>
      NSERT INTO member (name, username, password) VALUES ("test", "test", "test"),("abc","abc","123"),("def","def","456"),("aaaa","aaaa","1111"),("bbbb","bbbb","2222");
   </code>
   </pre>
   ![task3-1](https://github.com/Amelia147957/Amelia147957.github.io/blob/main/WeHelp/Assignment_5/pic/task3-1.jpg)
   #### * SELECT all rows from the member table.
   <pre><code>
   SELECT * FROM member;
   </code>
   </pre>
   ![task3-2](https://github.com/Amelia147957/Amelia147957.github.io/blob/main/WeHelp/Assignment_5/pic/task3-2.jpg)
   #### * SELECT all rows from the member table, in descending order of time.
   <pre><code>
   SELECT * from member ORDER BY time DESC;
   </code>
   </pre>
   ![task3-3](https://github.com/Amelia147957/Amelia147957.github.io/blob/main/WeHelp/Assignment_5/pic/task3-3.jpg)
   #### * SELECT total 3 rows, second to fourth, from the member table, in descending order of time. Note: it does not mean SELECT rows where id are 2, 3, or 4.
   <pre><code>
   SELECT * FROM member ORDER BY time DESC LIMIT 3 OFFSET 1;
   </code>
   </pre>
   ![task3-4](https://github.com/Amelia147957/Amelia147957.github.io/blob/main/WeHelp/Assignment_5/pic/task3-4.jpg)
  #### * SELECT rows where username equals to test.
  <pre><code>
     SELECT * FROM member WHERE username = "test";
  </code>
  </pre>
  ![task3-5](https://github.com/Amelia147957/Amelia147957.github.io/blob/main/WeHelp/Assignment_5/pic/task3-5.jpg)
  #### * SELECT rows where name includes the es keyword.
  <pre><code>
  SELECT name FROM member WHERE name like "%es%";
   </code>
  </pre>
  ![task3-6](https://github.com/Amelia147957/Amelia147957.github.io/blob/main/WeHelp/Assignment_5/pic/task3-6.jpg)
  #### * SELECT rows where both username and password equal to test.
  <pre><code>
  SELECT * FROM member WHERE username = "test" AND password = "test";
  </code>
  </pre>
  ![task3-7](https://github.com/Amelia147957/Amelia147957.github.io/blob/main/WeHelp/Assignment_5/pic/task3-7.jpg)
  #### * UPDATE data in name column to test2 where username equals to test.
  <pre><code>
  UPDATE member SET name = "test2" WHERE username = "test";
  </code>
  </pre>
   ![task3-8](https://github.com/Amelia147957/Amelia147957.github.io/blob/main/WeHelp/Assignment_5/pic/task3-8.jpg)
   
   # **Task 4**
   #### * SELECT how many rows from the member table.
   <pre><code>
   SELECT COUNT(*) FROM member;
   </code>
  </pre>
  ![task4-1](https://github.com/Amelia147957/Amelia147957.github.io/blob/main/WeHelp/Assignment_5/pic/task4-1.jpg)
  #### * SELECT the sum of follower_count of all the rows from the member table.
現在才發現要算follower_count，所以用了UPDATE member SET follower_count = 100 WHERE id = 1;以此類推的方式補資料進去。
   ![task4-2](https://github.com/Amelia147957/Amelia147957.github.io/blob/main/WeHelp/Assignment_5/pic/task4-2.jpg)
   <pre><code>
   SELECT SUM(follower_count) AS total_followers_rows FROM member;
   </code>
  </pre>
  ![task4-3](https://github.com/Amelia147957/Amelia147957.github.io/blob/main/WeHelp/Assignment_5/pic/task4-3.jpg)
  #### * SELECT the average of follower_count of all the rows from the member table.
  <pre><code>
     SELECT AVG(follower_count) AS average_followers FROM member;
   </code>
  </pre>
  ![task4-4](https://github.com/Amelia147957/Amelia147957.github.io/blob/main/WeHelp/Assignment_5/pic/task4-4.jpg)
 #### * SELECT the average of follower_count of the first 2 rows, in descending order of follower_count, from the member table.
 <pre><code>
   SELECT AVG(follower_count) AS average_followers FROM (
    SELECT follower_count FROM member ORDER BY follower_count DESC LIMIT 2
) AS top_two_followers;
   </code>
  </pre>
  ![task4-5](https://github.com/Amelia147957/Amelia147957.github.io/blob/main/WeHelp/Assignment_5/pic/task4-5.jpg)
 # **Task 5**
 #### * Create a new table named message, in the website database. designed as below.
 <pre><code>
   CREATE TABLE message(
     id BIGINT PRIMARY KEY AUTO_INCREMENT COMMENT 'Unique ID',
     member_id BIGINT NOT NULL COMMENT 'Member ID for Message Sender',
     content VARCHAR(255) NOT NULL COMMENT 'Content',
     like_count INT UNSIGNED NOT NULL DEFAULT 0 COMMENT 'Like Count',
     time DATETIME NOT NULL DEFAULT(CURRENT_TIME) COMMENT 'Publish Time',
     FOREIGN KEY (member_id) REFERENCES member(id) ON DELETE CASCADE);
   </code>
  </pre>
  ![task5-1](https://github.com/Amelia147957/Amelia147957.github.io/blob/main/WeHelp/Assignment_5/pic/task5-1.jpg)
#### * SELECT all messages, including sender names. We have to JOIN the member table to get that.
<pre><code>
SELECT * FROM  message ms JOIN member mb ON ms.member_id = mb.id;
</code>
  </pre>
![task5-2](https://github.com/Amelia147957/Amelia147957.github.io/blob/main/WeHelp/Assignment_5/pic/task5-2.jpg)
#### * SELECT all messages, including sender names, where sender username equals to test. We have to JOIN the member table to filter and get that.
<pre><code>
SELECT * FROM  message ms JOIN member mb ON ms.member_id = mb.id WHERE ab.username = "test";
</code>
</pre>
![task5-3](https://github.com/Amelia147957/Amelia147957.github.io/blob/main/WeHelp/Assignment_5/pic/task5-3.jpg)
#### * Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages where sender username equals to test.
<pre><code>
   SELECT AVG(ms.like_count) AS average_likes
   FROM message ms
   JOIN member mb ON ms.member_id = mb.id
   WHERE mb.username = 'test';
</code>
</pre>
![task5-4](https://github.com/Amelia147957/Amelia147957.github.io/blob/main/WeHelp/Assignment_5/pic/task5-4.jpg)
#### * Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages GROUP BY sender username.
<pre><code>
   SELECT mb.username, AVG(ms.like_count) AS average_likes
   FROM message ms
   JOIN member mb ON ms.member_id = mb.id
   GROUP BY mb.username;
</code>
</pre>
![task5-5](https://github.com/Amelia147957/Amelia147957.github.io/blob/main/WeHelp/Assignment_5/pic/task5-5.jpg)
   



