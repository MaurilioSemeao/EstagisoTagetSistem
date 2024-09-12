#Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

# A função remove_acentos normaliza o input com padrao de cracteres NFD
# E remove os acentos dos caracteres 
# A função conta_letas recebe uma string verifica 
# Verifica o tamnhao da srt para uma simples validaçõa caso
# Depois converte a string toda pra letras minusculas
# Euso uma metodo count() que passo como parametro a letra "a"
# Depois retorno o resultado como resposta 


import unicodedata as un

def remover_acentos(mss):
    mss_normalizada = un.normalize('NFD', mss)

    mss_sem_acento = ''.join(
        char for char in mss_normalizada 
        if un.category(char) != 'Mn'
    )

    return mss_sem_acento

def conta_letra(mss):
    
    if len(mss) < 1:
        return "Por favor, insira uma mensagem."
    
    mss = mss.lower()
    count = mss.count("a")

    if count <= 0:
        return "Não comtem letra 'a' na menssagem."

    return f"A messagem pissui {count} letra/s 'a'."

mss = input("Digite sua mensagem: ")

print(conta_letra(remover_acentos(mss)))