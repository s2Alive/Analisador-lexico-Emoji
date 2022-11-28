from Buffer import Buffer
from AnalisadorLexico import AnalisadorLexico

if __name__ == '__main__':
    Buffer = Buffer()
    Analisador = AnalisadorLexico()

    # Lista para toda lista retornada da lista de tokens.
    token = []
    lexema = []
    linha = []
    coluna = []

    # Tokenização e recarregamento do buffer.
    for i in Buffer.carregar_buffer():
        t, lex, lin, col = Analisador.cria_token(i)
        token += t
        lexema += lex
        linha += lin
        coluna += col

    print('\nReconhecimento de tokens: ', token)

