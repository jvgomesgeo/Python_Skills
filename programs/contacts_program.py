#INSERINDO OS DADOS
import random 

infos = {"Fábio": {"idade": 33, 'sexo': "M"},
         "Victor": {"idade": 28, 'sexo': "M"},
         "Julia": {"idade": 25, 'sexo': "F"},
         "Matheus" : {"idade": 30, 'sexo': "M"}
         }


for key, value in infos.items():
    infos[key].update({'tel': str(random.randint(10,99))  + '-'  + 
                       str(random.randint(100000000, 900000000)) })

options = [ "1- Adicionar Contato",
            "2- Buscar Contato",
            "3- Remover contatos",
            "q- Para Sair",
]

def add_contato():
    
    new_ctt = input("Digite o nome do novo contato: ")
    while True:
        try:
            idade = int(input("Digite a idade do contato: "))
            break
        except ValueError:
            print("Erro: Entre com numero válido")

    sexo_ctt = input("Digite o sexo do contato (M ou F):")
    while True:
        try:
            telefone = input("Digite o telefone do contato")
            if len(telefone) > 12:
                print(f"Entre com um numero válido!")
            break
        except ValueError:
            print("Erro: Entre com numero válido")

    infos[new_ctt] = {'idade': idade, 'sexo': sexo_ctt, 'tel': telefone}

def buscar_ctt():
    
    name_ctt = input("Digite o nome do contato para visualizar as informações: ")
    while True:
        try:
            if name_ctt in infos.keys():
                print("Contato: {}; Idade: {} anos; Sexo: {}; Tel: {}".format(
                    name_ctt,
                    list(infos.get(name_ctt).values())[0],
                    list(infos.get(name_ctt).values())[1],
                    list(infos.get(name_ctt).values())[2]
                ))
                break
            else:
                print(f"Contato {name_ctt} inexistente.")
                name_ctt = input("Digite o nome do contato para visualizar as informações: ")
            
        except ValueError:
            print("Erro, insira um nome válido")
    
def remover_ctt():
    ctt_remover = input("Digite o nome do contato a ser removido: ")
    while True:
        try:
            if ctt_remover in infos.keys():
                infos.pop(ctt_remover)
                
                break

            else:
                print(f"Contato {ctt_remover} inexistente.")
                ctt_remover = input("Digite o nome do contato a ser removido: ")
        
        except ValueError:
            print("Erro, insira um nome válido")


def main():
    
    while True:
        print("--- Opções de Contatos ---")
        for opt in options:
            print(opt)

        choice = input("Escolha uma opção: ")
        if choice == 'q'.lower():
            break
        elif choice == "1":
            add_contato()
        elif choice == "2":
            buscar_ctt()
        elif choice == "3":
            remover_ctt()
        else:
            print("Opção inválida. Por favor, digite uma opção válida.")


print("--- Sistema Fechado --- ")

if __name__ == '__main__':
    main()