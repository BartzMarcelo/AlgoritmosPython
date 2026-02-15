# # # # numbers=[10, 5, 7, 2, 1]

# # # # # number[0] = 111
# # # # # print(number)

# # # # print("Conteúdos originaisnda lista: ", numbers)
# # # # numbers[0]=111
# # # # print("\nConteúdos modificadosda lista: ", numbers)

# # # # numbers[1]= numbers[4]
# # # # print("\nConteúdos modificadosda lista: ", numbers)

# # # # print("\n list lenght: ", len(numbers))

# # # # print("\n")

# # # # del numbers[1]
# # # # print(len(numbers))
# # # # print(numbers)

# # # # print("\n")

# # # # print(numbers[-1])
# # # # print(numbers[-2])

# # # # print("\n")

# # # # # hat_list = [1, 2, 3, 4, 5]  # Esta é a lista inicial

# # # # # hat_list[2]= int(input("Substitua o número do meio da lista por outro número inteiro: "))
# # # # # print(hat_list)

# # # # # print("\n")

# # # # print(numbers)
# # # # print("Quantidade de elementos na lista: ", len(numbers))
# # # # numbers.append(4)
# # # # print(numbers)
# # # # print(len(numbers))

# # # # print("\n")

# # # # numbers.insert(0, 222)
# # # # print(numbers)
# # # # print(len(numbers))

# # # # print("\n")

# # # # numbers.insert(1, 333)
# # # # print(numbers)
# # # # print(len(numbers))

# # # # print("\n")

# # # # my_list = []  # Criando uma lista vazia.
 
# # # # for i in range(5):
# # # #     my_list.insert(0, i + 1)
 
# # # # print(my_list)

# # # # print("\n")

# # # # my_list = [10, 1, 8, 3, 5]

# # # # total = 0


# # # # for i in range(len(my_list)):

# # # #   total += my_list[i]

# # # # print(total)


# # # # my_list = [10, 1, 8, 3, 5]
# # # # total = 0
 
# # # # for i in my_list:
# # # #     total += i
 
# # # # print(total)


# # # # list_1 = [1]
# # # # list_2 = list_1
# # # # list_1 [0] = 2
# # # # print(list_2)

# # # # print("\n")

# # # # list_1 = [1]
# # # # list_2 = list_1[:]
# # # # list_1[0] = 2
# # # # print(list_2) 

# # # # print("\n")

# # # # my_list = [10, 8, 6, 4, 2]
# # # # new_list = my_list[-1:1]
# # # # print(new_list)
 
 
# # # # print("\n") 

# # # # my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
# # # # largest = my_list[0]

# # # # for i in range(1, len(my_list)):
# # # #     if my_list[i] > largest:
# # # #         largest = my_list[i]

# # # # print(largest)

# # # # temps = [[0.0 for h in range(24)] for d in range(31)]
# # # # #
# # # # # A matriz é magicamente atualizada aqui.
# # # # #
 
# # # # highest = -100.0
 
# # # # for day in temps:
# # # #     for temp in day:
# # # #         if temp > highest:
# # # #             highest = temp
 
# # # # print("A maior temperatura foi:", highest)
# # # # nums = [1, 2, 3]
# # # def message():
# # #     print("Entre um valor: ")
 
# # # print("Começamos aqui.")
# # # message()

# # # print("terminamos aqui.")



# # # def message(number):
# # #  print("Digite um número:", number)

# # # message(1)

# # # def message(number):
# # #     print("Digite um número:", number)
 
# # # number = 1234
# # # message(1)
# # # print(number)
 

# # def introduction(first_name, last_name):
# #     print("Olá meu nome é", first_name, last_name)
 
# # introduction("Skywalker", "Luke")
# # introduction("Quick", "Jesse")
# # introduction("Kent", "Clark")
 
# # def introduction(first_name, last_name):
# #     print("Olá meu nome é", first_name, last_name)
 
# # introduction(first_name = "James", last_name = "Bond")
# # introduction(last_name = "Skywalker", first_name = "Luke")

 
# def happy_new_year(wishes = True):
#     print("Três...")
#     print("Duas...")
#     print("Uma...")
#     if not wishes:
#         return
 
#     print("Feliz Ano Novo!")


# happy_new_year()

# def boring_function():
#     return 123
 
# x = boring_function()
 
# print("A aborrecimento_função retornou seu resultado. Isso é:", x)

# def boring_function():
#     print("'Modo de tédio' ON.")
#     return 123
 
# print("Esta lição é interessante!")
# boring_function()
# print("Essa aula é chata...")
 
def list_sum(lst):
    s = 0
 
    for elem in lst:
        s += elem
 
    return s

print(list_sum([5, 4, 3]))

def strange_list_fun(n):
 strange_list = []
 
 for i in range(0, n):
 strange_list.insert(0, i)
 
 return strange_list

print(strange_list_fun(5))

print("Olá, Mundo!)