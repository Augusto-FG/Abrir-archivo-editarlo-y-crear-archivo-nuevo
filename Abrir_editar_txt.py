# FUNCION RECURSIVA
def imprimirlista(lista, inicio=0):
    if inicio < len(lista):
        print(lista[inicio])
        imprimirlista(lista, inicio + 1)


try:

    entrada = open("Notas 1.txt", "rt")
    salida = open("Notas 2.txt", "wt")

    cant_carreras = dict()
    cant_carreras["Alimentos"] = 0
    cant_carreras["Electromecanica"] = 0
    cant_carreras["Electronica"] = 0
    cant_carreras["Industrial"] = 0
    cant_carreras["Informatica"] = 0
    cant_carreras["Telecomunicaciones"] = 0

    dic_mejores_promedios = {}

    # utilizo readlines para no cargar todo el archivo en memoria
    for linea in entrada.readlines():
        lista = linea.split(';')
        legajo, apellido_nombre, carrera = lista[:3]
        lista_notas = lista[3:]

        for i in range(len(lista_notas)):
            lista_notas[i] = int(lista_notas[i])

        promedio = sum(lista_notas) / len(lista_notas)
        promedio = '%.2f' % promedio

        lista_final = [legajo, apellido_nombre, carrera, promedio]
        linea = ';'.join(lista_final)
        salida.write(linea + "\n")

        # mejores promedios
        if len(dic_mejores_promedios) < 10:
            dic_mejores_promedios[lista_final[-1]] = lista_final
        else:
            lista_keys = list(dic_mejores_promedios.keys())
            minimo = min(lista_keys)
            if lista_final[-1] > minimo:
                dic_mejores_promedios[lista_final[-1]] = lista_final
                del dic_mejores_promedios[minimo]

        # contador de carreras
        cant_carreras[carrera] += 1

    # imprimo los datos de los mejores promedios mediante la funcion recursiva
    lista_mejores_promedios = list(dic_mejores_promedios.keys())
    lista_mejores_promedios.sort(reverse=True)

    lista_datos_mejores_promedios = []
    for key in lista_mejores_promedios:
        lista_datos_mejores_promedios.append(dic_mejores_promedios[key])

    print("Datos de los 10 mejores promedios")
    imprimirlista(lista_datos_mejores_promedios)

    print('\n' * 4)

    # imprimo los alumnos inscriptos por carrera
    print("Cantidad de alumnos inscriptos por carrera")
    for key, value in cant_carreras.items():
        print('Hay %d inscriptos en %s' % (value, key))


except FileNotFoundError as error:
    print("Error al abrir los archivos:", error)
except OSError as error:
    print("Error fatal:", error)
else:
    print('\n' * 4)
    print("Proceso finalizado.")
finally:
    try:
        entrada.close()
        salida.close()
    except NameError:
        pass
