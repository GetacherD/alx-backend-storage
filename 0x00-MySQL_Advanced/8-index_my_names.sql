-- Create Index on first letter of column
ALTER TABLE names ADD INDEX idx_name_first name(1);
