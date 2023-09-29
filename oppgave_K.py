
from oppgave_G import beregn_trend
from lister_for_del_1 import temperaturer, temperaturer_tidspunkter

def analyser_trend_i_temperatur():
    # bruker funksjon fra oppgave G, på lista gitt
    a, b = beregn_trend(temperaturer_tidspunkter, temperaturer)
    
    # printer trend
    if a > 0:
        print("Trenden er stigende.")
    elif a < 0:
        print("Trenden er synkende.")
    else:
        print("Det er ingen trend.")

# starter funksjonen
analyser_trend_i_temperatur()
