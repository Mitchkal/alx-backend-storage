-- Compute average weighted score and Store the average weighted score for the user
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser (
    IN user_id INT
)
BEGIN
    DECLARE avg_weighted_score DECIMAL(10,2);

    -- Compute average weighted score
    SELECT AVG(weighted_score) INTO avg_weighted_score 
    FROM (
        SELECT user_id, SUM(score * weight) / SUM(weight) AS weighted_score
        FROM scores
        WHERE user_id = user_id
        GROUP BY user_id
    ) AS user_weighted_scores;

    -- Store the average weighted score
    UPDATE users SET average_weighted_score = avg_weighted_score WHERE id = user_id;


END//

DELIMITER ;

