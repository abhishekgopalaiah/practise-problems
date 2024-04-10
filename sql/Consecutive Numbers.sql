/*
Find all numbers that appear at least three times consecutively.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Logs table:
+----+-----+
| id | num |
+----+-----+
| 1  | 1   |
| 2  | 1   |
| 3  | 1   |
| 4  | 2   |
| 5  | 1   |
| 6  | 2   |
| 7  | 2   |
+----+-----+
Output: 
+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+
Explanation: 1 is the only number that appears consecutively for at least three times.
*/
WITH ctes AS (
select num,id 
, lead(id, 1) OVER (partition by num order by id) snd_nbr
, lead(id, 2) OVER (partition by num order by id) trd_nbr
from logs)
, cte2 as (SELECT num, ABS(id - snd_nbr) dif1,ABS(snd_nbr-trd_nbr) dif2
, ABS(id-trd_nbr) dif3
FROM ctes)
SELECT DISTINCT num AS ConsecutiveNums 
FROM cte2
WHERE dif1=1 AND dif2=1 AND dif3=2
