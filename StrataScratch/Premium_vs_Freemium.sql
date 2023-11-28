/*
Find the total number of downloads for paying and non-paying users by date. Include only records where non-paying
customers have more downloads than paying customers. The output should be sorted by earliest date first and
contain 3 columns date, non-paying downloads, paying downloads.


(Example data)

Tables:

ms_user_dimension:
--------------------
| user_id | acc_id |
--------------------
|    1    |   716  |
|    2    |   749  |
|    3    |   713  |
|    4    |   744  |
|    5    |   726  |

ms_acc_dimension:
----------------------------
| Acc_id | Paying_customer |
----------------------------
|  700   |        no       |
|  701   |        no       |
|  702   |        no       |
|  703   |        no       |
|  704   |        no       |
|  705   |        no       |
|  706   |        no       |
|  707   |        no       |
|  708   |        no       |
|  709   |        no       |
|  710   |        no       |
|  711   |        no       |

ms_download_facts:
-------------------------------------
|    Date    | User_id | Downloads  |
-------------------------------------
| 2020-08-24 |    1    |     6      |
| 2020-08-22 |    2    |     6      |
| 2020-08-18 |    3    |     2      |
| 2020-08-24 |    4    |     4      |
| 2020-08-19 |    5    |     7      |
| 2020-08-21 |    6    |     3      |
| 2020-08-24 |    7    |     1      |
| 2020-08-24 |    8    |     8      |
| 2020-08-17 |    9    |     5      |
| 2020-08-16 |   10    |     4      |
| 2020-08-22 |   11    |     8      |
| 2020-08-19 |   12    |     6      |
| 2020-08-15 |   13    |     3      |
| 2020-08-21 |   14    |     0      |
*/

SELECT date,
    non_paying,
    paying
FROM (
        SELECT date,
            sum(
                CASE
                    WHEN paying_customer = 'yes' THEN downloads
                END
            ) AS paying,
            sum(
                CASE
                    WHEN paying_customer = 'no' THEN downloads
                END
            ) AS non_paying
        FROM ms_user_dimension a
            JOIN ms_acc_dimension b ON a.acc_id = b.acc_id
            JOIN ms_download_facts c ON a.user_id = c.user_id
        GROUP BY date
        ORDER BY date
    ) t
WHERE (non_paying - paying) > 0
ORDER BY t.date