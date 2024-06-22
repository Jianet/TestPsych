# TestPsych
Escribir contexto de su solucion
Nuestra app se trata de una herramienta diseñada para explorar y comprender tu bienestar emocional y psicológico. Este test te ayudará a reflexionar sobre tus emociones, pensamientos y comportamientos,
proporcionándote una guía personalizada para mejorar tu bienestar emocional.
## Modelo relacional
Modelo

[Up
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

/*usuarios (usuario_id, nombre, email, fecha_registro)
tests (test_id, nombre, descripcion, fecha_creacion)
preguntas (pregunta_id, test_id, texto_pregunta)
respuestas (respuesta_id, pregunta_id, texto_respuesta, valor)
resultados (resultado_id, usuario_id, test_id, fecha_realizacion, puntaje)*/
loading TestPysho.sql…]()

## Desarrollo de propuesta
Escribir sobre la solución realizar
Recomendaciones personalizadas para el bienestar
En TestPsych, nos enfocamos en ofrecer recomendaciones personalizadas basadas en los resultados del test psicológicos. Estas recomendaciones están diseñadas con el fin de ayudar a los usuarios a mejorar
su bienestar emocional y psicológico de manera práctica y comprensible.

