-- safe divide that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.

CREATE FUNCTION SafeDiv (
    a INT,
    b INT
)
RETURNS INT
BEGIN
    DECLARE result INT;
    
    IF b <> 0 THEN
        SET result = a / b;
    ELSE
        SET result = 0;
    END IF;
    
    RETURN result;
END;
