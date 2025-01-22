# somar é uma "função"

# 'def' é usado pra definir funções
## primeiro_numero e segundo_numero são "parâmetros" dessa função
def somar(primeiro_numero, segundo_numero):
    # return é o que a função retorna. Nesse caso, é a soma de dois números
    return (primeiro_numero + segundo_numero)

# ...int(... está convertendo tudo que está dentro do parênteses pra "inteiro" (número sem vírgula)
primeiro_numero = int(input('Insira o primeiro número, depois aperte Enter:'))

# ...input(... é quando o terminal¹ solicita uma entrada do usuário. Nesse caso, são os números a serem calculados!
segundo_numero = int(input('Insira o segundo número: '))

#print imprime coisas pro terminal¹
print(f'A soma de "{primeiro_numero}" e "{segundo_numero}" é {somar(primeiro_numero, segundo_numero)}!')

# [1] "terminal" é a mesma coisa que console. Se você estiver no windows, aperte o botão Win e digite "cmd"
#    o "prompt de comando" que aparecer é exatamente a mesma coisa que está aqui embaixo
#  
# OBS: no windows, o terminal "novo" se chama "Powershell" (mas é a mesma coisa!!)