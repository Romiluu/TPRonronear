

class Benito:
    def __init__(self):
        self.listaNegra = ['nieve', 'perico', 'piedra']
        self.tweetDenunciados = []

    def agregarTweet(self, tweet):
        for palabra in self.listaNegra:
            if palabra in tweet.texto.split():
                self.tweetDenunciados.append(tweet)
                break;

    def mostrarTweets(self):
        for tweet in self.tweetDenunciados:
            print('tweet denunciado: ', tweet.texto, 'pertenece al usuario @', tweet.usuario)



