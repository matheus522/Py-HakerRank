"""
    Um belo dia, um número finito de turistas vem se hospedar no hotel.
    Os turistas são compostos por:
 >>Um capitão.
 >>Um grupo desconhecido de famílias composto por K membros por grupo onde K ≠ 1.

 O capitão recebeu um quarto separado e os demais receberam um quarto por grupo.

    O Sr. Anant tem uma lista não ordenada de entradas de quartos organizadas aleatoriamente.
    A lista consiste nos números dos quartos para todos os turistas.
    Os números dos quartos aparecerão K vezes por grupo, exceto no quarto do Capitão.

    O Sr. Anant precisa de você para ajudá-lo a encontrar o número do quarto do Capitão.
    O número total de turistas ou o número total de grupos de famílias não é conhecido por você.
    Você só sabe o valor de K e a lista de números do quarto.

    Formato de entrada

    A primeira linha consiste em um número inteiro, K, o tamanho de cada grupo.
    A segunda linha contém os elementos não ordenados da lista de números de quarto.
"""

# Passo 1 - Pegar valpor de "Tripulantes"
k = int(input())

#Criar uma lista dos Numeros dos quartos
room_number_list = list(map(int, input().split()))

#Sum() -> Soma valores da lista
#Set() -> organiza a lista
captain_room_number = (sum(set(room_number_list)) * k - sum(room_number_list)) // (k - 1)
print(captain_room_number)

'''
k -> 4
room_number_list -> 1 2 3

1. Ordena lista
1 2 3

2. soma valores da lista
1 + 2 + 3 = 6

#por enquanto
(6 * 4 - 6 )// 3
24 - 6
18 // 3
6
* 
'''