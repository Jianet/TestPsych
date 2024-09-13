## Proyecto del ABP 
Desarrollo de una aplicación en Phyton 

## Título del proyecto 
Aplicación en Python, que automatiza un contexto especifico con acceso a datos 

## Descripción  
Este proyecto tiene como objetivo desarrollar una aplicación en Pythton que automatice un contexto específico con acceso a datos, se debe realizar un análisis detallado de los requerimientos del proyecto; además debe identificar las necesidades específicas del sistema, incluyendo el tipo de datos que se manejarán, la lógica de negocio y las funcionalidades esperadas, determina las abstracciones de los modelos a utilizar, desde la base de datos hasta la forma de cómo se aplicaría el paradigma de programación para el proyecto propuesto. 

## ESTRUCTURA DEL PROYECTO  

## TestPsych
En un mundo donde el bienestar emocional se ha vuelto una prioridad, TestPsych es una herramienta diseñada para ayudar a las personas a comprender y reflexionar sobre su estado emocional y psicológico. A través de una serie de tests personalizados, esta aplicación brinda recomendaciones prácticas que permiten a los usuarios mejorar su salud mental, proporcionando un apoyo accesible y comprensible.

## Contexto
Con el aumento de casos de estrés, ansiedad y problemas de autoestima en la sociedad moderna, muchas personas carecen de acceso a recursos que les ayuden a comprender su bienestar emocional. TestPsych aborda este problema proporcionando una herramienta accesible que permite a los usuarios evaluar su estado mental y recibir recomendaciones personalizadas para mejorar su salud emocional.

## Modelo relacional
![ModeloTest](https://github.com/user-attachments/assets/466fcc37-cd63-425a-8343-e6fac4af4869)



## Análisis de Requerimientos

Requerimientos Funcionales:
- Registro de usuarios: El sistema permitirá registrar a los usuarios ingresando sus datos personales (nombre, email) para que puedan acceder a los tests y recibir sus resultados personalizados.
- Tests psicológicos: La aplicación ofrecerá tres tests principales enfocados en:
Estrés
Ansiedad
Autoestima
- Preguntas y respuestas: Cada test constará de una serie de preguntas con respuestas múltiples, cada una asignada con un puntaje que será utilizado para la evaluación final.
- Evaluación y deducción: Al finalizar el test, el usuario recibirá una evaluación en función de su puntaje total. La evaluación incluirá:
- Mensajes personalizados según el nivel de estrés, ansiedad o autoestima detectado.
- Recomendaciones para mejorar su estado emocional.
- Resultados almacenados: El sistema permitirá almacenar los resultados en una base de datos para que los usuarios puedan revisar su progreso o realizar nuevos tests en el futuro.

Requerimientos No Funcionales:
- Usabilidad: La aplicación debe ser intuitiva y fácil de navegar, especialmente para usuarios sin conocimientos técnicos.
- Accesibilidad: Debe funcionar en diversas plataformas (PC, móvil) y ser accesible para personas con diferentes niveles de habilidades tecnológicas.
- Privacidad: Los datos del usuario (nombre, email, resultados) deben ser tratados de forma confidencial, respetando su privacidad.


## Test que se encontrarán en nuestra aplicación con sus respectivas preguntas y respuestas.
### Test del estrés
1. ¿Con qué frecuencia te sientes estresado/a durante la semana?   
a) Nunca  
b) Ocasionalmente  
c) Frecuentemente  
d) Constantemente  

2. ¿Cuáles son las principales fuentes de estrés en tu vida actualmente?  
a) Problemas personales  
b) Trabajo o estudios  
c) Problemas económicos  
d) Otros (especificar)

3. ¿Has presentado síntomas físicos por el estrés?  
a) Nunca  
b) Rara vez  
c) A veces  
d) Frecuentemente

4. ¿Sientes que tu rendimiento en el trabajo o en los estudios disminuye cuando estás estresado/a?  
a) Nunca  
b) A veces  
c) Frecuentemente  
d) Siempre

