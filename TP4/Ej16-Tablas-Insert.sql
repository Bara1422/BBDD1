DROP TABLE IF EXISTS feedbackclientes;
DROP TABLE IF EXISTS resumenfeedback;

CREATE TABLE FeedbackClientes (
    FeedbackId INT PRIMARY KEY AUTO_INCREMENT,
    ClienteId INT NOT NULL,
    Comentario VARCHAR(500) NOT NULL,
    Calificacion INT NOT NULL, -- 1 a 5
    FechaFeedback DATE NOT NULL
);

CREATE TABLE ResumenFeedback (
    ResumenId INT PRIMARY KEY AUTO_INCREMENT,
    ClienteId INT NOT NULL,
    ComentariosTotales INT NOT NULL,
    CalificacionPromedio DECIMAL(3,2) NOT NULL,
    FechaResumen DATE NOT NULL
);

INSERT INTO FeedbackClientes (ClienteId, Comentario, Calificacion, FechaFeedback)
VALUES 
    (1, 'Excelente servicio, muy satisfecho con la atención.', 5, '2024-09-01'),
    (1, 'El producto no cumplió con mis expectativas.', 2, '2024-09-15'),
    (2, 'Entrega rápida, producto en buen estado.', 4, '2024-09-10'),
    (2, 'Volveré a comprar, muy buena experiencia.', 5, '2024-09-20'),
    (3, 'Tardaron mucho en responder mis consultas.', 3, '2024-09-05'),
    (4, 'Todo perfecto, sin inconvenientes.', 5, '2024-09-18'),
    (4, 'Un poco caro, pero buena calidad.', 4, '2024-09-25'),
    (5, 'No recomendaría el producto, muy frágil.', 1, '2024-09-12'),
    (5, 'No recibí lo que esperaba.', 2, '2024-09-28');

###### COMENTADO PARA QUE SE GENERE AUTOMATICAMENTE ############
#INSERT INTO ResumenFeedback (ClienteId, ComentariosTotales, CalificacionPromedio, FechaResumen)
#VALUES
#    (1, 2, 3.50, '2024-09-30'),
#    (2, 2, 4.50, '2024-09-30'),
#    (3, 1, 3.00, '2024-09-30'),
#    (4, 2, 4.50, '2024-09-30'),
#    (5, 2, 1.50, '2024-09-30');

######### USAR DESPUES DE CREAR EL PROCEDIMIENTO PARA ACTUALIZAR LOS DATOS ###########
#CALL ConsolidarFeedback();
#SELECT * FROM resumenfeedback;

##### INGRESO DE NUEVO DATO #####
#INSERT INTO FeedbackClientes (ClienteId, Comentario, Calificacion, FechaFeedback)
#VALUES 
#    (1, 'Muy buena atención al cliente.', 4, '2024-10-01');

#### EJECUTAR EL PROCEDIMIENTO PARA ACTUALIZAR LOS DATOS YA GENERADOS
#CALL ConsolidarFeedback();
#SELECT * FROM resumenfeedback;

