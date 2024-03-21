-- Compute average weighted score and Store the average weighted score
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
    DECLARE done BOOLEAN DEFAULT FALSE;
    DECLARE user_id INT;
    DECLARE avg_weighted_score DECIMAL(10,2);

    -- Cursor to iterate over all users
    DECLARE user_cursor CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    -- Open the cursor
    OPEN user_cursor;

    -- Loop through all
    user_loop: LOOP
        FETCH user_cursor INTO user_id;
        IF done THEN
            LEAVE user_loop;
        END IF;

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
    END LOOP;

    -- Close cursor
    CLOSE user_cursor;

END//

DELIMITER ;
