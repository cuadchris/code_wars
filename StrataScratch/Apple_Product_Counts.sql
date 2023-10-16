/*
https://platform.stratascratch.com/coding/10141-apple-product-counts?code_type=1

Find the number of Apple product users and the number of total users with a device and group the counts by language.
Assume Apple products are only MacBook-Pro, iPhone 5s, and iPad-air. Output the language along with the total
number of Apple users and users with any device. Order your results based on the number of total users in
descending order.

Tables:

playbook_events:

| User ID | Timestamp           | Action      | Action Detail | Country           | Device                 |
|---------|---------------------|-------------|---------------|-------------------|------------------------|
| 6991    | 2014-06-09 18:26:54 | Engagement  | Home Page     | United States        | iPhone 5               |
| 18851   | 2014-08-29 13:18:38 | Signup Flow | Enter Info    | Russia               | Asus Chromebook        |
| 14998   | 2014-07-01 12:47:56 | Engagement  | Login         | France               | HP Pavilion Desktop    |
| 8186    | 2014-05-23 10:44:16 | Engagement  | Home Page     | Italy                | MacBook Pro            |
| 9626    | 2014-07-31 17:15:14 | Engagement  | Login         | Russia               | Nexus 7                |
| 16460   | 2014-07-24 18:43:19 | Signup Flow | Create User   | United States        | Samsung Galaxy Note    |
| 10101   | 2014-08-27 05:54:28 | Engagement  | Home Page     | Singapore            | Dell Inspiron Notebook |
| 2670    | 2014-05-10 10:03:34 | Engagement  | Like Message  | United States        | Nexus 7                |
| 8708    | 2014-05-26 10:42:12 | Engagement  | Send Message  | Australia            | MacBook Pro            |
| 167     | 2014-07-30 19:39:13 | Engagement  | View Inbox    | United Arab Emirates | Lenovo Thinkpad        |

playbook_users:

| User ID | Created At          | Company ID | Language | Activated At | State  |
|---------|---------------------|------------|----------|--------------|--------|
| 11      | 2013-01-01 04:41:13 | 1          | German   | 2013-01-01   | Active |
| 52      | 2013-01-05 15:30:45 | 2866       | Spanish  | 2013-01-05   | Active |
| 108     | 2013-01-10 11:04:58 | 1848       | Spanish  | 2013-01-10   | Active |
| 167     | 2013-01-16 20:40:24 | 6709       | Arabic   | 2013-01-16   | Active |
| 175     | 2013-01-16 11:22:22 | 4797       | Russian  | 2013-01-16   | Active |
| 238     | 2013-01-23 11:04:23 | 5027       | Spanish  | 2013-01-23   | Active |
| 251     | 2013-01-24 13:41:38 | 6          | Spanish  | 2013-01-24   | Active |
| 264     | 2013-01-25 17:53:16 | 9801       | Spanish  | 2013-01-25   | Active |
| 358     | 2013-02-03 08:00:45 | 11965      | Italian  | 2013-02-03   | Active |
| 738     | 2013-03-08 01:45:22 | 123        | English  | 2013-03-08   | Active |
| 765     | 2013-03-11 08:00:42 | 2398       | Japanese | 2013-03-11   | Active |
*/

SELECT language,
    COUNT(
        DISTINCT CASE
            WHEN device IN ('macbook pro', 'iphone 5s', 'ipad air') THEN pe.user_id
        END
    ) AS n_apple_users,
    COUNT(DISTINCT pe.user_id) as n_total_users
FROM playbook_events pe
    JOIN playbook_users pu ON pu.user_id = pe.user_id
GROUP BY language
ORDER BY n_total_users DESC