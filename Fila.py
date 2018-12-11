class Fila:

    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.__tamanho = 0
        self.__iterando = None

    class Nó:
        def __init__(self, conteudo):
            self.proximo = None
            self.conteudo = conteudo


    def __len__(self):
        return self.__tamanho

    def __repr__(self):
        return self.__str__()


    def __str__(self):
        formato = "["
        atual = self.primeiro
        for i in range(0, len(self)):
            formato += atual.conteudo.__repr__()
            if i < len(self) - 1:
                formato += ", "

            atual = atual.proximo
        formato += "]"
        return formato


    def __iter__(self):
        return self

    def __next__(self):
        if self.__iterando is None:
            self.__iterando = self.primeiro

        else:
            self.__iterando = self.__iterando.proximo

        if self.__iterando is not None:
            return self.__iterando.conteudo
        raise StopIteration

    def enfileirar(self, conteudo):
        novo = self.Nó(conteudo)

        if len(self) == 0:
            self.primeiro = novo
            self.ultimo = novo

        else:
            self.ultimo.proximo = novo
            self.ultimo = novo
        self.__tamanho += 1
        self.__iterando = None
        
    def desenfileirar(self):
        if self.__tamanho == 0:
            raise TypeError("Não existem elementos para desenfileirar")
        
        elif self.__tamanho == 1:
            self.primeiro = None
            self.ultimo = None
        
        elif self.__tamanho > 1:
            proximo = self.primeiro.proximo
            self.primeiro.proximo = None
            self.primeiro = proximo
            
        self.__tamanho -= 1
        self.__iterando = None
        


fila = Fila()

fila.enfileirar(1)
fila.enfileirar(2)
fila.enfileirar(3)
print(fila)

fila.desenfileirar()
fila.desenfileirar()
print(fila)


    
    
    


