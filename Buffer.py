class Buffer:
    def carregar_buffer(self):        

        arq = open('Programa.emoji', 'r', encoding='utf-8')
        texto = arq.readline()

        buffer = []
        cont = 1

        # O tamanho do buffer pode aumentar mudando o contador
        while texto != "":
            buffer.append(texto)
            texto = arq.readline()
            cont += 1

            if cont == 10 or texto == '':
                # Retorna um buffer completo
                buf = ''.join(buffer)
                cont = 1
                yield buf

                # Reseta o buffer
                buffer = []

        arq.close()
