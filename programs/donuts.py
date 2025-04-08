# #"""
# 01. donuts

# Dado um contador inteiro do numero de donuts, retorne uma string
# com o formato 'Number of donuts: <count>' onde <count> é o numero
# recebido. Entretanto, se o contador for 10 ou mais, use a palavra 'many'
# ao invés do contador.
# Exemplo: donuts(5) retorna 'Number of donuts: 5'
# e donuts(23) retorna 'Number of donuts: many'
# """


def count_donuts():
    ipt_ = int(input("Enter the donuts amount: "))
    
    
    if ipt_ < 10:
        return print(f"Number of donuts: {ipt_}")
    else:
        return print(f"Number of donuts: many")
    
    
if __name__ == '__main__':
    count_donuts()
    