class Wally:
    def __init__(self):
        self.listaPublicidad = []

    def agregarTweet(self, tweet):
        self.listaPublicidad.append(tweet)


    def responderTweet(self):
        for palabra in self.listaPublicidad:
            if 'quilmes' in palabra.texto.lower().split():
                print('Hola @', palabra.usuario,
                      'gracias por interesarte en nuestros productos, podes ver mas informacion en: www.Quilmes.com.ar')
            if 'patagonia' in palabra.texto.lower().split():
                print('Hola @', palabra.usuario,
                      'gracias por interesarte en nuestros productos, podes ver mas informacion en: www.Patagonia.com.ar')
            if 'andes' in palabra.texto.lower().split():
                print('Hola @', palabra.usuario,
                      'gracias por interesarte en nuestros productos, podes ver mas informacion en: www.Andes.com.ar')








