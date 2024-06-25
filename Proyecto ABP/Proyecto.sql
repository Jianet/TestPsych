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
