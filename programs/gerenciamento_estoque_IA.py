estoque = {
    'Calça Jeans': {'quantidade': 5, 'preco': 30.9},
    'Camiseta': {'quantidade': 15, 'preco': 5.60},
    'Óculos': {'quantidade': 8, 'preco': 7.55},
    'Tênis': {'quantidade': 7, 'preco': 56.7},
    'Cinto': {'quantidade': 3, 'preco': 12.3},
    'Regata': {'quantidade': 1, 'preco': 4.7},
    'Bermuda': {'quantidade': 5, 'preco': 7.4}
}

options = [
    "1 - Adicionar Produto ao Estoque",
    "2 - Visualizar Estoque",
    "3 - Registrar Venda",
    "4 - Remover Produto",
    "q - Sair"
]

def adicionar_produto():
    new_product = input("Digite o produto a ser adicionado: ")
    while True:
        try:
            quant_new_product = int(input("Digite a quantidade do produto a ser adicionado: "))
            break
        except ValueError:
            print("Erro: Por favor, digite um número inteiro para a quantidade.")
    while True:
        try:
            preco_new_product = float(input("Digite o valor do produto a ser adicionado: "))
            break
        except ValueError:
            print("Erro: Por favor, digite um número válido para o preço.")
    estoque[new_product] = {'quantidade': quant_new_product, 'preco': preco_new_product}
    print(f"\nProduto adicionado: {new_product}, Quantidade inicial: {quant_new_product}, Preço unitário: ${preco_new_product:.2f}")

def visualizar_estoque():
    print("\n--- Estoque ---")
    if not estoque:
        print("Estoque vazio.")
    else:
        for produto, detalhes in estoque.items():
            print(f"{produto}: Quantidade = {detalhes['quantidade']}, Preço = ${detalhes['preco']:.2f}")
    print("-" * 20)

def registrar_venda():
    product_sold = input("Digite o produto a ser vendido: ")
    if product_sold in estoque:
        while True:
            try:
                quant_sold = int(input(f"Digite a quantidade a ser vendida de {product_sold}: "))
                break
            except ValueError:
                print("Erro: Por favor, digite um número inteiro para a quantidade.")

        if quant_sold <= estoque[product_sold]['quantidade']:
            valor_venda = quant_sold * estoque[product_sold]['preco']
            estoque[product_sold]['quantidade'] -= quant_sold
            print(f"Venda registrada! Total: $ {valor_venda:.2f}")
            print(f"Estoque de {product_sold} atualizado para: {estoque[product_sold]['quantidade']} unidades")
        else:
            print(f"Estoque insuficiente de {product_sold}. Disponível: {estoque[product_sold]['quantidade']} unidades")
    else:
        print("Produto inválido!")

def remover_produto():
    removed_product = input("Digite o produto que quer remover do estoque: ")
    if removed_product in estoque:
        del estoque[removed_product]
        print(f"Produto '{removed_product}' removido do estoque.")
        visualizar_estoque()
    else:
        print("Produto inválido!")

while True:
    print("-" * 20)
    for opt in options:
        print(opt)
    print("-" * 20)

    choice = input("Digite a opção desejada: ")
    if choice == "q".lower():
        break
    elif choice == "1":
        adicionar_produto()
    elif choice == "2":
        visualizar_estoque()
    elif choice == "3":
        registrar_venda()
    elif choice == "4":
        remover_produto()
    else:
        print("Opção inválida. Por favor, digite uma opção válida.")

print("--- Sistema fechado ---")