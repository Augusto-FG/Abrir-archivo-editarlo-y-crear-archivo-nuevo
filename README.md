# Abrir-archivo-editarlo-y-crear-archivo-nuevo

La Facultad de Ingeniería dispone de un archivo de texto donde cada línea contiene:
· Un número entero, correspondiente al número de legajo del alumno.
· El apellido y nombre del alumno.
· El nombre de la carrera en la que se halla inscripto: Alimentos, Electromecanica,
Electronica, Industrial, Informatica o Telecomunicaciones.
· Un conjunto de números enteros correspondientes a las calificaciones obtenidas por
ese alumno (de 0 a 10). La cantidad de calificaciones varía según el alumno, ya que
dependen de los exámenes y recuperatorios rendidos y de los trabajos prácticos
presentados.
Todos estos datos se encuentran separados por un punto y coma, formando lo que se denomina
un archivo CSV (comma separated values). En estos archivos cada línea contiene
una serie de campos delimitados mediante punto y coma, ya que en la región la coma se
utiliza como separador decimal y podrían producirse inconsistencias. Se solicita:
a. Generar un nuevo archivo CSV con el número de legajo, el nombre del alumno, la
carrera y el promedio, calculado con dos decimales.
b. Mostrar un listado con los datos de los diez mejores alumnos de la facultad de Ingeniería,
ordenado de mayor a menor según el promedio de cada uno. Recuerde que
no se permite cargar todo el archivo en memoria. Se valorará la calidad de la solución
elegida.
c. Informar cuántos alumnos están inscriptos en cada carrera.
d. El programa debe incluir por lo menos una función recursiva.
Se suministra un archivo de texto llamado NOTAS.TXT a modo de ejemplo. Tener en cuenta
que el programa debe servir para cualquier archivo con las mismas características, aunque
su cantidad de registros sea diferente.
Ejemplo del archivo de entrada:
1080075;Torres, Alexander;Electronica;5;3;1;6;6;7
1072856;Lucero, Fatima Claudia;Electromecanica;8;7;9;6;8;1;2;3;4;4;10
109400;Herrera, Fatima Marcela;Alimentos;7;8;4;5
Ejemplo del archivo de salida:
1080075;Torres, Alexander;Electronica;4.67
1072856;Lucero, Fatima Claudia;Electromecanica;5.64
109400;Herrera, Fatima Marcela;Alimentos;6.00
