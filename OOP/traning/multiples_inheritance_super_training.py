
class UnidadeImobiliaria:
    def __init__(self, proprietario, localizacao, area):
        self.proprietario = proprietario
        self.localizacao = localizacao
        self.area = area
        


class Predio(UnidadeImobiliaria):
    def __init__(self, proprietario, localizacao, area, name, andar):
        super().__init__(proprietario, localizacao, area)
        self.name = name
        self.andar = andar
        
    def get_andar(self):
        print(f"O predio {self.name} possui {self.andar} andares")
        
    def describe_predio(self):
        print(f"Tipo: Prédio; Proprietário: {self.proprietario}; localização {self.localizacao}; area: {self.area}")
        

class Casa(UnidadeImobiliaria):
    pass


class Apartamento(Predio):
    pass

class Lote(UnidadeImobiliaria):
    pass


p1 = Predio("Fernando Jordão", "Centro - Angra dos Reis/RJ", 255, "Prefeitura Municipal de Angra dos Reis", "5º" )


print(p1.describe_predio())