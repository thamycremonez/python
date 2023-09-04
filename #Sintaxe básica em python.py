#Sintaxe básica em python 

#nome_variavel =dado/valor/atriuto

número =20

nome ='Veronica'

variavel =[21, 'Maria', 19.90]

print(número)
print(nome)
print(variavel)

#Sintaxe
#Leitura léxica
#Indentação

dicionario ={ 'Nome': 'Fernado',
            'Idade':33,
            'Formação':'Eng. da Computação'}

print(dicionario)

#Estrutura básica de um programa

#Olá mundo! 
print('Olá mundo!')

#INT - Número real inteiro, sem casas decimais

num1 =12

num2 =int(15)

print(num1)
print(type(num1))
print(type(num2))

#FLOAT - Número de ponto flutuante / com casas decimais

num3 =12.8

num4 =float(19.8)

print(num3)
print(type(num4))

# STRING - Texto composto de qualquer caractere alfanumerico
palavra1 ='palavra'

palavra2 ="marca d'agua"

frase1 ='Uma frase qualquer'

frase3 ='Ela tinha 8 anos'

frase3 =str('Outra frase qualquer')

print(palavra2)
print(type(frase3))

# List - Conjunto de elementos indexados e mutáveis

lista =[2, 'Pedro', 15.9]

lista2 =list([1,'Maria', 19.99])

print(lista)
print(lista2)

#Tupla - Conjunto de elementos imutáveis

tupla =('Ana', 'Fernando', 3, 19.90)

print(tupla)

# DICT - Dicionários

dicionario ={'Nome': 'Fernando',
              'Idade': '32'}

#Bool - Booleano
condicao1 =True

print(condicao1)
print(type(condicao1))

#Comentários simples de até uma linha

''' Comentário onde não há limite de linhas,
    podendo ser usado para descrever blocos 
    de códigos mais detalhadamente'''

#Tipos de Váriaveis

var_int =12
#Numéro inteiro

var_float =15.3
#Numéro com casas decimais

var_string ='Conjunto de caracteres alfanuméricos'
#Incluindo simbolos e caracteres especiais

var_lista =[1,2,'Paulo','Maria', True]
#Lista de dados/valores

var_dicionario ={'Nome':'Fernando', 'Idade':31}
#Conjunto de dados:valores

var_tupla =('Ana','Fernando', 3)
#Lista de dados/valores porém imutável

var_bool =True
#Booleano / binário (0 ou 1)

var_comentario ="""Um comentário atrinuido a uma variável
                    deixa de ser apenas um comentário, vira um texto 
                    que pode ser incorporado ao codigo..."""

#Declarando uma variavel quanto ao seu tipo

ano_nasc =1987
ano_nasc2 ='1987'
ano_nasc =int(1987)
ano_nasc2 =str(1987)
print(ano_nasc)
print(type(ano_nasc))
print(ano_nasc2)
print(type(ano_nasc2))

#Declarando multiplas variáveis por justaposição
nome ='Maria'
idade =32
sexo ='F'
print(nome)
print(idade)
print(sexo)

nome1, idade1, sexo1 ='João',20,'M'
print(nome1, idade1, sexo1)

#Declarando multiplas variaveis de mesmo tipo e dado

num5 =10
x =10
a1 =10
print(num5)
print(x)
print(a1)

num6 =x1 =a2 =10
print(num6)
print(x1)
print(a2)

#Operação entre variáveis
a =10
b =5.2
print(a+b) #soma simples

#Interações entre variáveis
msg ='Olá '
pessoa ='Carlos'
print(msg + pessoa)

#Palavras reservadas ao sistema (que não podem ser usadas como nome de uma variável)

# and         del         from        not         while
# as          elif        global      or          with
# assert      else        if          pass        yield
# break       else        import      print
# class       exec        in          raise
# continue    finally     is          return
# def         for         lambda      try

#Sintaxe não permitida / não recomendada

#Formas de desclarar uma variável que podem gerar erros de interpretação

# Nome        Nome de variável iniciando em letra maiúscula
# NOME        Nome de variável escrita totalmente em letras maiúsculas
# 8dados        Nome de variável iniciando com números
# _número        Nome de variável iniciando com caractere especial
# minha variavel        Nome de variável com espaços
# número        Nome de variável contendo acentos
# (variavel2)        Nome de variável encapsulado em chaves, parênteses ou colchetes

