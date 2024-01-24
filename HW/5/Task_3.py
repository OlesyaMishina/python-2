# Создайте функцию генератор чисел Фибоначчи

def fibonacci (number: int) -> (iter, int):
    fibo_subsequence = [0, 1, 1]
    count = 0
    while count <number:
        while len(fibo_subsequence)<number:
            fibo_subsequence.append(sum(fibo_subsequence[-2:]))

        yield fibo_subsequence[count]
        count +=1

print(*(fibonacci(8)))
