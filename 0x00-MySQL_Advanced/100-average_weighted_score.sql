-- compute average weighted score
DELIMITER ~
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	DECLARE u_id INT;
	DECLARE offset INT;
	DECLARE avgSC FLOAT;
	SET u_id = (SELECT id FROM users ORDER BY id ASC LIMIT 1);
	WHILE u_id IS NOT NULL DO
		
		SET avgSC = (SELECT SUM(score * weight) / SUM(weight)
		    FROM users
		    JOIN corrections ON users.id = corrections.user_id
		    JOIN projects ON projects.id=corrections.project_id
		    GROUP BY users.id
		    HAVING users.id = u_id);
		UPDATE users SET average_score=avgSc WHERE id=u_id;
		SET offset = u_id;
		SET u_id = (SELECT id FROM users
		    ORDER BY id ASC LIMIT 1 OFFSET offset);
	END WHILE;
END~
DELIMITER ;
