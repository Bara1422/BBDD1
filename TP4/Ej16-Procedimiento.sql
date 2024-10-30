DELIMITER //

CREATE PROCEDURE ConsolidarFeedback()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE ClienteId_var INT;
    DECLARE ComentariosTotales_var INT;
    DECLARE CalificacionPromedio_var DECIMAL(3,2);

    DECLARE cursor_feedback CURSOR FOR 
    SELECT ClienteId, COUNT(*) AS TotalComentarios, AVG(Calificacion) AS CalificacionPromedio FROM FeedbackClientes
    GROUP BY ClienteId;
    
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN cursor_feedback;
    FETCH cursor_feedback INTO ClienteId_var, ComentariosTotales_var, CalificacionPromedio_var;

    WHILE NOT done DO
        IF NOT EXISTS (SELECT * FROM ResumenFeedback WHERE ClienteId = ClienteId_var) THEN
            INSERT INTO ResumenFeedback (ClienteId, ComentariosTotales, CalificacionPromedio, FechaResumen)
            VALUES (ClienteId_var, ComentariosTotales_var, CalificacionPromedio_var, CURDATE());
        ELSE
			SET SQL_SAFE_UPDATES = 0;
            UPDATE ResumenFeedback
            SET 
				ComentariosTotales = ComentariosTotales_var,
				CalificacionPromedio = CalificacionPromedio_var,
				FechaResumen = CURDATE()
            WHERE ClienteId = ClienteId_var;
            SET SQL_SAFE_UPDATES = 1;
        END IF;
        FETCH cursor_feedback INTO ClienteId_var, ComentariosTotales_var, CalificacionPromedio_var;
    END WHILE;
    
    CLOSE cursor_feedback;
    
END//
DELIMITER ;