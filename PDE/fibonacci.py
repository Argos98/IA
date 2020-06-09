import sys
def fibonacci_recursive(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n-2)

def fibonacci_dinamico (n, memo = {}):

    if n == 0 or n== 1:
        return 1

    try: 
        return memo[n]

    except KeyError:
        resultado = fibonacci_dinamico(n-1) + fibonacci_dinamico(n-2)
        
        memo[n]= resultado

        return resultado


if __name__ == "__main__":
    sys.setrecursionlimit(10002)
    n = int(input('escoje un numero:'))   

    resultado = fibonacci_dinamico(n)

    print(resultado)
