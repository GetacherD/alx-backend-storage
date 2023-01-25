-- create stored procedure AddBonus
DELIMITER ~
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
	DECLARE pr_id VARCHAR(255);
	SET pr_id = (SELECT id FROM projects where name=project_name);
	IF pr_id is NULL THEN
		INSERT INTO projects (name) values(project_name);
		SET pr_id = LAST_INSERT_ID();
	END IF;
	insert into corrections (user_id, project_id, score) values
	(user_id, pr_id, score);
END~
