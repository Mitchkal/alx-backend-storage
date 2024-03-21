-- create meeting as needed

CREATE VIEW need_meeting AS
SELECT 
    users.name
FROM 
    users
LEFT JOIN 
    (
        SELECT 
            user_id, 
            MAX(meeting_date) AS last_meeting
        FROM 
            meetings
        GROUP BY 
            user_id
    ) AS last_meeting_dates
ON 
    users.id = last_meeting_dates.user_id
LEFT JOIN 
    (
        SELECT 
            user_id, 
            MAX(score_date) AS last_score
        FROM 
            scores
        GROUP BY 
            user_id
    ) AS last_score_dates
ON 
    users.id = last_score_dates.user_id
LEFT JOIN 
    (
        SELECT 
            user_id, 
            AVG(score) AS avg_score
        FROM 
            scores
        GROUP BY 
            user_id
    ) AS avg_scores
ON 
    users.id = avg_scores.user_id
WHERE 
    (avg_scores.avg_score < 80 OR avg_scores.avg_score IS NULL)
    AND (last_meeting_dates.last_meeting IS NULL OR last_meeting_dates.last_meeting < DATE_SUB(NOW(), INTERVAL 1 MONTH));