5. ¿Te sientes irritable o emocionalmente inestable cuando estás bajo presión?  
a) Nunca  
b) Raramente  
c) A veces  
d) Frecuentemente 
#### Deducción
- Bajo estrés (0-20%) Nunca/Raramente: Estás manejando bien el estrés. ¡Ánimos!

- Estrés moderado (21-60%) A veces/Ocasionalmente: Presentas un nivel de estrés moderado. Intenta hacer actividades que te relajen y ten un tiempo de descanso.

- Alto estrés (61-100%) Frecuente/Constante: Tu nivel de estrés es preocupantemente alto. Te recomendamos buscar ayuda profesional y cambiar tu rutina diaria.

### Test de la ansiedad 
1. ¿Con qué frecuencia te sientes preocupado por cosas cotidianas?  
a) Nunca  
b) Rara vez  
c) A veces  
d) Con frecuencia  
e) Siempre  

2. ¿Tienes problemas para dormir debido a pensamientos preocupantes?  
a) Nunca  
b) Rara vez  
c) A veces  
d) Con frecuencia  
e) Siempre  

3. ¿Te sientes abrumado o incapaz de manejar las cosas que te preocupan?  
a) Nunca  
b) Rara vez   
c) A veces  
d) Con frecuencia  
e) Siempre  

4. ¿Te resulta difícil concentrarte debido a pensamientos negativos o ansiosos?  
a) Nunca  
b) Rara vez  
c) A veces  
d) Con frecuencia  
e) Siempre  

5. ¿Cómo te sientes cuando te enfrentas a una situación nueva o desconocida?  
a) Tranquilo/a  
b) Un poco nervioso/a  
c) Moderadamente ansioso/a  
d) Muy ansioso/a  
e) Extremadamente ansioso/a  
#### Deducción
- Baja ansiedad (0-20%) Nunca/Rara vez: No tienes problemas significativos de ansiedad. Mantén tus hábitos saludables.

- Ansiedad moderada (21-60%) A veces/Con frecuencia: Experimentas ansiedad moderada. Procura hacer ejercicios de meditación y otras tecnicas para manejo de ansiedad.

- Alta ansiedad (61-100%) Siempre/Con frecuencia: Tu ansiedad es alta y podría afectar tu vida diaria. Busca apoyo profesional y establece una rutina calmante.
  
### Test de la autoestima  
1. ¿Cuál es tu comportamiento frente a grandes grupos sociales?  
a) Me siento ansioso/a y pienso que no formo parte de ellos.  
b) Sobrepienso sus comportamientos hacia mí.  
c) Aumenta mi interés social, siento seguridad y comodidad.  

2. ¿Cómo reaccionas ante circunstancias difíciles y adversas?  
a) Estoy lleno/a de ira y frustración.  
b) Me muestro optimista y busco soluciones.  
c) Tengo pensamientos negativos y falta de esperanza.  

3. ¿Cómo enfrentas los fracasos?  
a) Busco mejorar día a día.  
b) Me cuesta hacerlo, creo que soy mediocre y me culpo constantemente.  
c) Me siento triste y decepcionado/a.  

4. ¿Sientes que tu valor proviene de las opiniones ajenas?   
a) Me afectan significativamente, pero intento no dejarme llevar.   
b) Sí, siempre trato de encajar para no caer en el rechazo.   
c) EStoy seguro/a de mi valor y la percepción ajena no interviene en mis capacidades.  

5. ¿Estableces límites respecto a los intereses ajenos?  
a) No, siempre complazco los intereses de los demás dejando de lado los propios.   
b) Tengo carácter y personalidad para no tener que satisfacer a otros.   
c) Trato de agradar para ser gratificado/a y obtener aprobación.  
#### Deducción 
- Baja autoestima (0-20%) Me siento ansioso/Me afecta: Tu autoestima es baja. Es importante buscar apoyo y trabajar en la autoaceptación de tu persona.
 
- Autoestima moderada (21-60%) Inseguridad ocasional: Tu autoestima es moderada. Trabaja en fortalecerla desafiando pensamientos negativos. Sé que puedes.
 
- Alta autoestima (61-100%) Seguridad y percepción positiva: Tienes una buena percepción de ti mismo. Estoy orgullosa de ti.