#Função de saída que exibe em tela ou em terminal
print('Seja bem-vindo!!!')

#Realizando operações aritméticas dentro da função print

print(15 + 4)
print(15 - 4)
print(15 * 4)
print(15 / 4)

#Realizando operações entre dados/valores declarados e variáveis

número1 =30
print('O resultado da soma é: ', número1 + 15)

#Operações lógicas dentro do print()

número2 =9
print(número2 > 3)
print(número2 < 10)
print(número2 ==11)
print(número2 >=12)

#Usando fStrings e máscaras de substituição dentro da função print()
nome ='Fernando'
print(f'Seja muito bem-vindo {nome}!!!')

#Usando operadores por meio de fStrings e suas máscaras 
camisa =19.99
calca =39.90
print(f'A soma dos produtos é: {camisa+calca}')

#Sintaxe antiga vs atual moderna

nome ='Maria'
#Sintaxe funcional básica // Defasada
print('Bem-vindo', nome,'!!!')

#Sintaxe funcional // Defasada
print('Bem-vindo'+' '+nome+' ''!!!')

#Sintaxe antiga // Defasada
print('Bem-vindo %s !!!'%nome)

#Sintaxe usual // Defasada
print('Bem-vindo {} !!!'.fomart(nome))

#Sintaxe moderna atual
print(f'Bem-vindo {nome}!!!')

#Função input
variavel1 =input('Digite o seu nome: ')
print(f'Bem-vindo {variavel1}!!!')

#Operações aritméticas compostas
print((5+2)*7) #Primeiro será realizado a operação dentro dos parenteses

#Potenciação
print(3 ** 5) #3 elevado a 5ª potencia

