
edad = int(input("Ingresa por favor tu edad actual: "))
promedio = float(input("Teclea el promedio: "))



if edad < 6:
    print('Kinder')
    print('Tú no aplicas')
elif edad >= 6 and edad < 12:
    print('Primaria')
    if promedio >= 9.5:
       print('Promedio aceptable')
    else:
       print('Promedio no aceptable')


elif edad >= 12 and edad < 15:
    print('Secundaria')
    if promedio > 9.5:
       print('Promedio aceptable')
    else:
       print('Promedio no aceptable')


elif edad >= 15 and edad < 18:
    print('Bachillerato')
    if promedio >= 8.5:
       print('Promedio aceptable')
    else:
       print('Promedio no aceptable')



elif edad >= 18 and edad < 23:
    print('Universidad')
    if promedio >= 8:
       print('Promedio aceptable')
    else:
       print('Promedio no aceptable')



else:
    print('Profesionista')