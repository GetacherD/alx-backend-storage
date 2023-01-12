-- Create View Demo

CREATE VIEW need_meeting AS
SELECT name FROM students WHERE
score < 80 AND (last_meeting is NULL OR IF(DATE_SUB(NOW(), INTERVAL 1 MONTH) > last_meeting, TRUE, FALSE));
