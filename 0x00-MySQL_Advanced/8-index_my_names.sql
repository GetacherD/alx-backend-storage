-- Create Index on first letter of column
CREATE INDEX idx_name_first ON names(name(1));
