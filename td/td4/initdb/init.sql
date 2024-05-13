-- Create a sample table
CREATE TABLE IF NOT EXISTS sample_table (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

-- Insert some data into the sample table
INSERT INTO sample_table (name) VALUES
    ('John Doe'),
    ('Jane Doe'),
    ('Jane Doe'),
    ('Bob Smith');