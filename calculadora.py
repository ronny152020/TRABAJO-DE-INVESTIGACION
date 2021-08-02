from math import pi
GREEN = '\033[32m'
YELLOW = '\033[33m'
MAGENTA = '\033[35m'
class calculadora:
    def __init__(self,numero1,numero2):
        self.num1=numero1
        self.num2=numero2
    
    def suma(self):
        total=self.num1+self.num2
        print("La suma de los dos numeros es: ", total)
    
    def resta(self):
        diferencia=self.num1-self.num2
        print("El resultado de la resta de los dos numeros es: ", diferencia)
    
    def multiplicacion(self):
        producto=self.num1*self.num2
        print("El producto de los dos numeros es: ", producto)
    
    def division(self):
        cociente=self.num1/self.num2
        print("La division de los dos numeros es: ", cociente)


class calEstandar(calculadora):
    def __init__(self, numero1, numero2):
        super().__init__(numero1, numero2)
        
    def multiplicacion(self):
        acu=0
        for i in range(self.num2):
            acu=acu+self.num1
        print("la multiplicacion entre {} , {} es {}  ".format(self.num1,self.num2,acu) )
            
    def exponente(self):
        potencia=self.num1**self.num2
        print("La potencia es: ", potencia)
        
    def valor_absoluto(self,numero):
        if numero>=0:
            print("El valor absoluto de {} es {}  ".format(numero,numero))
        else:
            x=numero*-1
            print("El valor absoluto de {} es {}  ".format(numero,x))
        
        
class calCientifica(calculadora):
    pi=3.1416
    def __init__(self, numero1, numero2):
        super().__init__(numero1, numero2)
        
    def circunferencia(self,radio):
        Cir=2* calCientifica.pi *radio
        print("La longitud de la circunferencia es: ", Cir)
    
    def areaCirculo(self,radio):
        area=calCientifica.pi*(radio**2)
        print("El area del circulo es : ", area)
    
    def areaCuadrado(self,lado):
        areacua=lado*lado
        print("El area del cuadrado es {}u²: ".format(areacua))

