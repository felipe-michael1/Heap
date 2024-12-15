#Class heap para verificar o valor máximo de um número

class Heap:
    def __init__(self, array, number):
        self.array = array
        self.number = number

    def seleciona_ultimo(self):
        return max(self.array)

    def remove_ultimo(self):
        valor_maximo = self.seleciona_ultimo()
        return [num for num in self.array if num != valor_maximo]

    def insere_valores(self):
        self.array.append(self.number)
        return self.array

# Exemplo de uso
array = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]
number = 89
retorna_heap = Heap(array, number)

print("Array após inserção do novo valor:", retorna_heap.insere_valores())
