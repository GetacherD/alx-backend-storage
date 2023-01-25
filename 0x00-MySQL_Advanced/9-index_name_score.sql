-- Create Index on first letter of column
CREATE INDEX idx_name_first_score ON names(name, score);
