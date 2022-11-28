import re

class AnalisadorLexico:
    # Token linha
    lin_num = 1

    def cria_token(self, code):
        regras = [
            ('INT', r'🔢'),             # Tipo Inteiro
            ('STR', r'🔢'),             # Tipo String
            ('BOOL', r'🔢'),            # Tipo Booleano
            ('TRUE', r'🔢'),            # Verdadeiro
            ('FALSE', r'🔢'),           # Falso
            ('IF', r'🤨'),              # Se
            ('ELSE', r'😣'),            # Senão
            ('WHILE', r'⏰'),           # Enquanto
            ('FOR', r'😵'),             # Para
            ('SWITCH', r'🧐'),          # Escolha
            ('CASE', r'🔎'),            # Caso
            ('BREAK', r'👊'),           # Quebra
            ('CONT', r'🗿'),             # Continua
            ('TRY', r'🤔'),             # Tente
            ('CATCH', r'⛔'),           # Pegue
            ('RETURN', r'🔁'),          # Retorne
            ('INPUT', r'📝'),           # Entrada
            ('SLEEP', r'😴'),           # Dorme
            ('PRINT', r'🖨️'),           # Imprima
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
            ('TAB', r'➡️'),           # Entrada
            ('ESPACO', r'[ \t]+'),        # Espaço
            ('N_IDEN', r'.'),         # Outros caracteres
        ]

        tokens_join = '|'.join('(?P<%s>%s)' % x for x in regras)
        comeco_linha = 0

        # Lista de saída para o programa principal.
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
                    # Imprime a informação dos tokens encontrados.
                    print('Token = {0}, Lexema = \'{1}\', Linha = {2}, Coluna = {3}'.format(tipo_token, lexema_token, self.lin_num, col))

        return token, lexema, linha, coluna
