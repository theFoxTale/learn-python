a = 3
b = 4
c = a + b
print('+: ' + str(c))

c = a - b
print('-: ' + str(c))

c = a * b
print(f'*: {c}')

c = a ** b
print('^: {dInt}'.format(dInt=c))

c = a / b
print('/: {}'.format(c))

m = "Hello"
n = "world"
d = '{} {}!'.format(m, n)
print(d)

dd = len(d)
print(f'Длина строки: {dd}.')

f = d.upper()
print(f)

g = d.lower()
print(g)

h = g.capitalize()
print(h)

trimStr = '  Вася   '
print(f'Строка: {trimStr}, длина строки: {len(trimStr)};')
trimmedStr = trimStr.strip()
print(f'Строка: {trimmedStr}, длина строки: {len(trimmedStr)};')

rStr = "Привет, мир!"
replaceStr = rStr.replace('мир', 'Python')
print(replaceStr)

siteTxt = 'learn.python.org'
print(siteTxt.split('.'))

txt = "Привет   я робот  "
print(txt.split())

err = 0
print(f'0 is None: {err is None}')
err = None
print(err is None)

print(f'Text datatype: {type(txt)}')
print(f'None datatype: {type(err)}')

k = 'Привет!'
print(f'Bool от привет: {bool(k)}')
print(f'Bool от 0: {bool(0)}')
print(f'Bool от None: {bool(None)}')
print(f'Bool от " ": {bool(" ")}')
print(f'Bool от "": {bool("")}')