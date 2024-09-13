CREATE TABLE usuarios (
    usuario_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    fecha_registro DATE NOT NULL
);

CREATE TABLE tests (
    test_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    fecha_creacion DATE NOT NULL
);

CREATE TABLE preguntas (
    pregunta_id INT AUTO_INCREMENT PRIMARY KEY,
    test_id INT NOT NULL,
    texto_pregunta TEXT NOT NULL,
    FOREIGN KEY (test_id) REFERENCES tests(test_id) ON DELETE CASCADE
);

CREATE TABLE respuestas (
    respuesta_id INT AUTO_INCREMENT PRIMARY KEY,
    pregunta_id INT NOT NULL,
    texto_respuesta TEXT NOT NULL,
    valor INT NOT NULL,
    FOREIGN KEY (pregunta_id) REFERENCES preguntas(pregunta_id) ON DELETE CASCADE
);

CREATE TABLE resultados (
    resultado_id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    test_id INT NOT NULL,
    fecha_realizacion DATE NOT NULL,
    puntaje INT NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(usuario_id) ON DELETE CASCADE,
    FOREIGN KEY (test_id) REFERENCES tests(test_id) ON DELETE CASCADE
);


INSERT INTO tests (nombre, descripcion, fecha_creacion) VALUES
('Estrés', 'Test para evaluar el nivel de estrés', CURDATE()),
('Ansiedad', 'Test para evaluar el nivel de ansiedad', CURDATE()),
('Autoestima', 'Test para evaluar el nivel de autoestima', CURDATE());


INSERT INTO preguntas (test_id, texto_pregunta) VALUES
(1, '¿Con qué frecuencia te sientes estresado/a durante la semana?'),
(1, '¿Cuáles son las principales fuentes de estrés en tu vida actualmente?'),
(1, '¿Has presentado síntomas físicos por el estrés?'),
(1, '¿Sientes que tu rendimiento en el trabajo o en los estudios disminuye cuando estás estresado/a?'),
(1, '¿Te sientes irritable o emocionalmente inestable cuando estás bajo presión?');


INSERT INTO respuestas (pregunta_id, texto_respuesta, valor) VALUES
(1, 'Nunca', 0),
(1, 'Ocasionalmente', 1),
(1, 'Frecuentemente', 2),
(1, 'Constantemente', 3),
(2, 'Problemas personales', 1),
(2, 'Trabajo o estudios', 2),
(2, 'Problemas económicos', 3),
(2, 'Otros (especificar)', 4),
(3, 'Nunca', 0),
(3, 'Rara vez', 1),
(3, 'A veces', 2),
(3, 'Frecuentemente', 3),
(4, 'Nunca', 0),
(4, 'A veces', 1),
(4, 'Frecuentemente', 2),
(4, 'Siempre', 3),
(5, 'Nunca', 0),
(5, 'Raramente', 1),
(5, 'A veces', 2),
(5, 'Frecuentemente', 3);

INSERT INTO preguntas (test_id, texto_pregunta) VALUES
(2, '¿Con qué frecuencia sientes ansiedad en tu vida diaria?'),
(2, '¿Te resulta difícil relajarte en situaciones de estrés?'),
(2, '¿Sientes una preocupación constante por cosas que no puedes controlar?'),
(2, '¿Has experimentado ataques de pánico o momentos de intensa ansiedad?'),
(2, '¿Tienes problemas para conciliar el sueño debido a la ansiedad?');

INSERT INTO respuestas (pregunta_id, texto_respuesta, valor) VALUES
(6, 'Nunca', 1),
(6, 'Ocasionalmente', 2),
(6, 'Frecuentemente', 3),
(6, 'Constantemente', 4),
(7, 'No, puedo relajarme fácilmente', 1),
(7, 'A veces me cuesta un poco relajarme', 2),
(7, 'Me cuesta bastante relajarme', 3),
(7, 'No puedo relajarme en absoluto', 4),
(8, 'No, no me preocupo mucho', 1),
(8, 'Solo a veces', 2),
(8, 'Me preocupo bastante', 3),
(8, 'Siempre estoy preocupado/a', 4),
(9, 'Nunca', 1),
(9, 'En raras ocasiones', 2),
(9, 'Algunas veces', 3),
(9, 'Frecuentemente', 4),
(10, 'No, duermo bien', 1),
(10, 'Tengo ligeros problemas para dormir', 2),
(10, 'Me cuesta bastante dormir', 3),
(10, 'No puedo dormir por la ansiedad', 4);

INSERT INTO preguntas (test_id, texto_pregunta) VALUES
(3, '¿Con qué frecuencia te sientes satisfecho/a con quién eres?'),
(3, '¿Te sientes seguro/a al tomar decisiones importantes?'),
(3, '¿Sientes que mereces amor y respeto?'),
(3, '¿Sueles compararte negativamente con los demás?'),
(3, '¿Te sientes capaz de superar los desafíos que enfrentas?');

INSERT INTO respuestas (pregunta_id, texto_respuesta, valor) VALUES
(11, 'Siempre', 1),
(11, 'Casi siempre', 2),
(11, 'A veces', 3),
(11, 'Raramente', 4),
(12, 'Muy seguro/a', 1),
(12, 'Algo seguro/a', 2),
(12, 'Inseguro/a', 3),
(12, 'Muy inseguro/a', 4),
(13, 'Siempre', 1),
(13, 'Casi siempre', 2),
(13, 'A veces', 3),
(13, 'Raramente', 4),
(14, 'Nunca', 1),
(14, 'Raramente', 2),
(14, 'A veces', 3),
(14, 'Frecuentemente', 4),
(15, 'Siempre', 1),
(15, 'Casi siempre', 2),
(15, 'A veces', 3),
(15, 'Raramente', 4);



