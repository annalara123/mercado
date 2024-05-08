import psycopg2

def conectarDB():
    return conectar_localBD()

def conectar_localBD():
    con = psycopg2.connect(
        host= 'localhost',
        database= 'projeto_de_rene',
        user= 'postgres',
        password= '12345'
    )
    return con

def conectar_cloudBD():
    con = psycopg2.connect(
        host= 'dpg-cot4sv021fec73fr6c1g-a',
        database= 'projeto_de_rene',
        user= 'projeto_de_rene_user',
        password= 'g1NOLgRqHeS5HobfXbuoNEVecRdFLPgN'
    )
    return con

def conectar_db():
    return conectar_cloudBD()