MAGENTA = '\033[35m'
RESET = '\033[39m'
YELLOW = '\033[33m'
class menu_principal:
    def __init__(self,titulo,opciones):
        self.titulo=titulo
        self.opciones=opciones
    
    def menus(self):
        print(MAGENTA+self.titulo)
        for opcion in self.opciones:
            print(RESET+opcion)
        x=int(input("Elija una opcion [1....{}]: ".format(len(self.opciones))))
        return x