with confirmed_cte AS 
(
    SELECT 
        a1.user_id 
        ,COUNT(action) confirmed_request
    FROM Signups a1
    LEFT OUTER JOIN Confirmations  a2
        ON a1.user_id = a2.user_id
    WHERE action='confirmed'
    GROUP BY a1.user_id
)
,total_request_cte AS 
(
    SELECT 
        a1.user_id 
        ,COUNT(action) total_request
    FROM Signups a1
    LEFT OUTER JOIN Confirmations  a2
        ON a1.user_id = a2.user_id
    GROUP BY a1.user_id
)
SELECT c1.user_id, CAST(COALESCE(SUM(c2.confirmed_request)*1.0/SUM(c1.total_request),0) AS DECIMAL(11,2)) confirmation_rate 
FROM  total_request_cte c1
FULL OUTER JOIN confirmed_cte c2
    ON c1.user_id = c2.user_id
GROUP BY c1.user_id
