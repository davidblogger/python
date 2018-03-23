import datetime



def ver_instrucciones():
	print("Operaciones a realizar")
	print("1 ver la hora")
	print("2 Ver la fecha y hora")
	print("3 Hora de New York")
	print("4 Hora de San Francisco")
	print("5 Hora de Paris")
	print("6 Hora de Tokyo")
	print("7 Ver instrucciones")
	print("8 Salir")


def ver_hora(zona_horaria):
	if zona_horaria == -4:
		zona = "Caracas"
	elif zona_horaria == -5:
		zona = "Tiempo del Pacifico"
	elif zona_horaria == +1: 
		zona = "Hora de Paris"
	elif zona_horaria == +9:
		zona = "Hora de Tokyo"	
	else:
		zona = "Tiempo del este"	

	formato = "%H:%M:%S %p"
	zona_horaria = datetime.timezone(datetime.timedelta(hours=zona_horaria))
	hora_actual = datetime.datetime.now(zona_horaria).time()
	hora_formateada = hora_actual.strftime(formato)
	print("La hora exacta en: {} es {}".format(zona,hora_formateada))


def ver_fecha_hora():
	formato = "%B %d, %Y  %H:%M:%S "
	zona_horaria = datetime.timezone(datetime.timedelta(hours=-4))
	fecha_actual = datetime.datetime.now(zona_horaria)
	fecha_formateada = fecha_actual.strftime(formato)
	print("La fecha y la hora exacta es: {}".format(fecha_formateada))	

def ver_reloj():
	print("Bienvenidos al reloj del mundo")
	ver_instrucciones()



	while True:
		operacion = input(": ")
		if operacion == "1":
			ver_hora(-4)
		elif operacion == "2":
			ver_fecha_hora()
		elif operacion == "3":
			ver_hora(-5)
		elif operacion == "4":
			ver_hora(-7)
		elif operacion == "5":
			ver_hora(+1)		
		elif operacion == "6":
			ver_hora(+9)
		elif operacion == "7":
			ver_instrucciones()	
		elif operacion == "8":				
			break
		else:
			print("No reconozco esa operacion")	

	print("Gracias por usar el reloj mundial")			

ver_reloj()				