import re

class AnalisadorLexico:
    # Token linha
    lin_num = 1

    def cria_token(self, code):
        regras = [
            ('INT', r'π’'),             # Tipo Inteiro
            ('STR', r'π’'),             # Tipo String
            ('BOOL', r'π’'),            # Tipo Booleano
            ('TRUE', r'π’'),            # Verdadeiro
            ('FALSE', r'π’'),           # Falso
            ('IF', r'π€¨'),              # Se
            ('ELSE', r'π£'),            # SenΓ£o
            ('WHILE', r'β°'),           # Enquanto
            ('FOR', r'π΅'),             # Para
            ('SWITCH', r'π§'),          # Escolha
            ('CASE', r'π'),            # Caso
            ('BREAK', r'π'),           # Quebra
            ('CONT', r'πΏ'),             # Continua
            ('TRY', r'π€'),             # Tente
            ('CATCH', r'β'),           # Pegue
            ('RETURN', r'π'),          # Retorne
            ('INPUT', r'π'),           # Entrada
            ('SLEEP', r'π΄'),           # Dorme
            ('PRINT', r'π¨οΈ'),           # Imprima
            ('ABRE_PAR', r'\('),        # (
            ('FECHA_PAR', r'\)'),        # )
            ('ABRE_CHAVES', r'\{'),          # {
            ('FECHA_CHAVES', r'\}'),          # }
            ('VIRG', r','),            # ,
            ('P_VIRG', r';'),           # ;
            ('DOIS_PONTOS', r':'),           # :
            ('IGUAL', r'=='),              # ==
            ('DIF', r'!='),              # !=
            ('ME_IGUAL', r'<='),              # <=
            ('MA_IGUAL', r'>='),              # >=
            ('OU', r'\|\|'),            # ||
            ('ee', r'&&'),             # &&
            ('ATRIB', r'\='),            # =
            ('MENOR', r'<'),               # <
            ('MAIOR', r'>'),               # >
            ('MAIS', r'\+'),            # +
            ('MENOS', r'-'),            # -
            ('MULT', r'\*'),            # *
            ('DIV', r'\/'),             # /
            ('ID', r'[a-zA-Z]\w*'),     # Identificadores
            ('VALOR_STR', r'"(?:[^"]|"")*"'),     # Identificadores
            ('CONST_INT', r'\d(\d)*'),  # Inteiros
            ('NOVALINHA', r'\n'),         # Nova linha
            ('TAB', r'β‘οΈ'),           # Entrada
            ('ESPACO', r'[ \t]+'),        # EspaΓ§o
            ('N_IDEN', r'.'),         # Outros caracteres
        ]

        tokens_join = '|'.join('(?P<%s>%s)' % x for x in regras)
        comeco_linha = 0

        # Lista de saΓ­da para o programa principal.
        token = []
        lexema = []
        linha = []
        coluna = []

        # Analisa o codigo para encontrar os lexemas e os respectivos tokens.
        for m in re.finditer(tokens_join, code):
            tipo_token = m.lastgroup
            lexema_token = m.group(tipo_token)

            if tipo_token == 'NOVALINHA':
                comeco_linha = m.end()
                self.lin_num += 1
            elif tipo_token == 'ESPACO':
                continue
            elif tipo_token == 'N_IDEN':
                raise RuntimeError('%r inesperado na linha %d' % (lexema_token, self.lin_num))
            else:
                    col = m.start() - comeco_linha
                    coluna.append(col)
                    token.append(tipo_token)
                    lexema.append(lexema_token)
                    linha.append(self.lin_num)
                    # Imprime a informaΓ§Γ£o dos tokens encontrados.
                    print('Token = {0}, Lexema = \'{1}\', Linha = {2}, Coluna = {3}'.format(tipo_token, lexema_token, self.lin_num, col))

        return token, lexema, linha, coluna
