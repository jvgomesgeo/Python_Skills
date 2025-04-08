estoque = {'Calça Jeans':{5: 30.9},
           'Camiseta':{15 : 5.60},
           'Óculos':{8: 7.55},
           'Tênis':{ 7: 56.7},
           'Cinto':{3 : 12.3},
           'Regata': {1 : 4.7},
           'Bermuda':{5: 7.4}
           }

options = ["1- Add Protudo ao Estoque", 
           "2- Visualizar Estoque", 
           "3- Registrar Venda", 
           "4- Remover Protudo", 
           "q- Sair"]

while True:

    print("-" * 20)
    for opt in options:
        print(opt)
    print("-" * 20)

    choice = input("Digite a opção desejada: ")
    if choice == "q".lower():
        break
        
    elif choice == "1":
        new_product = input("Digite o produto a ser adicionado")
        quant_new_product = int(input("Digite a quantidade do produto a ser adicionado"))
        preco_new_product = float(input("Digite o valor do produto a ser adicionado"))
        estoque.update({new_product: {quant_new_product : preco_new_product}})
        
        print()
        print(f"Produto adicionado: {new_product}")
        print(f"Quantidade inicial: {quant_new_product}")
        print(f"Preço unitário: ${preco_new_product}")
    
    elif choice == "2":

        print("--- Estoque ---")
        for key, value in estoque.items():
            print(f"{key}: Quantidade {list(estoque.get(key).keys())[0]} unidades, Preço ${round(list(estoque.get(key).values())[0], 2)}")

        print("-" * 20)

    elif choice == "3":

        product_sold = input("Digite o produto a ser vendido: ")
        quant_sold = int(input(f"Digite a quantidade a ser vendida de produtos do tipo {product_sold}: "))
        
        if product_sold in estoque.keys():
            if quant_sold> list(estoque.get(product_sold).keys())[0]:
                print(f"Estoque insuficiente de {product_sold}. Disponível: {list(estoque.get(product_sold))[0]} unidades")
            else:
                print(f"Venda confirmada. Estoque de {product_sold} está com {(list(estoque.get(product_sold))[0]) - quant_sold} unidades")

        else:
            print(f"Produto inválido !")
    
    elif choice == "4":
        removed_product = input("Digite o produto que quer remover do estoque")
        
        if removed_product in estoque.keys():
            estoque.pop(removed_product)
            print(f"{removed_product} Removido")

        else:
            print(f"Produto inválido !")

        print("--- Novo Estoque ---")
        for key, values in estoque.items():
            print(f"{key} : {values}")
        
        print(20* '-')


print("--- Sistema fechado ---")
