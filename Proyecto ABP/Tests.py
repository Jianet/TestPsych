import mysql.connector
import datetime
import random

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password='',
    database="testpsycho"
)

cursor = db.cursor()

print("\t\t¡Bienvenido a TestPsycho!"
      "\t\nExplora tu bienestar emocional con nuestros tests.")


def registrar_usuario():
    nombre = input("Ingresa tu nombre: ")
    email = input("Ingresa tu email: ")
    fecha_registro = datetime.date.today()

    query = "INSERT INTO usuarios (nombre, email, fecha_registro) VALUES (%s, %s, %s)"
    values = (nombre, email, fecha_registro)
    cursor.execute(query, values)
    db.commit()

    print(f"¡Usuario {nombre} registrado con éxito!\n")
    return cursor.lastrowid


def realizar_test(test_id, usuario_id):
    if test_id == 1:
        print("\n--- Test del Estrés ---")
        preguntas = [
            ("¿Con qué frecuencia te sientes estresado/a durante la semana?", ["Nunca", "Ocasionalmente", "Frecuentemente", "Constantemente"]),
            ("¿Cuáles son las principales fuentes de estrés en tu vida actualmente?", ["Problemas personales", "Trabajo o estudios", "Problemas económicos", "Otros (especificar)"]),
            ("¿Has presentado síntomas físicos por el estrés?", ["Nunca", "Rara vez", "A veces", "Frecuentemente"]),
            ("¿Sientes que tu rendimiento en el trabajo o en los estudios disminuye cuando estás estresado/a?", ["Nunca", "A veces", "Frecuentemente", "Siempre"]),
            ("¿Te sientes irritable o emocionalmente inestable cuando estás bajo presión?", ["Nunca", "Raramente", "A veces", "Frecuentemente"])
        ]
        respuestas = [1, 2, 3, 4]

    elif test_id == 2:
        print("\n--- Test de la Ansiedad ---")
        preguntas = [
            ("¿Con qué frecuencia te sientes preocupado por cosas cotidianas?", ["Nunca", "Rara vez", "A veces", "Con frecuencia", "Siempre"]),
            ("¿Tienes problemas para dormir debido a pensamientos preocupantes?", ["Nunca", "Rara vez", "A veces", "Con frecuencia", "Siempre"]),
            ("¿Te sientes abrumado o incapaz de manejar las cosas que te preocupan?", ["Nunca", "Rara vez", "A veces", "Con frecuencia", "Siempre"]),
            ("¿Te resulta difícil concentrarte debido a pensamientos negativos o ansiosos?", ["Nunca", "Rara vez", "A veces", "Con frecuencia", "Siempre"]),
            ("¿Cómo te sientes cuando te enfrentas a una situación nueva o desconocida?", ["Tranquilo/a", "Un poco nervioso/a", "Moderadamente ansioso/a", "Muy ansioso/a", "Extremadamente ansioso/a"])
        ]
        respuestas = [1, 2, 3, 4]

    elif test_id == 3:
        print("\n--- Test de la Autoestima ---")
        preguntas = [
            ("¿Cuál es tu comportamiento frente a grandes grupos sociales?", ["Me siento ansioso/a y pienso que no formo parte de ellos.", "Sobrepienso sus comportamientos hacia mí.", "Aumenta mi interés social, siento seguridad y comodidad."]),
            ("¿Cómo reaccionas ante circunstancias difíciles y adversas?", ["Estoy lleno/a de ira y frustración.", "Me muestro optimista y busco soluciones.", "Tengo pensamientos negativos y falta de esperanza."]),
            ("¿Cómo enfrentas los fracasos?", ["Busco mejorar día a día.", "Me cuesta hacerlo, creo que soy mediocre y me culpo constantemente.", "Me siento triste y decepcionado/a."]),
            ("¿Sientes que tu valor proviene de las opiniones ajenas?", ["Me afectan significativamente, pero intento no dejarme llevar.", "Sí, siempre trato de encajar para no caer en el rechazo.", "Estoy seguro/a de mi valor y la percepción ajena no interviene en mis capacidades."]),
            ("¿Estableces límites respecto a los intereses ajenos?", ["No, siempre complazco los intereses de los demás dejando de lado los propios.", "Tengo carácter y personalidad para no tener que satisfacer a otros.", "Trato de agradar para ser gratificado/a y obtener aprobación."])
        ]
        respuestas = [1, 2, 3, 4]

    else:
        print("Test no válido.")
        return

    puntaje_total = 0

    for i, pregunta in enumerate(preguntas):
        print(f"\n{pregunta[0]}")
        for j, opcion in enumerate(pregunta[1]):
            print(f"{j + 1}. {opcion}")

        while True:
            try:
                eleccion = int(input("Selecciona una opción (1-4): ")) - 1
                if eleccion < 0 or eleccion >= len(pregunta[1]):
                    raise IndexError
                break
            except (ValueError, IndexError):
                print("Opción no válida. Por favor, selecciona una opción correcta.")

        puntaje_total += respuestas[eleccion]

    fecha_realizacion = datetime.date.today()
    query_resultado = "INSERT INTO resultados (usuario_id, test_id, fecha_realizacion, puntaje) VALUES (%s, %s, %s, %s)"
    values = (usuario_id, test_id, fecha_realizacion, puntaje_total)
    cursor.execute(query_resultado, values)
    db.commit()

    deduccion_test(test_id, puntaje_total)

