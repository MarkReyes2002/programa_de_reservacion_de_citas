HorarioMatriz = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
HoraElegida = 0

#Intro
print ("Bienvenido a la pagina de reservación de citas")
print (" ")

print ("Horario de atención:")
print ("Lunes - Viernes")
print ("8:00 AM - 6:00 PM")
print (" ")

print ("Todas las citas tienen una duración de 2 horas")
print (" ")

#Nombre
InputNombre = str(input("Para empezar ingrese su nombre: "))
print (" ")

#Fecha
FechaMatriz = 0
InputFecha = str(input("Para que día desearía hacer su reserva: "))
InputFecha = InputFecha.lower()

#Entregador de numero del 0 al 4 por fecha
if InputFecha == "lunes":
  FechaMatriz = 0
elif InputFecha == "martes":
  FechaMatriz = 1
elif InputFecha == "miercoles":
  FechaMatriz = 2
elif InputFecha == "jueves":
  FechaMatriz = 3
elif InputFecha == "viernes":
  FechaMatriz = 4
else:
  #En caso de datos no validos
  print (" ")
  print("ERROR")
  print("DATOS NO VALIDOS")
  print ("POR FAVOR REINICIE EL PROGRAMA")
  sys.exit(1)
print (" ")


#Entregador de numero del 0 al 4 por hora (Unico formato aceptado : hh:mm)
HoraMatriz = 0
print("¿Para que horario desearía hacer su reserva? ")
print("Los horarios son:")
print("8:00 - 10:00")
print("10:00 - 12:00")
print("12:00 - 14:00")
print("14:00 - 16:00")
print("16:00 - 18:00")
print (" ")

InputHora = input("Horario: ")

if InputHora == "8:00 - 10:00":
  HorarioMatriz [FechaMatriz] = [InputNombre, 0, 0, 0, 0]
elif InputHora == "10:00 - 12:00":
  HorarioMatriz [FechaMatriz] = [0, InputNombre, 0, 0, 0]
elif InputHora == "12:00 - 14:00":
  HorarioMatriz [FechaMatriz] = [0, 0, InputNombre, 0, 0]
elif InputHora == "14:00 - 16:00":
  HorarioMatriz [FechaMatriz] = [0, 0, 0, InputNombre, 0]
elif InputHora == "16:00 - 18:00":
  HorarioMatriz [FechaMatriz] = [0, 0, 0, 0, InputNombre]
else:
  #En caso de datos no validos
  print (" ")
  print("ERROR")
  print("SU ELECCIÓN NO SE ENCUENTRA EN LAS OPCIONES BRINDADAS")
  print ("POR FAVOR REINICIE EL PROGRAMA")
  sys.exit(1)
print (" ")

#Final
print ("¡Reservación exitosa!")
print ("Datos de la reservación:")
print ("Nombre: ", InputNombre.upper())
print ("Fecha:", InputFecha.upper())
print ("Hora:", InputHora)


