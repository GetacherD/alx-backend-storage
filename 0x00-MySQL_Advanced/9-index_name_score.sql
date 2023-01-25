-- Create Index on first letter of column
CREATE INDEX idx_name_first_score ON names(name(1), score(1));
