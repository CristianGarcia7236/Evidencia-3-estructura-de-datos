import sys
import sqlite3
from sqlite3 import Error


Lista_articulos = []
switch = True
clave={}
registro = []
total=[]
pago_total = 0
numero_venta=0

while switch == True:

      print("NEGOCIO DE COSMETICOS")
      print("\n MENU \n")

      print("\n1.-REGISTRAR UNA VENTA\n")
      print("\n2.-CONSULTAR VENTA\n")
      print("\n3.-REPORTE DE VENTAS \n")
      print("\n4.-SALIR")
      eleccion = int(input("\nIngresa la opccion que deses realizar: "))

      if eleccion == 4:
         switch = False
         print("\nHas salido del Menu\n")
      
      
      
      if eleccion == 1:
         
               print("REGISTRO DE VENTA")
               
    
               while eleccion == 1:
                numero_venta=numero_venta+1
                        
                     
                fecha_venta= input(" Ingresa la fecha de la Venta: ")
                descripcion=input(" Ingresa la Descripción del articulo: ")
                cantidad = int(input (" Ingresa la Cantidad de piezas vendidas: "))
                precio= float(input(" Ingresa el Precio de Venta: "))
                monto = cantidad * precio
                pago_total = pago_total + monto
                registro.append(numero_venta)
                registro.append(fecha_venta)
                registro.append(descripcion)
                registro.append(cantidad)
                registro.append(precio)
                registro.append(pago_total)
                total.append(registro)
                eleccion = int(input(" Quieres Ingresar otro articulo: 1.- SI / 0.- NO: "))
                    
                if eleccion == 0:
                    print(f" El Monto total a pagar es : {pago_total}")
                    Lista_articulos.append(registro)
                    eleccion = int(input(" Desea capturar otro registro de venta 1.- SI / 0.- NO: "))
                    if eleccion == 0:
                        switch == True
                            
                try: numero_venta = int(numero_venta)
                except ValueError:
                    print(numero_venta,"no es un entero")
                    exit()
                    
                try: cantidad = int(cantidad)
                except ValueError:
                    print(cantidad,"no es un entero")
                    exit()
                    
                try: precio = int(precio)
                except ValueError:
                    print(precio,"no es un entero")
                    exit()
                    
                try: monto = int(monto)
                except ValueError:
                    print(monto,"no es un entero")
                    exit()
                    
                try: pago_total = int(pago_total)
                except ValueError:
                    print(pago_total,"no es un entero")
                    exit()    
                
                try:
                   with sqlite3.connect("Base_de_Datos.db") as conn:
                       c = conn.cursor()
                       registro = (numero_venta,fecha_venta,descripcion,cantidad,precio,monto,pago_total)
                       c.execute("CREATE TABLE IF NOT EXISTS INVENTARIO (Clave INTEGER PRIMARY KEY, fecha_registro TEXT, Articulo TEXT, Piezas INTEGER, Precio INTEGER, Total INTEGER);")
                       c.execute("INSERT INTO INVENTARIO VALUES(?,?,?,?,?,?,?)")
                       print("Tabla creada exitosamente")
except Error as e:
    print (e)
except:
    print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
finally:
    if (conn):
        conn.close()
    
      if eleccion == 2:
            print("CONSULTA DE VENTA")
               
            
    
                
         
            codigo_venta = int(input("\nIngrese la clave de venta que desea buscar: "))
            for buscar in Lista_articulos:
                if buscar[0] == codigo_venta:
                    print(buscar) 
               
                    eleccion = int(input("\nIngrese la tecla 0 para regresar al Menu Principal: "))
                    if eleccion == 0:
                        switch == True
      
      
      
      
      
      if eleccion == 3:
             print("REPORTE DE VENTAS")
          
             fecha_ventas = input("\nIngrese la fecha de venta que desea buscar  dd/mm/yy: ")
             for registro in Lista_articulos:
                 if registro[1] == fecha_ventas:
                    print(registro)
          
                    eleccion = int(input("\nIngrese la tecla 0 para regresar al Menu Principal: "))
                    if eleccion == 0:
                       switch == True
                       
                       
                       