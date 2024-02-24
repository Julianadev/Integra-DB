import os
import pandas as pd
import sqlite3

def main(nome_db, nome_tabela):
    conn = sqlite3.connect(f'{nome_db}')
    if conn is not None:
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM {nome_tabela}')
        rows = cur.fetchall()
        for row in rows:
            print(row)
        conn.close()

def conecta_db():
    try:
        nome_db = input('Digite o nome para o seu banco de dados: ')
        if not nome_db.endswith('db'):
            nome_db += '.db'
        nome_tabela = input('Digite o nome para a tabela: ')
        conn = sqlite3.connect(f'{nome_db}')
        if conn is not None:
            if os.path.exists(f'{nome_tabela}.csv'):
                df = pd.read_csv(f'{nome_tabela}.csv')
                df.to_sql(f'{nome_tabela}', conn, if_exists='replace')
                print(df.loc[len(df.index) -1])
            else:
                print(f'O arquivo {nome_tabela} foi encontrado')
        else:
            print('Por favor digite um novo para o banco de dados.')
    except ConnectionError as e:
        print('Erro de conexão', e)
    visualizar = input('Deseja visualizar a tabela? S/N ').upper()
    if visualizar == 'S':
        main(nome_db, nome_tabela)
    else:
        print('Encerrando o programa')

if __name__ == '__main__':
    conecta_db()


