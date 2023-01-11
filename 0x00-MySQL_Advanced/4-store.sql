-- create trigger
DELIMITER ~
CREATE TRIGGER dec_quant AFTER INSERT ON orders
FOR EACH ROW
BEGIN
UPDATE items SET quantity = quantity - NEW.number
where items.name = NEW.item_name; 
END~
