# """
# 02. both_ends

# Dada uma string s, retorne uma string feita com os dois primeiros
# e os dois ultimos caracteres da string original.
# Exemplo: 'spring' retorna 'spng'. Entretanto, se o tamanho da string
# for menor que 2, retorne uma string vazia.
# """


def both_ends(string):
    a = string[:2] + string[-2:]
    return a
    


both_ends("Asvedo")