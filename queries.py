import pandas as pd
#Jogador de cada time
def jogador_time(mydb):
    query = """
        SELECT time.nome AS clube,jogador.nome AS jogador, jogador.gols AS gols
        FROM time JOIN jogador 
        ON time.id_time = jogador.id_time ORDER BY gols;
    """
    df = pd.read_sql(query,mydb)
    return df

#Países e suas quantidades de times
def time_pais(mydb):
    query = """
        SELECT pais,count(*) AS quantidade, group_concat(nome) AS clubes
        FROM time GROUP BY pais ORDER BY quantidade DESC;
    """
    df = pd.read_sql(query,mydb)
    return df

#Total de gols por time
def gol_time(mydb):
    query = """
        SELECT time.nome, SUM(jogador.gols) AS gols_marcados 
        FROM time JOIN jogador ON time.id_time = jogador.id_time
        GROUP BY jogador.id_time ORDER BY gols_marcados DESC;
    """
    df = pd.read_sql(query,mydb)
    return df

#Artilheiros
def artilheiro(mydb):
    query = """
        SELECT time.nome AS clube, jogador.nome AS jogador, jogador.gols AS gols_no_mata_mata 
        FROM time JOIN jogador ON jogador.id_time = time.id_time 
        WHERE gols>2 ORDER BY gols DESC;
    """
    df = pd.read_sql(query,mydb)
    return df

#Média de gols por fase
def media_gol(mydb):
    query = """
        SELECT DISTINCT fase, AVG(gols_casa + gols_fora) AS media_de_gol 
        FROM partida 
        GROUP BY fase;
    """
    df = pd.read_sql(query,mydb)
    return df

#Gols como mandante
def gol_mandante(mydb):
    query = """
        SELECT time_casa.nome AS clube, SUM(partida.gols_casa) AS gols_como_mandante
        FROM time AS time_casa JOIN partida ON time_casa.id_time = partida.id_casa 
        GROUP BY time_casa.nome
        ORDER BY gols_como_mandante DESC;
    """
    df = pd.read_sql(query,mydb)
    return df

def gol_visitante(mydb):
    query = """
    SELECT time_fora.nome AS clube, SUM(partida.gols_fora) AS gols_como_visitante
    FROM time AS time_fora JOIN partida ON time_fora.id_time = partida.id_fora
    GROUP BY time_fora.nome
    ORDER BY gols_como_visitante DESC;
    """
    df = pd.read_sql(query,mydb)
    return df

def empates(mydb):
    query = """
    SELECT partida.fase,
	    CONCAT(time_casa.nome,' X ',time_fora.nome) AS jogo,
	    CONCAT(partida.gols_casa,' X ',partida.gols_fora) AS placar,
	    partida.estadio 
    FROM partida 
        JOIN time AS time_casa ON partida.id_casa = time_casa.id_time 
        JOIN time AS time_fora ON partida.id_fora = time_fora.id_time
    WHERE gols_casa = gols_fora;
    """
    df = pd.read_sql(query,mydb)
    return df

