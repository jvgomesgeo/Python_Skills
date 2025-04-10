class Veiculo:
    def __init__(self, name, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.name = name
        
    def ligar(self):
        print(f"O veículo está ligado")
        
    def desligar(self):
        print(f"O veículo está desligado")
        
class Moto(Veiculo):
    def empinar(self):
        print(f"{self.name} está empinando! ")
        

class Carro(Veiculo):
    def abrir_porta_malas(self):
        print(f"{self.name} Porta-malas aberto! ")
        