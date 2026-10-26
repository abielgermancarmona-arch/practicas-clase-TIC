#programa bonos empleados
nombre=input("ingresa tu nombre")
pago_hora=float(input('Pago por hora'))
horas=float(input("Horas trabajadas x mes"))
sueldo= pago_hora*horas
bono=0
if sueldo>=100 and sueldo>=300:
    bono=500
    print ("Tu sueldo es ",sueldo+bono)
elif sueldo>300 and sueldo<=1500:
    bono=1700
    print("Tu sueldo es",sueldo+bono)
elif sueldo>1500 and sueldo<=3000:
    bono=3500
    print ("Tu sueldo es",sueldo+bono)
elif sueldo>3000 and sueldo<=8000:
    bono=8500
    print ("Tu sueldo es",sueldo+bono)
elif sueldo>8000:
    bono=10000
    print ("Tu sueldo es",sueldo+bono)
else:
    print ("no valido")