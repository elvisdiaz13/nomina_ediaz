#Elvis A. Diaz G.
#Cedula: 16.496.981
from datetime import datetime #importar, formato de fecha
import os

#funcion para formato de fecha de ingreso de los empleados
def inv_fecha(fecha_ing):
    newFI = datetime.strptime(fecha_ing,'%d/%m/%Y')
    return datetime.strftime(newFI,'%Y-%m-%d')


print("BIENVENIDOS")
print("YABADABADU C.A.")

archivo_up = 'nomina.txt'
archivo = open("pago_nomina_12sep2021.py", "w")

#validacion de los datos ingresados por el usuario
while True:
    try:
        bono_g = int(input("Ingrese el % del Bono General: "))
        bono_e = int(input("Ingrese el % del Bono Eficiencia: "))
    except ValueError:
        print("Ingrese el % correcto.")
        continue

    if bono_g < 0 and bono_e < 0 :
        print("Debes ingreso un % positivo.")
        continue
    else:
        break

archivo.write("cedula   fecha_ingreso   empleado     sueldo_base  salario_devengado\n")
with open('datos.txt', 'r') as fichero:
    #linea = fichero.readline()
    for linea in fichero:
        print("╔═══════════════════════════════════╗")
        linea = fichero.readline()
        nomina = linea

        #Declaro array para guardar la cedula
        array = []
        array = nomina.split( )
    
        cedula = array[0].lower().replace(' ', '')#Quita los espacios en vacio de la cadena string de la variable creada
        print("  Cedula: ",cedula)

        fecha_ingreso = array[1].lower().replace(' ', '')#Quita los espacios en vacio de la cadena string de la variable creada
        fecha_ing = inv_fecha(fecha_ingreso)
        print("  Fecha Ingreso: ",fecha_ing)

        print("  Empleado: ",array[2],(""),array[3])
        empleado = array[2],array[3]#crea la variable emleados con nombre y apellido

        print("  Salario Base: ",array[4])
        salario_base = array[4].lower().replace('$', '') #Quita los espacios en vacio de la cadena string de la variable creada
        salario_base = int(salario_base)

        horas_extras = int(array[5]) #asignacion de las horas trabajadas
        print("  Horas Extras: ",horas_extras)

        bono_general = 0 #inicio del calculo del bono general
        bono_general = salario_base* (float(bono_g) / 100)
        print ("  Bono General:",bono_general,"$")

        if horas_extras > 5: #Bono Eficiencia
            bono_eficiencia = salario_base*(float(bono_e) / 100)
            print ("  Bono Eficienca:",bono_eficiencia,"$")
        else:
            bono_eficiencia = 0
            print ("  Bono Eficienca:",bono_eficiencia,"$")
        
        salario = salario_base + bono_general + bono_eficiencia
        print ("  Sueldo:",salario,"$")
        print("╚═══════════════════════════════════╝")
        
        archivo.write(str (cedula) +"  "+ str (fecha_ing)+"    "+ str (array[2])+" "+ str (array[3])+"    "+ str (salario_base)+"$   "+ str (salario)+ "$\n")
                
fichero.close()
archivo.close()
