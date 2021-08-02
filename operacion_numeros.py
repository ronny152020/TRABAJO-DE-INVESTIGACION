MAGENTA = '\033[35m'
RESET = '\033[39m'
class basico:
    def __init__(self):
        pass
    
    def numerosN(self,n):
        con=0
        print(MAGENTA+"Se presentara la serie del 1 al {}".format(+n))
        while con<n:
            con+=1
            print(con,end=" - ")
    
    def sumnumN(self,n):
        acu=n
        for i in range(n):
            acu+=i 
        return acu
    
    def multiplo(self,numero):
        con=1
        for i in range(1,12+1):
            multiplo=numero*con
            con+=1
            print("{} x {} = {} ".format(numero,i,multiplo))
        
    def divisoresnumero(self,numero):
        divisores=[]
        for i in range(1,numero+1):
            res=numero%i
            if res==0:
                divisores.append(i)
        print("Los divisores de {} = {}".format(numero,divisores))
        
    def primo(self,numero):
        con=0
        for divisor in range(1,numero+1):
            if numero%divisor==0:
                con+=1
        if con==2:
            print("El numero {} es primo ".format(numero))
        else:
            print("El numero {} no es primo ".format(numero))
    
    def perfecto(self,numero):
        acu=0
        for divisor in range(1,numero):
            res=numero%divisor
            if res==0:
                acu=acu+divisor
        if acu==numero:
            print("El numero {} es perfecto ".format(numero))
        else:
            print("El numero no es perfecto")
              


class intermedio(basico):
    def __init__(self):
        super().__init__()
        
    def numerosN(self, n):
        for i in range(1,n+1):
            print(i)
    
    def factorial(self,numero):
        acu=1
        for fac in range(numero,0,-1):
            acu=acu*fac
        print("El factorial del numero {} es {} ".format(numero,acu))
        
    def fibonacci(self,n):
        serie=[1]
        x,y,z=0,1,0
        for fib in range(n):
            z=x+y
            serie.append(z)
            x=y
            y=z
        print("La serie fibonacci de 1 hasta {} es {} ".format(n,serie))
        
    def primosgemelos(self,num1,num2):
        while num1<0 or num2<0 or num1==num2 or num1>num2:
            num1=int(input("Vuelva a ingresar otro primer numero: "))
            num2=int(input("Vuelva a ingresar otro segundo numero: "))
        a=0
        for numero in range(num1,num2+1):
            con=2
            esprimo=True
            while esprimo and con<numero:
                if numero%con==0:
                    esprimo = False
                else:
                    con+=1
            if esprimo and not a:
                a=numero
            elif esprimo and a:
                b=numero
                if b-a==2:
                    print("{} y {} son primos gemelos".format(a,b))
                a=numero
    
    def amigos(self,num1,num2):
        divisores_1=[]
        divisores_2=[]
        suma_a=0
        suma_b=0
        for i in range(1,num1):
            if num1%i==0:
                divisores_1.append(i)
        for i in range(1,num2):
            if num2%i==0:
                divisores_2.append(i)
        for sum in divisores_1:
            suma_a=suma_a+sum
        for sum in divisores_2:
            suma_b=suma_b+sum
        if suma_a==num2 and suma_b==num1:
            print("Los numeros si son amigos ")
        else:
            print("Los numeros no son amigos")
