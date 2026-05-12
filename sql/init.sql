CREATE TABLE test_connection (

    id SERIAL PRIMARY KEY,
    message VARCHAR(100)

);

INSERT INTO test_connection (message)
VALUES ('PostgreSQL running successfully');