#Divisão exata
print(9.4 // 3)

#Modulo ou resto de uma divisão
print(10 % 3)

#Atribuição Aditiva, Subtrativa, Multiplicativa, Divisiva, Modulo, Divisão inteira, exponenciação
valor =4
valor +=2 #Atribuição Aditiva
valor -=3 #Atribuição Subtrativa
valor *=5 #Atribuição Multiplicativa
valor /=2 #Atribuição Divisiva
valor %=2 #Atribuição Modulo
valor //=2 #Atribuição Divisão Inteira
valor **=2 #Atribuição Exponenciação

#Arredondando casas decimais
equacao =((50+25)*7.2)/3.8
print(equacao)
print(f'O resultado bruto da equacao é: {equacao:.2f}')

#Operadores lógicos
print( 5 ==9) #Igualdade
print( 7 !=3) #Diferença
print( 8 > 4 ) #Maior que
print( 8 < 32 ) #Menor que
print( 8 >=25 ) #Maior ou igual
print( 8 <=4 ) #Menor ou igual

#Operadores compostos (TODAS AS CONDIÇÕES PRECISAM SER VERDADEIRAS)
print(7 !=3 and 2 > 3)

#Operadores de membro
#is
num7 =4
num8 =25
print(num7 is num8)
print(num7 is 4)

#in
lista =[1,2,3,'Ana','Maria']
print(2 in lista)

#not in
lista1 =[1,2,3,'Ana','Maria']
print(2 not in lista)

#Estrutura condicional simples

#if
nome2 = input('Digite o seu nome:')

if nome2 =='Fernando':
    print('Bem vindo de volta Fernando!')
else:
    print(f'Você é novo(a) aqui, olá {nome2}!')

#elif
num9 =float(input('Digite um número: '))

if num9 <= 50:
    print('Menor que 50')
elif num9 > 50 and num9 < 100:
    print('Maior que 50')
else:
    print('Número inválido')

#Estruturas condicionais com interpolação
nomes = ['Fernando', 'Maria', 'Carlos']
usuario = input('Digite o seu nome: ')

if usuario in nomes:
    print(f'Bem vindo(a) {usuario}')
else:
    print('Usuario não cadastrado')

#Estruturas condicionais compostas com or(ou) e and(e)
veiculo ='Gol'
veiculo1 ='Corsa'
veiculo2 ='Onibus'
cor1 ='Branco'
cor2 ='Vermelho'

if veiculo =='Gol' or veiculo =='Celta':
    print('Carro')
elif veiculo =='Gol' and cor1=='Branco':
    print('Gol branco')
elif veiculo1 =='Onibus' and cor2=='Vermelho':
    print('Onibus vermelho')

#Estrutura de repetição

#While

variavel2 = 0

while variavel2 <= 5:
    print(variavel2)

    variavel2 +=  1

# While com condição
num10 = 0 
total = 10

while num10 <= 10:
    print(num10)
    num10 += 1

    if num10 == 5:
        print('50% computado')
    if num10 == total:
        print('100%, processo encerrado')

# While com validação

validador = input('Digite "Brasil" para continuar:')

while validador != 'Brasil':
    print('Palavra-chave não confere, digite novamente:')
    validador = input('Digite "Brasil" para continuar:')

    if validador == 'Brasil':
        print('Agora você digitou Brasil corretamente')


#While true

while True:
    validador = input('Digite "Brasil" para continuar:')
    if validador == 'Brasil':
        print('Agora você digitou Brasil corretamente')
        break
    else:
        ('Palavra-chave não confere, digite novamente:')

#For
compras = ['Arroz', 'Feijão', 'Massa', 'Carne', 'Pão']

for i in compras:
    print(i)
#------------------
nome3 = 'Alberto'

for i in nome3:
    print(i)
#------------------

for i in range(0,11):
    print(i)
#------------------

vendas = [1000,459,911,200,838,50]
total = 0

for i in vendas:
    total += i

print(total)

#For com intervalo personalizado
for i in range(0,11,2):
    print(i)

#For com intervalo do ultimo para o primeiro
for i in range(10,0, -1):
    print(i)

#------------------
num11 = int(input('Digite o número limite:'))

for i in range(0, num11+1):
    print(i)

#For retornando tamanho da variável
nome = 'Thiago'
num = 0

for num in range(len(nome)):
    print(num)

#Sintaxe básica de uma string
frase = 'Atributo em formato alfanumérico...'

print(frase) 
print(len(frase)) #Contando caracteres
print(len(frase) - frase.count(' ')) #Contando caracteres desconsiderando espaços
print(frase.count('a')) #Contando um caractere especifico
print(frase.find('é')) #Exibindo a posição do indice de um determinado elemento
print(frase[16]) #Lendo um caractere pelo seu indice
print(frase.split()) #Desmembrando uma string

#Substituindo elementos de uma string
frase = 'Porto Alegre é uma cidade brasileira.'
frase = frase.replace('Porto Alegre', 'Curitiba')
print(frase)

#Concatenando strings por meio de variaveis
mensagem = 'Seja bem-vindo '
usuario = 'Thiago'

base = mensagem + usuario
print(base)

#Concatenando diferentes tipos de dados em uma string
nome = 'Ana Clara'
idade = 12
print(f'{nome} tem {idade} anos')

aviso = 'Atenção, geradores entrarão em manutenção às: ' +str(22)+' horas!'
print(aviso)

#Convertendo caracteres maiusculo e minusculo
alerta = 'Risco de morte'
print(alerta.upper())
print(alerta.lower())

#Convertendo outro tipo de dados para string
num1 = str(2536)
print(type(num1))

#Removendo espaços no inicio e no fim de uma string
frase = '     Olá, você é o visitante n° 1000  '
print(frase)
print(frase.strip())

#Convertendo todas as iniciais das palavras para maiusculo
tema = 'O diagnostico por imagem como ferramenta para detecção de câncer'
tema = tema.title()
print(tema)

#Verificando se uma string é composta por letras e números
variavel = 'aaa44'
print(variavel.isalnum()) #Qualquer caractere alfanumerico
print(variavel.isalpha()) #Apenas letras
print(variavel.isdigit()) #Apenas números

#Pegando dados de uma string com intervalo definido pelo indice
frase = 'Porto Alegre é uma cidade Brasileira'
print(frase[26:37]) #intervalo especifico
print(frase[0:5]) #do inicio até uma posição
print(frase[-9]) #de trás para frente

#Criando uma lista simples
lista = ['Ana Clara', 'Carlos', 19.99,'Michele',1987]
print(lista)

#Pegando um elemento da lista pelo indice
print(lista[3])

#Descobrindo o número de indice de um elemento da lista
print(lista.index('Michele'))

#Descobrindo o número de elementos de uma lista
print(len(lista))

#Adicionando um novo elemento a lista fim da lista
lista.append('Paulo')

#Substituindo um elemento da lista em posição especifica
lista[2] = 'José'

#Adicionando um novo elemento na lista em posição especifica
lista.insert(2,'Thiago')

#Removendo um elemento de uma lista pelo indice
lista.remove(lista[5])

#Lista dentro de listas
cadastro = [1,2,3,['Ana','Maria','Paulo','Roberto']]
print(cadastro)
print(cadastro[4])

#Laço for em lista
repetir = 's'
fatura = []
total = 0

while repetir =='s':
    produto = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço: '))
    
    fatura.append([produto, preco])
    total+= preco
    
    repetir = input('Cadastrar mais algum item? (S ou N)').lower()

for i in fatura:
    print(i[0], ':', i[1])

print('O total da fatura é: ',total)

#Criando um conjunto numerico(set) em python
conjunto = {5,10,15,20}
print(type(conjunto))

#Operações entre conjunto
cj1 = {1,2,3,4,5}
cj2 = {1,3,5,7,9}
print(cj2 - cj1)

#União de conjuntos
uniao = cj1.union(cj2)
print(uniao)

#Interseção de dois conjuntos
uniao1 = cj1.intersection(cj2)
print(uniao1)

#operadores logicos em conjuntos
print(uniao == cj2)
print(uniao >= cj1)

#diferença entre conjuntos
c1 = {1,2,3,4,5} - {1,2}
print(c1)

print(cj1 - cj2)

#Pilhas
sequencia = [11,22,33,444]

pilha = []

for elemento in sequencia:
    pilha.append(elemento)

pilha.append(555)
pilha.pop()

while len(pilha) > 0:
    print(pilha)
    
    topo = pilha.pop()
    
    print(f'Objeto do topo da pilha: {topo}')
    
#Interpolação
nome = 'Maria'
exp = 33

print(f'Ola {nome}, queremos te parabenizar por seus {exp} anos em nossa empresa.')

#Operações dentro da mascara de substituição
idade = 30

print(f'{nome} tem 3 vezes minha idade, ela tem {3 * idade} anos!!')

#Sintaxe basica de um dicionario
dicionario = {'chave':'valor'}
print(dicionario)

#Adicionando novos elementos ao dicionario
dicionario = {'nome':'Paulo'}
print(dicionario)

dicionario['nome1'] = 'Veronica'
print(dicionario)

#Alterando o valor de uma chave do dicionario
dicionario = {'nome1':'Ana',
              'nome2': 'Carla',
              'nome3':'Maria'}
print(dicionario)

dicionario['nome2'] = 'Barbara'
print(dicionario)

#Acessando um elemento do dicionario
print(dicionario['nome1'])
print(dicionario['nome3'])

#Usando o contrutor de dicionario do Python
dicionario2 = dict(chave1 = 'valor da chave1',
                   chave2 = 'valor da chave2')
print(dicionario2)
print(type(dicionario2))

#Consultado as chaves de um dicionario
print(dicionario2.keys())

#Consultado valores de um dicionario
print(dicionario2.values())

#verificando se uma chave ou valor consta em um dicionario
d3 = {'1':'Ana',
      '2':'Maria',
      '3':'Paulo',
      '4':'Marcos'}

print(d3.get('5')) #Usando get
print('3' in d3) #Usando operador logico in
print('2' in d3.keys())
print(d3['2'] == 'Maria') #Usando operador logico ==

#Atualizando um elemento do dicionario
d4 = {'1':'A',
      '2':'B',
      '3':'C',
      '4':'D'}
print(d4)
d4.update({'2':'E'})
print(d4)

#Removendo um elemento do dicionario
print(d4)
del d4['4']
print(d4)

#Imprimindo somente chaves ou somente valores
print(d4.keys())
print(d4.values())

#Pesquisando o tamanho de um dicionario
print(len(d4))

#lendo as chaves ou valores por meio do laço for
for chaves in d4.keys(): #somente chaves
    print('Chaves: ',chaves)
    
for valor in d4.values(): #somente valores
    print('Chaves: ',valor)
    
for itens in d4.items(): #chaves e valores
    print('Chaves: ',itens)
    
for c,v in d4.items():
    print(f'Chaves: {c}, valores: {v}')
    
#Listas dentro de dicionarios
dict = {'almox':['Folha de oficio','Caneta','Grampeador'],
        'cozinha':['Café','Açúcar']}

print(dict['almox'][0])
print(dict['cozinha'][1])

#Removendo elementos de um dicionario
dicionario1 = {'Nome':'Fernando',
               'Idade':32,
               'Sexo':'Masculino',
               'Nacionalidade':'Brasileiro'}

dicionario1.pop('Nacionalidade')
print(dicionario1)

#Funções
#Sintaxe basica de uma função
def nome_da_funcao2(parâmetros):
    "corpo da função"

def minha_funcao():
    print('Minha primeira função presonalizada!!!')

variavel =minha_funcao()

#Definindo uma função sem parâmetros
def exibe_mensagem():
    print('Seja bem-vindo!')
    #poderia ser, dependendo do contexto > return 'Seja bem-vindo!!'

print(exibe_mensagem())
msg =exibe_mensagem()

#chamando a função
def mensagem():
    print('Seja bem-vindo!')

mensagem()

#Função interagindo com o usuario
usuario = input('Digite o seu nome:')
def mensagem(nome):
    print(f'Bem vindo {nome}!!')

print(mensagem(usuario))

#passando parametro ao chamar a função
def funcao(msg):
    print(msg)
    
mensagem = 'Boas Vindas!!!'
funcao(mensagem)

#----------------------------
def mensagem(nome):
    print(f'Bem vindo(a) {nome}!!')
usuario = mensagem('Fernando')
print(usuario)

#Função com dois ou mais parâmetros
def mesagem(nome, idade):
    print(f'{nome} tem {idade} anos...')
usuario = mensagem('Fernando',33)
print(usuario)

#definindo parâmetros padrão
def funcao(msg, nome='usuario'):
    print(f'{msg} para {nome}')
funcao('Olá')

#passando apenas um parametro e recebendo o resto padrão
def funcao(msg='Olá', nome='usuario', msg2='Seja bem vindo!!'):
    print(msg, nome, msg2)

funcao(nome='Fernando')

#input + funcao
def funcao(mensagem, nome):
    print(mensagem, nome)

funcao('Olá', input('Digite o seu nome: '))

#input + funcao 2
def funcao(msg='Ola', nome='usuario', msg2='Seja bem vindo!!'):
    nome = input('Digite o seu nome: ')
    print(msg, nome, msg2)

variavel = funcao()

#input + funcao 3
def funcao(msg='Ola', nome='usuario', msg2='Seja bem vindo!!'):
    return f'{msg} {nome}, {msg2}'

variavel = funcao(nome=input('Digite o seu nome: '))

print(variavel)

#Fazendo operações dentro de uma funcao
def soma(n1,n2):
    return f'O resultado da soma é: {n1 + n2}'

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
print(soma(n1, n2))

#operações compostas dentro de uma funcao
def aumento_perdentual(valor, percentual):
    return (valor + ((valor * percentual) / 100))

n1 = int(input('Digite o valor: '))
n2 = int(input('Você deseja somar quantos % ?'))
calculo = aumento_perdentual(n1,n2)

print(f'O valor final será: {calculo}')
print(f'O valor final será: R$ {round(calculo,2)}')
print(f'O valor final será: R$ {calculo:.2f}')

#Estruturas condicionais dentro de função 
# #1
def repetidor(msg):
    contador = 0
    while contador < 5:
        print(msg)
        contador += 1
        
print(repetidor(msg=input('Digite algo para ser repetido 5 vezes: ')))

#2
def divisao(n1, n2):
    if n1 == 0 or n2 == 0:
        return 'Operação inválida'
    return n1 / n2

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

print(f'O resultado da divisão é: {divisao(n1,n2)}')

#3
def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return f'FizzBuzz, {num} é divisível por 3 e 5'
    if num % 5 == 0:
        return f'Buzz, {num} é divisível por 5'
    if num % 3 == 0:
        return f'Fizz, {num} é divisível por 3'
    return num

print(fizz_buzz(num=int(input('Digite um número: '))))

#Função com argumentos externos
def funcao(*args):
    for parametro in args:
        print(parametro)
        
argumentos = ('nome', 'idade')

print(funcao(argumentos))

#Descompactando uma lista para que os elementos dela virem argumentos
lista = ['nome', 'idade', 'sexo', 'nacionalidade']

def funcao(*args):
    print('Informações necessárias:')
    print(args)
    
funcao(*lista)

#função com parâmetros baseados em *args e **kwargs
#supondo que está cadastrando senhas e usuários em um sistema
def funcao(*args, **kwargs):
    print(args)
    print(kwargs)
    
senhas_padrao = [12345, 11111, 54321]

funcao(*senhas_padrao, usuario='user', administrador='admin')

#buscando dados do modelo anterior
def funcao(*args, **kwargs):
    nome = kwargs['usuario']
    nome2 = kwargs['administrador']
    senha1 = args[0]
    senha2 = args[1]
    
    print(f'O usuário padrão é: {nome}')
    print(f'O administrador é: {nome2}')
    print(f'A senha padrão é: {senha1}')
    print(f'A senha alternativa é: {senha2}')
    
senhas_padrao = [12345,11111]

funcao(*senhas_padrao, usuario='user', administrador='admin')

#funcao que recebe outra funcao como parametro
def mestre(funcao):
    return funcao()

def msg_boas_vindas():
    return 'Seja muito bem vindo!!'

executa = mestre(msg_boas_vindas)
print(executa)

#Expressões lambda / funções vazias
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

variavel = lambda num1, num2: num1 * num2

print(variavel(num1,num2))

#Escopo global vc escopo local
variavel ='Paulo'
def funcao1():
    print(f'Print da variavel do escopo global {variavel}')

funcao1()

def funcao2():
    variavel2 = 'Maria'
    print(f'Print da variavel do escopo local {variavel2}')

funcao2()

#modificando uma variavel global dentro de uma funcao
num1 = 100
print(f'Variavel com seu valor inicial: {num1}')

def modificador():
    global num1
    num1 = 200
    print(f'Variavel alterada dentro da função: {num1}')
    
modificador()
print(f'Variavel atualizada pela função do modificador: {num1}')

#Sintaxe basica usual - programação orientada a objetos
#POO
# class Nome:
#     objetos de classe
#     métodos de classe
    
# class Nome:
#     método construtor
#     objetos de classe
#     métodos de classe

#Criando uma classe vazia
class Pessoa:
    pass

#Criando objetos(atributos da classe)
pessoa1 = Pessoa()

pessoa1.nome = 'Thamyres'
pessoa1.idade = 25

print(pessoa.nome)

#Criando funções(métodos de classe)
class Pessoa:
    def acao1(self):
        print('Ação 1 sendo executada....')
        
pessoa1 = Pessoa()
pessoa1.acao1()

#Criando uma classe com método construtor e objetos internos
class Pessoa:
    def __init__(self, nome, idade, sexo, altura):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.altura = altura
        
pessoa1 = Pessoa('Thamyres', 25, 'F', 1.72)

#print(pessoa1.nome, pessoa1.idade)
print(f'Bem vindo {pessoa1.nome}, parabens pelos seus {pessoa1.idade} anos!!')

#Mais de um método de classe 
class Pessoa:
    ano_atual = 2023
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def ano_nascimento(self):
        ano_nasc = self.ano_atual - self.idade
        print(f'Seu ano de nascimento é {ano_nasc}')
        
pessoa1 = Pessoa('Thamyres', 25)
print(pessoa1.ano_nascimento())

#Usando método de classe fora da classe
class Pessoa:
    ano_atual = 2023
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def ano_nasc(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)
        
pessoa1 = Pessoa.ano_nasc('Thamyres', 1998)
print(pessoa1.idade)

#Aula 179