# Función para calcular la deducción del test
def deduccion_test(test_id, puntaje):
    if test_id == 1:
        if puntaje <= 20:
            print("Bajo estrés (0-20%): Estás manejando bien el estrés. ¡Ánimos!")
        elif puntaje <= 60:
            print("Estrés moderado (21-60%): Presentas un nivel de estrés moderado. Intenta relajarte.")
        else:
            print("Alto estrés (61-100%): Tu nivel de estrés es alto. Considera buscar ayuda profesional.")
    elif test_id == 2:
        if puntaje <= 20:
            print("Baja ansiedad (0-20%): No tienes problemas significativos de ansiedad.")
        elif puntaje <= 60:
            print("Ansiedad moderada (21-60%): Experimentas ansiedad moderada.")
        else:
            print("Alta ansiedad (61-100%): Busca apoyo profesional.")
    elif test_id == 3:
        if puntaje <= 20:
            print("Baja autoestima (0-20%): Tienes baja autoestima. Trabaja en tu autoaceptación.")
        elif puntaje <= 60:
            print("Autoestima moderada (21-60%): Tu autoestima es moderada.")
        else:
            print("Alta autoestima (61-100%): Tienes una buena percepción de ti mismo.")

# Función para realizar todos los tests
def realizar_todos_los_tests(usuario_id):
    puntajes = []
    for test_id in [1, 2, 3]:
        realizar_test(test_id, usuario_id)
        query = "SELECT puntaje FROM resultados WHERE usuario_id = %s AND test_id = %s"
        cursor.execute(query, (usuario_id, test_id))
        puntajes.append(cursor.fetchone()[0])

    puntaje_total = sum(puntajes) // 3

    print("\nDeducción general de los tres tests:")
    if puntaje_total <= 20:
        print("Estás en buena forma psicológica. Sigue cuidándote.")
    elif puntaje_total <= 60:
        print("Tu nivel de estrés, ansiedad y autoestima es moderado. Toma medidas para mejorar.")
    else:
        print("Necesitas atención urgente. Considera buscar ayuda profesional.")

# Menú principal
def menu_principal():
    usuario_id = registrar_usuario()
    print("¿Quieres realizar un solo test o los tres?\n1. Un solo test\n2. Todos los tests")
    eleccion = int(input("Selecciona una opción: "))

    if eleccion == 1:
        print("¿Qué test quieres realizar?\n1. Estrés\n2. Ansiedad\n3. Autoestima\n4. Test aleatorio")
        test_eleccion = int(input("Selecciona una opción: "))
        if test_eleccion == 4:
            test_eleccion = random.choice([1, 2, 3])
        realizar_test(test_eleccion, usuario_id)
    elif eleccion == 2:
        realizar_todos_los_tests(usuario_id)

if __name__ == "__main__":
    menu_principal()
    cursor.close()
    db.close()






