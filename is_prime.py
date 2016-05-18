import time

n_input = raw_input("Ingrese un numero: ")


n_input = int(n_input)
start_time = time.time()
if n_input <= 0:
	print "Ingrese un numero mayor a 1"
else: 
	if n_input <= 3:
		print "Si es primo"
	else:
		i = 2
		while i <= int(n_input**0.5):
			if (n_input % i) == 0:
				print "No es primo"
				print("--- %s seconds ---" % (time.time() - start_time))
				quit()
			i = i + 1
		print "Es primo"
		print("--- %s seconds ---" % (time.time() - start_time))