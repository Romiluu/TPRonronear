from Benito import Benito
from Terminator import Terminator
from Tweet import Tweet
from Wally import Wally

ingresoDatos = True;
benito = Benito();
wally = Wally();
terminator = Terminator();


def tweet():
    if len(tw.split()) <= 15:
        twitter = Tweet(tw, usuario)
        benito.agregarTweet(twitter)
        terminator.agregarTweet(twitter)
        wally.agregarTweet(twitter)
    else:
        print('El límite del twit es de 15 palabras')


def ingresarDatos():
    ingresoDatos = True if inputIngDatos == 'Y' else False;
    if (ingresoDatos == False):
        benito.mostrarTweets()
        terminator.mostrarTweets()
        wally.responderTweet()
        exit()


while (ingresoDatos == True):
    usuario = input("Usuario: ");
    tw = input("Tweet: ");
    tweet();
    inputIngDatos = input("Desea ingresar un nuevo tweet?(Y/N): ");
    ingresarDatos();


