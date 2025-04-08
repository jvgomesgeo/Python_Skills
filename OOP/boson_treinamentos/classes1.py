#Orientação a objetos: Paradigma de programação
#Classes e Objetos.
# Atributos são propriedades da classe
# Métodos são as funcionalidades da classe

class Veiculo:
    def __init__(self, fabricante, modelo, motor, cor, ano):
        self.__fabricante = fabricante #Se eu colocar __ antes do atributo, eu torno ele encapsulado, ou seja o dado armazenado dentro deles n fica acessível diretamente
        self.__modelo = modelo
        self.motor = motor
        self.cor = cor
        self.ano = ano
        self.id = None #nem todos os atributos eu preciso passar no __init__, porém os que nao sao passados, tem que ter seus valores declaros
        
    #Método Setter para setar um valor do atributo
    def set_id(self, id):
        self.id = id
        
    #Método Getter para pegar (get) um valor do atributo
    def get_id(self):
        return self.id

    def move(self):
        print(f"O veículo e me desloco! ")    
    
    # Método Getter para pegar dados encapsulados
    def descrever_veiculo(self):
        return f"O veículo é da fabricante: {self.__fabricante}; Modelo: {self.__modelo}; Motor: {self.motor}, Cor: {self.cor}; Ano: {self.ano}"
    #caso eu n tivesse passado o __ antes do modelo, daria erro, pois o dados está encapsulado
        
        
        
#HERANÇAS - classes que recebem atributos de outras classes diferentes. 
#EX: podem existir diferentes tipos de veículo que receberão os mesmos atributos da classe veiculo.
class Moto(Veiculo):
    #Metodo init sera herdado
    #Posso criar um metodo com o mesmo nome que o herdado, o herdado n sera usado nesse caso
    def move(self):
        print(f"Sou uma moto e ando pelas ruas")
    
    def descrever_moto(self):
        return f"Motor: {self.motor}, Cor: {self.cor}; Ano: {self.ano}"
        
class Carro(Veiculo):
    def move(self):
        print(f"Sou um carro e ando adoidado")
    
    def descrever_car(self):
        return f"Motor: {self.motor}, Cor: {self.cor}; Ano: {self.ano}"


class Plane(Veiculo):
    def __init__(self, fabricante, categoria, modelo, motor, cor, ano):
        self.categoria = categoria
        super().__init__(fabricante, modelo, motor, cor, ano) #esse codigo copia as configs feita do init da classe de herança.
        
    def get_category(self):
        return self.categoria
    
    
    
    
if __name__ == '__main__':
    meu_veiculo = Veiculo("Toytota", "Corolla", 1.8, "Cinza", 2024)
    minha_moto = Moto("Honda", "Titan 225", 1.2, "Vermelha", 2025)
    meu_carro = Carro("Hiunday", "Elantra", 1.4,"Azul", 2021 )
    my_plane = Plane("Emirate", "Airbus", "Comercial", 45, "White-Blue", 2020)
    print(my_plane.descrever_veiculo())
    print(my_plane.get_category())