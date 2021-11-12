"""
11. remove_adjacent

Dada uma lista de números, retorne uma lista onde todos elementos
adjacentes iguais são reduzidos a um único elemento.

Exemplo: [1, 2, 2, 3]
Irá retornar: [1, 2, 3]
"""
def remove_adjacent(nums):
    list1 = []
    list2 = []
    final = []
    for pos1 in enumerate(nums):
        list1.append(pos1)
    for pos2, num2 in enumerate(nums):
        pos_final = pos2 + 1
        new_tupple = (pos_final, num2)
        list2.append(new_tupple)

    for i in range(len(nums)):
        if list1[i] == list2[i-1]:
            continue
        else:
            final_element = list1[i]
            final.append(final_element[1])

    return final


#
# def remove_adjacent(nums):
#     pos1 = 0
#     pos2 = 0
#     count = 0
#     list1 = []
#     list2 = []
#     final = []
#     for pos1 in enumerate(nums):
#         list1.append(pos1)
#     for pos2,num2 in enumerate(nums):
#         posf = pos2 + 1
#         tup = (posf,num2)
#         list2.append(tup)
#
#     for i in range(len(nums)):
#
#         element = list2[i]
#
#         #print(list1[i], element)
#
#         if list1[i] == list2[i-1]:  # ou !=
#             #print("equal") #HERE!!!
#             continue
#         else:
#             final_element = list1[i]
#             #print("different", final_element[1]) #HERE!!!
#
#             final.append(final_element[1])
#         #print(i, (len(list1)))
#         #print(element[0], i, list1[i], list2[i], list2[i-1])
#         # while count != (len(list1)): # fix this!
#         #     count += 1
#         #     ii = i + 1
#         #     #print("here1")
#         #     print(ii, list1[ii],list2[ii-1] )
#         #     if list1[i] == list2[i-1]: # ou !=
#         #         print("equal")
#         #     else:
#         #         print("different")
#         #         final.append(element[i])
#     return final
#
#






# import re
# def remove_adjacent(nums):
#     final_list = []
#     dis_list = []
#     for num in nums:
#         num1 = num
#         #print(num1)
#         for numbla in nums:
#             num2 = numbla
#             #print(num1, numbla)
#             if num1 != numbla:
#                 continue
#             else:
#                 final_list.append(num1) # numbla
#     for num2 in nums:
#         num22 = num2
#
#     return final_list

# newnum = re.match(r'{num}?', nums)
        # print (newnum)

# remove_adjacent([1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7])


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(remove_adjacent, [1, 2, 2, 3], [1, 2, 3])
    test(remove_adjacent, [2, 2, 3, 3, 3], [2, 3])
    test(remove_adjacent, [], [])
    test(remove_adjacent, [2, 2, 3, 3, 3, 2, 2], [2, 3, 2])
