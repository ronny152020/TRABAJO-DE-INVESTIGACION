from math import factorial
import os
MAGENTA = '\033[35m'
RESET = '\033[39m'
YELLOW = '\033[33m'
class tratamientolistas:
    def __init__(self,datos):
        self.datos=datos
        
    def presentarlista(self):      
        aux=[]
        for i in self.datos:
            aux.append(i)
        print("la lista es: ",aux)
        
    def buscarlista(self,valor):
        x=False
        for i in self.datos:
            if i==valor:
                print("El valor si esta {}".format(valor))
                x=True
        if x==False:
            print("El valor no se encuentra")
            
    def listaprimos(self):
        aux=[]
        for prim in self.datos:
            con=0
            for num in range(2,prim):
                if prim%num==0:
                    con+=1
            if con==0:
                aux.append(prim)
        return aux
    
    def listafactorial(self):
        aux=[]
        for fac in self.datos:
            acu=1
            res=factorial(fac)
            aux.append(res)
        print("Estos son los factoriales de los numeros de las lista:\n",aux)
    
    def listanotas(self,cantalum):
        alumnos = {}
        for num in range(cantalum):
            alumno = input("Nombre del alumno: ")
            os.system("cls")
            while alumno in alumnos:
                print("Alumno ya existe.")
                alumno = input("Nombre del alumno: ")
            notas=[]
            cantnotas=int(input("Introduzca la cantidad de notas que desea guardar: "))
            os.system("cls")
            for i in range(cantnotas):
                os.system("cls")
                nota=int(input("Ingrese una nota: "))
                notas.append(nota)
            alumnos[alumno] = notas.copy()
        print(alumnos)
        
    def insertarlista(self,valor,posicion):
        os.system("cls")
        while posicion>len(self.datos):
            posicion=int(input("La posicion donde se quiere insertar el valor no existes, intente con una posicion menor, que sea entre [0 y {}]: ".format(len(self.datos)-1)))
        anexo=[]
        for pos,ele in enumerate(self.datos):
            if pos==posicion:
                anexo.append(valor)
                break
        print("Su lista inicial era: ",self.datos)
        self.datos=self.datos[:posicion]+anexo+self.datos[posicion:]
        return self.datos
         
    def eliminarlista(self,valor):
        os.system("cls")
        print("Este es su lista inicial: \n",self.datos) 
        listanueva=[]
        for i in self.datos:
            if i!=valor:
                listanueva.append(i)    
        print("Esta es su nueva lista eliminando las ocurrencias con el valor identificado [{}]: \n{}".format(valor,listanueva))
           
    def retornarvalorlista(self,posicion):
        ele=self.datos[posicion]
        self.datos=self.datos[0:posicion]+self.datos[posicion+1:]
        return ele 
        
    def copiartuplalista(self,tupla):
        lista=[]
        print("La tupla es: ",tupla)
        for i in tupla:
            lista.append(i)
        return lista
    
    def vueltolista(self,cantidad):
        caja={}
        for num in range(cantidad):
            cliente = input(RESET+"Buen dia, su nombre por favor: ")
            os.system("cls")
            cuenta=[]
            cantprod=int(input("Introduzca la cantidad de productos que desea comprar: "))
            productos=[]
            npro=[]
            for i in range(cantprod):
                os.system("cls")
                producto=input("Ingrese el nombre del producto: ")
                costopro=float(input("Ingrese el costo del producto por unidad: "))
                cant=int(input("¿Cuantas unidades desea de este producto? "))
                subtotal=costopro*cant
                productos.append(producto)
                cuenta.append(subtotal)
                npro.append(cant)
            caja[cliente] = cuenta.copy()
            os.system("cls")
            acu=0
            for i in cuenta:
                acu+=i
            print("Su cuenta a pagar es de $ {}".format(acu))
            dinero=float(input("Ingrese la cantidad de dinero que posee: "))
            cliente_mayus=cliente.upper()
            while dinero<acu:
                dinero=float(input("No alcanza con ese dinero, vuelva a ingresar otra cantidad mayor: "))
                os.system("cls")
            os.system("cls")
            if dinero==acu:
                for num,pro,sub in zip(npro,productos,cuenta):
                    print("El total a pagar por {} {} es = {} dolares  ".format(num,pro,sub))
                print("{} su cuenta es {}\nEsta completo no hay vuelto, gracias vuelva pronto".format(cliente_mayus,acu))
            else:
                vuelto=dinero-acu
                for num,pro,sub in zip(npro,productos,cuenta):
                    print("El total a pagar por {} {} es = {} dolares ".format(num,pro,sub))
                print(YELLOW+"{} su cuenta total es {} dolares\nSu vuelto es $ {} ".format(cliente_mayus,acu,vuelto))
