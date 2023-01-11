-- trigger for reset when email changed
DELIMITER ~
CREATE TRIGGER email_changed BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
if OLD.email != NEW.email THEN
IF NEW.id=OLD.id THEN
SET NEW.valid_email = 1;
END IF;
END IF;
END~
