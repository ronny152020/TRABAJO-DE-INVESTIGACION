MAGENTA = '\033[35m'
RESET = '\033[39m'
YELLOW = '\033[33m'
import os
class cadena:
    def __init__(self,cadena):
        self.cadena=cadena


    def  recorrerCadena(self):
        for x in self.cadena:
            print(x,end=" ")
            
    def  buscarCaracter(self, caracter):
        acum=0
        for i in self.cadena:
            if i== caracter:
                acum += 1
        print("Su caracter se encuentra %s veces, dentro de la cadena" % acum)
    

    def  listaPosiciones(self,caracter):
        aux=[]
        for x, i in enumerate(self.cadena):
            if i == caracter:
                aux.append(x)
        print('Su caracter se encuentra en la(s) siguiente(s) posiciones')
        print('%s' % aux)

                
    def listaPalabras(self):
        aux=[]
        for i in self.cadena:
            aux.append(i)
        return aux

    def cadenaLista(self):
        lista=[]
        cantele=int(input("Introduzca la cantidad de elementos que desea ingresar a la lista: "))
        for i in range(cantele):
            ele=str(input("Introduzca el elemento para la lista: "))
            lista.append(ele)
            os.system("cls")
        print("Tu lista es: ",lista)
        caden=" ".join(lista)
        return "\nEsta es la cadena a partir de una lista:\n{}".format(caden)

    def insertarDato(self,buscado,posicion):
        os.system("cls")
        while posicion>len(self.cadena):
            posicion=int(input("La posicion donde se quiere insertar el valor no existes, intente con una posicion menor, que sea entre [0 y {}]: ".format(len(self.cadena)-1)))
        vector1=self.cadena[:posicion]
        vector2=self.cadena[posicion:]
        print("La anterior cadena ingresada es: ",self.cadena)
        return MAGENTA+"La nueva cadena es :\n{} {} {} ".format(vector1,buscado,vector2)

    def eliminarOcurrencias(self,buscado):
        os.system("cls")
        print("Este es su cadena inicial: \n",self.cadena) 
        listaoriginal=list(self.cadena)
        listanueva=[]
        for i in listaoriginal:
            if i != buscado:
                listanueva.append(i) 
        listaA="".join(listanueva)   
        print(MAGENTA+"Esta es su nueva cadena eliminando las ocurrencias por el valor identificado [{}]\n{}".format(buscado,listaA))
        
    def retornaValor(self,posicion):
        ele=self.cadena[posicion]
        self.cadena=self.cadena[0:posicion]+self.cadena[posicion+1:]
        return ele 
        
    def concatenarCadena(self,dato):
        return "La cadena concatenada con la otra es:\n {} {} ".format(self.cadena,dato)
