import Tabuleiro,Jogador

from IA import *
import time

ia = IA()

ti = time.clock()
ia.get_melhor_jogada(True)
print(time.clock() - ti)


