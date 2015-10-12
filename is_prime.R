is_prime <- function(n){
  
  if (n <= 0){
    print("Ingrese un numero mayor a 1")
    break
  }
  else{
    if (n <= 3) print("Si es primo")
    else{
      i = 2
      while (i <= floor(n**0.5)){
        if ((n %% i) == 0){
          print("No es primo")
          break
        }
        i = i + 1
      }
      print("Es primo")
    }
  } 
}