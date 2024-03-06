#generame un codigo que realice la busqueda de pares en un rango de numeros

class Pares:
    def __init__(self, n):
        self.n = n

    def __str__(self):
        return "Pares de " + str(self.n)

    #generame los getter y setter de la variable n
    def get_n(self):
        return self.n

    def set_n(self, n):
        self.n = n
    
    def pares(self):
        result = 0
        for i in range(1, self.n+1):
            if i % 2 == 0:
                result += 1
        return result