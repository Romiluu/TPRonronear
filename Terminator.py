class Terminator:
    def __init__(self):
        self.listaDeTweets = []

    def agregarTweet(self, tweet):
        self.listaDeTweets.append(tweet)


    def mostrarTweets(self):
        for tweet in self.listaDeTweets:
            print('tweet : ', tweet.texto, 'pertenece al usuario @', tweet.usuario)