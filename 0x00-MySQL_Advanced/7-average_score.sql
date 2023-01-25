-- Calculate average score using stored procedure
DELIMITER ~
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
DECLARE avgScore FLOAT;
SET avgScore = (SELECT AVG(score) FROM users LEFT JOIN corrections ON users.id = corrections.user_id LEFT JOIN projects ON projects.id=corrections.project_id GROUP BY users.id having users.id = user_id);
UPDATE users set average_score=avgScore where id=user_id;
END~
DELIMITER ;
