-- compute average weighted score
DELIMITER ~
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
	DECLARE avgSC FLOAT;
	SET avgSC = (SELECT SUM(score * weight) / SUM(weight)
	    FROM users
	    JOIN corrections ON users.id = corrections.user_id
	    JOIN projects ON projects.id=corrections.project_id
	    GROUP BY users.id
	    HAVING users.id = user_id);
	UPDATE users SET average_score=avgSC WHERE id=user_id;
END~
DELIMITER ;
