def get_summ(one, two, delimiter='&'):
    one = str(one)
    two = str(two)
    return f'{one}{delimiter}{two}'

rez = get_summ("Learn", "python")
print(rez)
print(f'rez in caps: {rez.upper()}')