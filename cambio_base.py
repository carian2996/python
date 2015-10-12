# Ian / Jessica
# 23/09/15
# Este script tomo un numero entero positivo y genera su equivalente en base 2

base = int(raw_input('Escribe 1 si deseas convertir un numero en base 10 a base 2. \nEscribe 2 si deseas convertir un numero en base 2 a base 10: '))

if base == 1:

	num10 = int(raw_input('Ingrese un numero entero positivo en base 10: '))
	num = num10

	bin = str(num10 % 2)
	
	while num10 > 1:
		num10 = num10 / 2
		bin = bin + str(num10 % 2)
	
	bin = bin[::-1]
	
	print 'El numero', num, 'se escribe', bin, 'en base 2'

elif base == 2:

	num = raw_input('Ingrese un en base 2: ')
	num2 = num
	num2 = num2[::-1]

	num2 = list(num2)
	num2 = map(int, num2)

	n = len(num2)
	ten = []

	for i in range(n):
		ten.append(num2[i] * 2**i)

	print 'El numero', num, 'se escribe', sum(ten), 'en base 10'

else:

	print "Base invalida"
