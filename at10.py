def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        fib = [1, 1]
        for i in range(2, n):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib

esimo_termo = int(input("Digite o quantos numeros da sequencia de fibonacci sejam gerados  "))
resultado_fibonacci = fibonacci(esimo_termo)
print(f"Série de Fibonacci até o {esimo_termo}º termo: {resultado_fibonacci}")
#uns soq mais deus trabalho pra entender savio bem eleborado viu