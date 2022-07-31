from filme import Filme
from serie import Serie
from playlist import Playlist



# ------------------- FILMES ------------------------
vingadores  = Filme('vingadores - gerra infinita', 2018, 160)
tmep        = Filme('Todo mundo em Panico', 1999, 100)

vingadores.dar_likes()
tmep.dar_likes()



# ---------------- SERIES --------------------------
atlanta   = Serie('atlanta', 2018, 2)
demolidor = Serie('demolidor', 2016, 2)

atlanta.dar_likes()
atlanta.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()



# ---------------- Playlist --------------------------
filmes_e_series         = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana  =  Playlist('fim de semana', filmes_e_series)

print(f'Tamanho da playlist: {len(playlist_fim_de_semana)}')
for programa in playlist_fim_de_semana:
  print("-----------------")
  print(programa)