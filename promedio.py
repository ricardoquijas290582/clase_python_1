nombre = input('Nombre? ')
print("Me alegro de conocerle " + nombre)

cal_1 = float(input("Ingresa calif 1: "))
cal_2 = float(input("Ingresa calif 2: "))
cal_3 = float(input("Ingresa calif 3: "))

promedio = (cal_1 + cal_2 + cal_3) / 3

if promedio >= 7:
    print('Aprobado!')
else:
    print('Reprobado!, suerte para la próxima...')
