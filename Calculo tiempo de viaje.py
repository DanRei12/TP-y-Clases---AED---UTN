print ("Este es un programa para calcular el tiempo estimado de viaje en horas, teniendo como velocidad del vehicullo en km""\n")
vel = float(input("Ingrese la velocidad del vehiculo en km/h: "))
d = float(input("\n""Ingrese la distancia a recorrer en km: "))
t = d / vel
seg = t * (60 ** 2)
seg = round(seg, 0)
h = seg // (60 ** 2)
m = (seg % (60 ** 2)) // 60
segt = (seg % (60 ** 2)) % 60
h = int(h)
m = int(m)
segt = int(segt)
print ("El viaje duraria aproximandamente", h, "horas con", m, "minutos y", segt, "segundos.")
print (input())
