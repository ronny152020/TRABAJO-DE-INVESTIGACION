from menu import menu_principal
from calculadora import calEstandar,calCientifica,calculadora
from operacion_numeros import basico,intermedio
from Tratamiento_de_listas import tratamientolistas
from OperacionesDeCadena import cadena
import os
MAGENTA = '\033[35m'
RESET = '\033[39m'
YELLOW = '\033[33m'

opcion=""
while opcion!=5:
    inicio=menu_principal("Menu principal",["1.- calculadora","2.-operacion numeros ", "3.- listas ", "4.- cadenas", "5.- salir"])
    opcion=inicio.menus()
    os.system("cls")
    if opcion==1:
        cal=""
        while cal!=10:
            os.system("cls")
            inicio=menu_principal("MENÚ CALCULADORA",["1.- Suma","2.- Resta","3.-Multiplicacion","4.-Division","5.- Exponente","6.- Valor absoluto","7.- Circunferencia","8.- Área Círculo","9.- Área Cuadrado","10.- Salir"])
            cal=inicio.menus()
            os.system("cls")
            if cal>=1 and cal<=4:
                print("Calculadora Básica")
                num1=int(input(RESET+"Ingrese un primer numero: "))
                num2=int(input(RESET+"Ingrese un segundo numero: "))
                calba=calculadora(num1,num2)
                if cal==1:
                    calba.suma()
                    input("presione cualquier tecla para continuar...")
                elif cal==2:
                    calba.resta()
                    input("presione cualquier tecla para continuar...")
                elif cal==3:
                    calba.multiplicacion()
                    input("presione cualquier tecla para continuar...")
                elif cal==4:
                    calba.division()
                    input("presione cualquier tecla para continuar...")
            elif cal>=5 and cal<=6:
                print(MAGENTA+"Calculadora Estandar")
                if cal==5:
                    num1=int(input(RESET+"Ingrese el numero base: "))
                    num2=int(input(RESET+"Ingrese el exponente: "))
                    cales=calEstandar(num1,num2)
                    cales.exponente()     
                    input("presione cualquier tecla para continuar...")
                elif cal==6:
                    num1=""
                    num2=""
                    numero=int(input(RESET+"Ingrese un numero para determinar su valor absoluto: "))
                    cales=calEstandar(num1,num2)
                    cales.valor_absoluto(numero)
                    input("presione cualquier tecla para continuar...")
            elif cal>=7 and cal<10:
                print(MAGENTA+"Calculadora Cíentifica")
                num1=""
                num2=""
                calcien=calCientifica(num1,num2)
                if cal==7:
                    radio=int(input(RESET+"Ingrese el valor de radio: "))
                    calcien.circunferencia(radio)
                    input("presione cualquier tecla para continuar...")
                elif cal==8:
                    radio=int(input(RESET+"Ingrese el valor de radio: "))
                    calcien.areaCirculo(radio)
                    input("presione cualquier tecla para continuar...")
                elif cal==9:
                    lado=int(input(RESET+"Ingrese el lado del cuadrado: "))
                    calcien.areaCuadrado(lado)
                    input("presione cualquier tecla para continuar...")
            else:
                input(MAGENTA+"presione una tecla para volver a MENU PRINCIPAL.......") 
                os.system("cls")
    elif opcion==2:
        opnum=""
        while opnum!=11:
            os.system("cls")
            inicio=menu_principal("MENU DE OPERACION DE NUMEROS",["1.- Presentar numeros de 1 a n","2.- Sumar los numeros de 1 a n","3.- Multiplos","4.- Divisores","5.- Numero primo","6.- Factorial","7.- Fibonacci","8.- Perfecto","9.- Primos gemelos","10.- Numeros amigos","11.- Salir"])
            opnum=inicio.menus()    
            os.system("cls")
            if opnum>=1 and opnum<=5:
                print("Operador Basico")
                opba=basico()
                if opnum==1:
                    n=int(input(RESET+"Ingrese un numero: "))
                    opba.numerosN(n)
                    input(RESET+"\npresione cualquier tecla para continuar...")
                elif opnum==2:
                    n=int(input(RESET+"Ingrese un numero: "))
                    print(opba.sumnumN(n))
                    input("presione cualquier tecla para continuar...")
                elif opnum==3:
                    numero=int(input(RESET+"Ingrese un numero: "))
                    opba.multiplo(numero)
                    input("presione cualquier tecla para continuar...")
                elif opnum==4:
                    numero=int(input(RESET+"Ingrese un numero: "))
                    opba.divisoresnumero(numero)
                    input("presione cualquier tecla para continuar...")
                elif opnum==5:
                    numero=int(input(RESET+"Ingrese un numero: "))
                    opba.primo(numero)
                    input("presione cualquier tecla para continuar...")
            elif opnum>=6 and opnum<11:
                print(MAGENTA+"Operador Intermedio")
                opinter=intermedio()
                if opnum==6:
                    numero=int(input(RESET+"Ingrese un numero: "))
                    opinter.factorial(numero)
                    input("presione cualquier tecla para continuar...")
                elif opnum==7:
                    n=int(input(RESET+"Ingrese un numero: "))
                    opinter.fibonacci(n)
                    input("presione cualquier tecla para continuar...")
                elif opnum==8:
                    numero=int(input(RESET+"Ingrese un numero: "))
                    opinter.perfecto(numero)
                    input("presione cualquier tecla para continuar...")
                elif opnum==9:
                    print(YELLOW+"NOTA:\nLos dos numeros deben ser positivos\nLos dos numeros no deben ser iguales\nEl primer numero ingresado debe ser menor al segundo\nCaso contrario se le va a volver a preguntar")
                    num1=int(input(RESET+"Ingrese un primer numero entero y positivo: "))
                    num2=int(input(RESET+"Ingrese un segundo numero entero y positivo: "))
                    opinter.primosgemelos(num1,num2)
                    input("presione cualquier tecla para continuar...")
                elif opnum==10:
                    num1=int(input(RESET+"Ingrese un primer numero: "))
                    num2=int(input(RESET+"Ingrese un segundo numero: "))
                    opinter.amigos(num1,num2)
                    input("presione cualquier tecla para continuar...")
            else:
                input(MAGENTA+"presione una tecla para volver a MENU PRINCIPAL.......") 
                os.system("cls")
    elif opcion==3:
        oplista=""
        while oplista!=11:
            os.system("cls")
            inicio=menu_principal("MENU TRATAMIENTO DE LISTAS",["1.- Recorrer y presentar los datos de una lista","2.- Buscar un valor en una lista","3.- Retornar una lista con los factoriales","4.- Retornar una lista de numeros primos","5.- Recorrer una lista de diccionario con notas de alumnos","6.- Insertar un dato en una Lista dada lo Posición","7.- Eliminar todas las ocurrencias en una Lista","8.- Retornar cualquier valor de una lista eliminándolo ","9.- Copiar cada elemento de una tupla en una lista","10.- Dar el vuelto a varios clientes","11.- Salir"])
            oplista=inicio.menus()
            os.system("cls")
            if oplista==1:
                cantele=int(input("Introduzca la cantidad de elementos que desea ingresar a la lista: "))
                lista=[]
                for i in range(cantele):
                    ele=str(input("Introduzca el elemento: "))
                    lista.append(ele)
                    os.system("cls")
                tralista=tratamientolistas(lista)
                tralista.presentarlista()
                input("presione cualquier tecla para continuar...")
            elif oplista==2:
                cantele=int(input("Introduzca la cantidad de elementos que desea ingresar a la lista: "))
                lista=[]
                for i in range(cantele):
                    ele=str(input("Introduzca el elemento: "))
                    lista.append(ele)
                    os.system("cls")
                tralista=tratamientolistas(lista)
                print(lista)
                valor=str(input(RESET+"Ingrese el valor que desea buscar: "))
                tralista.buscarlista(valor)
                input("presione cualquier tecla para continuar...")
            elif oplista==3:
                cantnum=int(input("Introduzca la cantidad de numeros que desea ingresar: "))
                numeros=[]
                for num in range(cantnum):
                    ele=int(input("Introduzca un numero: "))
                    numeros.append(ele)
                    os.system("cls")
                tralista=tratamientolistas(numeros)
                print("La lista creada es {} ".format(numeros))
                tralista.listafactorial()
                input("presione cualquier tecla para continuar...")
            elif oplista==4:
                cantnum=int(input("Introduzca la cantidad de numeros que desea ingresar: "))
                numeros=[]
                for num in range(cantnum):
                    ele=int(input("Introduzca un numero: "))
                    numeros.append(ele)
                    os.system("cls")
                tralista=tratamientolistas(numeros)
                print("La lista creada es {} ".format(numeros))
                print("Los numeros primos de la lista son: {} ".format(tralista.listaprimos()))
                input("presione cualquier tecla para continuar...")
            elif oplista==5:
                datos=""
                cantalum = int(input("Introduce la cantidad de alumnos que vamos a guardar: "))
                tralista=tratamientolistas(datos)
                tralista.listanotas(cantalum)
                input("presione cualquier tecla para continuar...")
            elif oplista==6:
                cantidadele = int(input("Introduce la cantidad de elementos para la lista: "))
                os.system("cls")
                lista=[]
                for i in range(cantidadele):
                    elem=str(input("Introduzca un elemento: "))
                    lista.append(elem)
                    os.system("cls")
                tralista=tratamientolistas(lista)
                valor=str(input("Ingrese el valor que desea agregar en la lista:\n "))
                os.system("cls")
                print("Segun su lista creada = {}\n ".format(lista))
                posicion=int(input("Ingrese en que lugar desea agregar el valor [0.....{}] ".format(len(lista)-1)))
                print(MAGENTA+"Esta es su nueva lista:\n",tralista.insertarlista(valor,posicion))
                input(RESET+"presione cualquier tecla para continuar...")    
            elif oplista==7:
                lista=[]
                cantele=int(input("Introduzca la cantidad de elementos que desea ingresar a la lista: "))
                for i in range(cantele):
                    ele=str(input("Introduzca el elemento: "))
                    lista.append(ele)
                    os.system("cls")
                tralista=tratamientolistas(lista)
                print(YELLOW+"El valor que va a ingresar va ser buscado en la lista\ny luego va eliminado como ocurrencia:")
                valor=str(input(RESET+"Ingrese el valor que va a eliminar: "))
                tralista.eliminarlista(valor)
                input("presione cualquier tecla para continuar...")    
            elif oplista==8:
                cantidadele = int(input("Introduce la cantidad de elementos para la lista: "))
                os.system("cls")
                lista=[]
                for i in range(cantidadele):
                    elem=str(input("Introduzca un elemento: "))
                    lista.append(elem)
                    os.system("cls")
                tralista=tratamientolistas(lista)
                posicion=int(input("Ingrese la posicion que desea despejar [0.....{}] ".format(len(lista)-1)))
                print(tralista.retornarvalorlista(posicion),tralista.datos)
                input("presione cualquier tecla para continuar...")      
            elif oplista==9:
                lista=[]
                cantele=int(input("Introduzca la cantidad de elementos que desea ingresar a la tupla: "))
                for i in range(cantele):
                    ele=str(input("Introduzca el elemento: "))
                    lista.append(ele)
                    os.system("cls")
                tupla=tuple(lista)
                tralista=tratamientolistas("")
                print("Estos son los elementos de la tupla en una lista: ",tralista.copiartuplalista(tupla))
                input("presione cualquier tecla para continuar...")    
            elif oplista==10:
                cantidad = int(input("Introduce la cantidad de clientes :"))
                os.system("cls")
                datos=""
                tralista=tratamientolistas(datos)
                tralista.vueltolista(cantidad)
                input("presione cualquier tecla para continuar...")    
            else:
                input(MAGENTA+"presione una tecla para volver a MENU PRINCIPAL.......") 
                os.system("cls")
            
    elif opcion==4:
        opcad=""
        while opcad!=10:
            os.system("cls")
            inicio=menu_principal("MENU OPERACIONES DE CADENAS",["1.- Recorrer y presentar los datos de una cadena","2.- Buscar un carácter en una cadena","3.- Retornar una lista con la posiciones dado un carácter de la cadena","4.- Retornar una lista con todas las palabras de una cadena","5.- Retornar una cadena a partir de una lista","6.- Insertar un dato en una cadena dada lo Posición","7.- Eliminar todas las ocurrencias en una cadena","8.- Retornar cualquier valor de una cadena eliminándolo ","9.- Concatenar cadenas","10.- Salir"])
            opcad=inicio.menus()
            os.system("cls")
            if opcad==1:
                elementos = str(input("Por favor ingrese los valores de la cadena: "))
                cad=cadena(elementos)
                cad.recorrerCadena()
                input("\npresione cualquier tecla para continuar...") 
            elif opcad==2:
                elementos = str(input("Por favor ingrese los valores de la cadena: "))
                cad=cadena(elementos)
                print('su cadena ingresada es: %s\n' % elementos)
                caracter=str(input('Por favor ingrese el caracter que desea buscar:\n'))
                cad.buscarCaracter(caracter)
                input("presione cualquier tecla para continuar...")  
            elif opcad==3:
                elementos = str(input("Por favor ingrese los valores de la cadena: "))
                cad=cadena(elementos)
                print('su cadena ingresada es: %s\n' % elementos)
                caracter=str(input('Por favor ingrese el caracter que desea buscar e  identificar su posicion:\n'))
                cad.listaPosiciones(caracter)
                input("presione cualquier tecla para continuar...")  
            elif opcad==4:
                elementos = str(input("Por favor ingrese los valores de la cadena: "))
                cad=cadena(elementos)
                print("Esta es la cadena agregada a una lista: ",cad.listaPalabras())
                input("presione cualquier tecla para continuar...")  
            elif opcad==5:
                cad=cadena("")
                print(cad.cadenaLista())
                input("\npresione cualquier tecla para continuar...") 
            elif opcad==6:
                elementos = str(input("Por favor ingrese los valores de la cadena: "))
                cad=cadena(elementos)
                valor=str(input("Ingrese el valor que quiere agregar: "))
                posicion=int(input("Ingrese en la posicion que va a ubicar el valor [0...{}]: ".format(len(elementos)-1))) 
                print(cad.insertarDato(valor,posicion))
                input(RESET+"\npresione cualquier tecla para continuar...")
            elif opcad==7:
                elementos=str(input("Ingrese una cadena: "))
                cad=cadena(elementos)
                print(YELLOW+"El valor que va a ingresar va ser buscado en la cadena\ny va ser eliminado como ocurrencia")
                buscado=str(input(RESET+"Ingrese el valor que desea eliminar: "))
                cad.eliminarOcurrencias(buscado)
                input(RESET+"presione cualquier tecla para continuar...")   
            elif opcad==8:
                valores=str(input("Ingrese una cadena: "))
                cad=cadena(valores)
                posicion=int(input("Ingrese la posicion que desea despejar [0.....{}] ".format(len(valores)-1)))
                print(cad.retornaValor(posicion),"--- {}".format(cad.cadena))
                input("\npresione cualquier tecla para continuar...")
            elif opcad==9:
                elementos = str(input("Por favor ingrese los valores de la cadena: "))
                cad=cadena(elementos)
                dato=str(input("Ingrese la cadena que se va a concatenar: "))
                os.system("cls")
                print(cad.concatenarCadena(dato))
                input("\npresione cualquier tecla para continuar...")
            else:
                input(MAGENTA+"presione una tecla para volver a MENU PRINCIPAL.......") 
                os.system("cls")
        
input(YELLOW+"Muchas Gracias por su visita")          