"""
07. front_back

Considere dividir uma string em duas metades.
Caso o comprimento seja par, a metade da frente e de trás tem o mesmo tamanho.
Caso o comprimento seja impar, o caracter extra fica na metade da frente.

Exemplo: 'abcde', a metade da frente é 'abc' e a de trás é 'de'.

Finalmente, dadas duas strings a e b, retorne uma string na forma:
a-frente + b-frente + a-trás + b-trás
"""

# da pra colocar um def dentro de outro? como passar as variavels pro interno ja que nao tem self?

def front_back(a, b):
    if len(a) % 2 != 0:
        positionA = int(len(a) / 2) + 1
        AparteA = a[:positionA]
        AparteB = a[positionA:]
    else:
        positionA = int(len(a) / 2)
        AparteA = a[:positionA]
        AparteB = a[positionA:]

    if len(b) % 2 != 0:
        positionB = int(len(b) / 2) + 1
        BparteA = b[:positionB]
        BparteB = b[positionB:]
    else:
        positionB = int(len(b) / 2)
        BparteA = b[:positionB]
        BparteB = b[positionB:]

    return AparteA+BparteA+AparteB+BparteB



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
    test(front_back, ('abcd', 'xy'), 'abxcdy')
    test(front_back, ('abcde', 'xyz'), 'abcxydez')
    test(front_back, ('Kitten', 'Donut'), 'KitDontenut')
