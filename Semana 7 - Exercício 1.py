largura = int(input('Digite a largura:'))
altura = int(input('Digite a altura:'))


linha = 0
coluna = 0


while linha < altura:
    while coluna < 1:
        print(largura*'#', end="")
        coluna = coluna + 1 
    print()
    
    linha = linha + 1
    coluna = 0
