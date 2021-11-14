"""
12. linear_merge

Dada duas listas ordenadas em ordem crescente, crie e retorne uma lista
com a combinação das duas listas, também em ordem crescente. Você pode
modificar as listas recebidas.

A sua solução deve rodar em tempo linear, ou seja, deve fazer uma
única passagem em cada uma das listas.
"""

def linear_merge(list1, list2):
    finallist = []
    ia, ib = 0, 0

    for ia, na in enumerate(list1):
        if ia






    return finallist


# def linear_merge(list1, list2):
    # if list1[-1] > list2[-1]:
    #     biglist = list1
    #     smalllist = list2
    # else:
    #     biglist = list2
    #     smalllist = list1
    # finallist = []
    # ia = 0
    # ib = 0
    # na = biglist[ia]
    # nb = smalllist[ib]
    # ind = 0
    # while ind < len(list1+list2):
    #
    #     if ia <= ib and na <= nb:
    #         ib += 1
    #         if ia <= ib and na <= nb:
    #             ib += 1
    #             if (ia <= ib and na <= nb) or (ia or ib == None):
    #                 finallist.append(na)
    #                 ia += 1
    #                 ib = 0
    #             else:
    #                 print("error case a1")
    #
    #
    #
    #         elif ia <= ib and na >= nb:
    #             if (ia <= ib and na >= nb) or (ia or ib == None):
    #                 finallist.append(nb)
    #                 ia += 1
    #                 ib = 0
    #             else:
    #                 print("error case a1")
    #         elif ia >= ib and na <= nb:
    #             if (ia >= ib and na <= nb) or (ia or ib == None):
    #                 finallist.append(na)
    #                 ia += 1
    #                 ib = 0
    #             else:
    #                 print("error case a1")
    #         elif ia >= ib and na >= nb:
    #             if (ia >= ib and na >= nb) or (ia or ib == None):
    #                 finallist.append(nb)
    #                 ia += 1
    #                 ib = 0
    #             else:
    #                 print("error case a1")
    #
    #
    #     elif ia <= ib and na >= nb:
    #         ib += 1
    #         if ia <= ib and na >= nb:
    #             ib += 1
    #             if (ia <= ib and na >= nb) or (ia or ib == None):
    #                 finallist.append(nb)
    #                 ia += 1
    #                 ib = 0
    #             else:
    #                 print("error case b1")
    #
    #
    #         elif ia <= ib and na >= nb:
    #             if (ia <= ib and na >= nb) or (ia or ib == None):
    #                 finallist.append(nb)
    #                 ia += 1
    #                 ib = 0
    #             else:
    #                 print("error case a1")
    #         elif ia >= ib and na <= nb:
    #             if (ia >= ib and na <= nb) or (ia or ib == None):
    #                 finallist.append(na)
    #                 ia += 1
    #                 ib = 0
    #             else:
    #                 print("error case a1")
    #         elif ia >= ib and na >= nb:
    #             if (ia >= ib and na >= nb) or (ia or ib == None):
    #                 finallist.append(nb)
    #                 ia += 1
    #                 ib = 0
    #             else:
    #                 print("error case a1")
    #
    #
    #
    #
    #     elif ia >= ib and na <= nb:
    #         ib += 1
    #         if ia >= ib and na <= nb:
    #             ib += 1
    #             if (ia >= ib and na <= nb) or (ia or ib == None):
    #                 finallist.append(nb)
    #                 ia += 1
    #                 ib = 0
    #             else:
    #                 print("error")
    #
    #
    #
    #
    #     elif ia >= ib and na >= nb:
    #         ib += 1
    #         if ia >= ib and na >= nb:
    #             ib += 1
    #             if (ia >= ib and na >= nb) or (ia or ib == None):
    #                 finallist.append(nb)
    #                 ia += 1
    #                 ib = 0
    #             else:
    #                 print("error")
    #
    #
    #
    #         finallist.append(nb)
    #         ia += 1
    #         ib = 0
    #
    #
    #
    #
    #
    #
    #
    #     ind += 1
    # return finallist



    # if list1[-1] > list2[-1]:
    #     biglist = list1
    #     smalllist = list2
    # else:
    #     biglist = list2
    #     smalllist = list1
    #
    # for i, n in enumerate(biglist):
    #     ii = i - 1
    #     print(i, ii, n, biglist[ii])
    #     if i <= ii and n <= (biglist[ii]):
    #         i += 1
    #         #ii += 1
    #         if i <= ii and n <= biglist[ii]:
    #             final_list.append(n)
    #         elif i <= ii and n >= biglist[ii]:
    #             final_list.append(biglist[ii])
    #     elif ii <= i and biglist[ii] <= n:
    #         final_list.append(biglist[ii])
    #     elif i <= ii and n >= biglist[ii]:
    #         final_list.append(biglist[ii])
    #     elif ii <= i and biglist[ii] >= n:
    #         final_list.append(n)
    #     else:
    #         print("fail")
    # return final_list









# def linear_merge(list1, list2):
#     count = 0
#     finallist = [list1+list2]
#     def equalFunc(toprocess):
#         newlist = []
#         count = 0
#         #print(toprocess[0])
#         for pp, i in enumerate(toprocess):
#
#             print(pp)
#             count += 1
#             #print(i)
#             inn = count - 1
#             inn2 = count
#             position1 = i[inn]
#             position2 = i[inn2]
#             #print(position1)
#
#             if position1 < position2: #mudar de ordem //  manter ordem
#                 newlist.append(position1)
#                 newlist.append(position2)
#             else:
#                 newlist.append(position2)
#                 newlist.append(position1)
#
#
#         return newlist
#
#     equalFunc(finallist)
#
#     # def finaldef(arg1, arg2):
#     #     for i in range(3):
#     #         if arg1[i] < arg2 [i]:
#     #             finallist.append(arg1[i])
#     #         elif arg1[i] > arg2[i]:
#     #             finallist.append(arg2[i])
#     #     return finallist
#
#     #equalFunc(list1, list2)
#     # finaldef(list1, list2)
#
#     return finallist[0]

#------------------------------------------
# def linear_merge(list1, list2):
#     for i in list2:
#         list1.append(i)
#     list1.sort()
#
#     return list1

# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}{in_!r} retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(linear_merge, (['aa', 'xx', 'zz'], ['bb', 'cc']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge, (['aa', 'xx'], ['bb', 'cc', 'zz']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge, (['aa', 'aa'], ['aa', 'bb', 'bb']),
         ['aa', 'aa', 'aa', 'bb', 'bb'])
