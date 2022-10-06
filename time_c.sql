DROP DATABASE test;
CREATE DATABASE test;
USE test;

CREATE TABLE Intervals(
	DateTime_id INT PRIMARY KEY AUTO_INCREMENT,
    StartDateTime TIMESTAMP, 
    EndDateTime TIMESTAMP
);

INSERT INTO Intervals(StartDateTime, EndDateTime)
VALUES ('2018-01-01 06:00:00','2018-01-01 14:00:00'),
	('2018-01-01 11:00:00','2018-01-01 19:00:00'),
	('2018-01-01 20:00:00','2018-01-02 03:00:00'),
	('2018-01-02 06:00:00','2018-01-02 14:00:00'),
	('2018-01-02 11:00:00','2018-01-02 19:00:00');

SELECT * FROM Intervals;

DROP PROCEDURE IF EXISTS sp_foo;

delimiter $$
CREATE PROCEDURE sp_foo()
BEGIN
	DECLARE n INT DEFAULT 0;
	DECLARE i INT DEFAULT 0;
    DECLARE start_t TIMESTAMP;
    DECLARE end_t TIMESTAMP;
    DECLARE r TIMESTAMP;
    DECLARE l TIMESTAMP;
    
    DROP TABLE IF EXISTS temp_intervals;
    CREATE TEMPORARY TABLE temp_intervals LIKE Intervals;
    
	SELECT count(*)
    FROM Intervals INTO n;
    
    SELECT StartDateTime, EndDateTime FROM Intervals LIMIT 0, 1 INTO l, r;
    SET start_t = l;
    SET end_t = r;
    
    WHILE i  < n DO
    SET i = i + 1;
    SELECT StartDateTime, EndDateTime FROM Intervals LIMIT i, 1 INTO l, r;
    IF end_t > l THEN
		SET end_t = r;
        IF i = n THEN
        
        INSERT INTO temp_intervals(StartDateTime, EndDateTime)
        VALUES (start_t, end_t);
        END IF;
	ELSE
        INSERT INTO temp_intervals(StartDateTime, EndDateTime)
        VALUES (start_t, end_t);
		SET start_t = l;
		SET end_t = r;
	
	END IF;
    END WHILE;
    
SELECT * FROM temp_intervals;
DROP TABLE temp_intervals;

END$$
delimiter ;

CALL sp_foo();

