from django.http import HttpResponse
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from .training import Trainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

# Create your views here.
from django.template import loader

chatterbot = ChatBot('Bot de Musica')
trainer = ChatterBotCorpusTrainer(chatterbot)
trainer_list = ListTrainer(chatterbot)
# trainer.train("chatterbot.corpus.spanish")
trainer.export_for_training('export.yml')

trainer_list.train([
    "musica",
    "Te gusta la musica?",
])

trainer_list.train([
    "musica",
    "me gusta el genero rock, a tí?",
    "quiénes son Los Beatles?",
    "Una banda inglesa muy popular en los 60's",
    "conoces alguna canción de tiktok?",
    "Claro que sí. Escucha Cure for me de Aurora.",
    "cuál es el género de música más popular?",
    "De acuerdo Statista Global Consumer Survey, el género más popular es el pop contemporáneo para adultos",
    "Diferencias entre dream pop y shoegaze",
    "La comunidad shoegaze categoriza el género como centrado en la guitarra, utilizando toneladas de reverberación y efectos de retardo, paisajes sonoros en capas e influencias punk, muy diferente al dream pop.",
    "quién fue Michael Jackson?",
    "Fue una leyenda musical, conocido como el rey del pop.",
    "quién es el rey del pop?",
    "El legendario Michael Jackson",
    "quién es la reina del pop?",
    "Me la pones difícil. Disfruta de Madonna y de Beyoncé por igual 😎.",
    "en qué año surge trip hop?",
    "A mediados de 1980 en Bristol, Inglaterra.",
    "de quien es el album mezzanine?",
    "El album Mezzanine pertenece al grupo Massive Attack.",
    "quién fue Elvis Presley?"
    "El gran Elvis Presley es una leyenda musical, conocido como el rey del rock and roll.",
    "quién es el rey del rock n roll?",
    "El legendario Elvis Presley",
    "Cuántos albums tiene led zeppelin?",
    "Led Zeppelin cuenta con 9 álbumes de estudio, 9 recopilatorios, 4 en directo y 3 en video.",
    "En qué año salió romances de Luis Miguel?",
    "El álbum Romances de Luis Miguel es del año 1997.",
    "cuántos discos tiene daft punk?",
    "Daft Punk cuenta con 4 álbumes de estudio, 1 recopilatorios, 2 en directo y 1 en video.",
    "cuál es el disco más vendido en la historia?",
    "El disco más vendido ha sido Thriller de Michael Jackson.",
    "MTV unplugged más escuchado",
    "Probablemente haya sido el MTV Unplugged de 1993, con la banda Nirvana.",
    "de qué banda es Kurt Cobain?",
    "Nirvana",
    "quién fue Freddie Mercury?",
    "Freddue Mercury fue un cantante, compositor, vocalista y líder de la banda inglesa Queen. Su nombre real era Farrokh Bulsara.",
    "quién es el vocalista de Queen?",
    "Farrokh Bulsara, mejor conocido como Freddie Mercury.",
    "quiénes son Rammstein?",
    "Rammstein es una banda alemana de metal industrial formada en 1994 por los músicos Till Lindemann, Richard Z. Kruspe, Oliver Riedel, Paul Landers, Christian Lorenz y Christoph Schneider.",
    "cuál fue el último disco de David Bowie?",
    "The Gouster.",
    "en qué año ganó Leonard Cohen el premio príncipe de Asturias?",
    "Leonard Cohen fue galardonado en el año 2011.",
    "quién fue Jeff Buckley?",
    "Fue un músico de rock alternativo, reconocido como el que popularizó 'Hallelujah'.",
    "en qué año murió John Lennon?",
    "El trágico fallecimiento de John Lennon fue el 8 de diciembre de 1980.",
    "quién escribió Let it Be?",
    "Una de las canciones más reconocidas de The Beatles fue escrita por el dueto Lennon-McCartney.",
    "quién es Drake?",
    "Aubrey Drake Graham, conocido simplemente como Drake, es un rapero, cantante, compositor, productor discográfico y actor canadiense.",
    "quién canta stand by me?",
    "Esa hermosa canción es interpretada por mi buen amigo Ben E. King.",
    "en que banda estuvo Paul McCartney?"
    "La más famosa globalmente fue The Beatles. Posteriormente conformó otro grupo llamado Paul McCartney and Wings.",
    "Qué género es PXNDX",
    "PXNDX es una banda de rock en español originaria de Monterrey, Nuevo León.",
    "quién fue Chuck Berry?",
    "Charles Edward Berry (Chuck Berry) fue un guitarrista, cantante y compositor de rock and roll estadounidense.",
    "qué día murió Chalino Sánchez?",
    "Chalino Sánchez falleció el 16 de mayo de 1992.",
    "conoces a los Beach Boys?",
    "Por su pollo que sí, The Beach Boys es una banda de rock. Muy distinguidos por sus armonías vocales y muy influyentes en la era del Rock And Roll.",
    "quién es Jimi Hendrix?",
    "Jimi Hendrix fue un guitarrista, cantante y compositor estadounidense que solo duró cuatro años de carrera profesional. Aún así, es considerado uno de los guitarristas más influyentes de la historia del rock.",
    "quiénes son AC/DC?",
    "AC/DC es una banda de Hard Rock británica-australiana formada en 1973.",
    "cuál fue la canción del mundial de lol de este año?",
    "Star Walkin' de Lil Nas X.",
    "qué es un picture disc?",
    "Los discos ilustrados (picture disc) son un tipo de discos fonográficos que muestran imágenes en su superficie de reproducción.",
    "de qué país es el grupo el columpio asesino?",
    "El Columpio Asesino es una banda originaria de Pamplona, España en el año 1999.",
    "en qué año se separaron los the white stripes?",
    "La banda The White Stripes oficializó su disolución en febrero de 2011.",
    "De qué nacionalidad son los Cardigans?",
    "The Cardigans es un grupo originario en Suecia en el año 1992.",
    "recomiendame una canción",
    "Espero te guste esta canción 😊 https://youtu.be/dQw4w9WgXcQ",
    "cuántos soundtracks tiene 31 minutos?",
    "31 minutos cuenta con 4 álbumes de estudio, 1 en directo, 2 recopilatorios, 9 sencillos, 1 tributo y 2 colaboraciones",
    "en qué año salió OK computer?",
    "El disco OK Computer se publicó el 16 de junio de 1997 en Reino Unido por Radiohead.",
    "en cuántas bandas estuvo Chris Cornell?",
    "Chris Cornell estuvo en 3 grupos musicales diferentes.",
    "mejor disco de Beyoncé",
    "El disco más vendido de Beyoncé ha sido 'Dangerously in Love'",
    "quién es Kanye West?",
    "Kanye West es un rapero, productor, actor, diseñador y empresario estadounidense.",
    "Qué es el japanoise?",
    "Como su nombre sugiere, el “ruido” es un género musical que explora los límites entre “música” y “no música”.\nLos instrumentos utilizados varían ampliamente. Noise presenta una fusión de instrumentos tradicionales y sonidos electrónicos, grabaciones y máquinas. A veces se describe como un escape sonoro, ya que el ritmo y la estructura son de menor importancia.",
    "Quién es Axl Rose?",
    "William Bruce Bailey, mejor conocido como Axl Rose, es un cantante, compositor y pianista estadounidense.",
    "Quiénes son Masive Attack?",
    "Masive Attack es una banda inglesa, considerados padres del género trip-hop.",
    "Quiénes son Weezer?",
    "Weezer son una banda de rock alternativo estadounidense formada en 1992.",
    "Por qué se separaron The Beatles?",
    "Popularmente se dice que fue culpa de 'Yoko Ono', pero no deja de ser solo una teoría. Paul McCartney declaró en una entrevista que fue John (Lennon) quien un día llegó al estudio y dijo 'Me voy del grupo'.",
    "Cuándo va a regresar One Direction?",
    "NUNCA MUAJAJAJAJA",
    "Quiénes son Black Sabbath?",
    "Black Sabbath fue una banda británica de Heavy Metal y Hard Rock formmada en 1968.",
    "Para qué sirve Parental Advisor?",
    "Parental Advisory: Explicit Content es una etiqueta de clasificación pegada por la Asociación de Industria Magnetofónica de América en muchos álbumes de estudio de artistas y grupos musicales que presentan lenguaje soez.",
    "quién inventó el tocadiscos?",
    "En 1877, Thomas Alva Edison patentó el fonógrafo, un invento capaz de grabar y reproducir posteriormente los sonidos que se grababan sobre cilindros.\nPero las cosas no pararían ahí, en 1883 los científicos Chichester Alexander Bell, su primo Alexander Graham Bell y su socio Charles Tainter mejoraron el fonógrafo de Edison dando paso al grafófono y crearon la Volta Graphophone Company en 1886.\nDos años después otro avance llegó con la astucia de Emile Berliner, que llamó a su mejora gramófono, éste era capaz de trabajar con un disco de goma vulcanizada de 5” y era impulsado de forma manual.",
])


def send_message(request):
    if request.POST:
        print("[I] POST")
        template = loader.get_template('index.html')
        if request.POST.get('length', '') == '1':
            conversation = {'1': request.POST.get('message1', ''), '2': request.POST.get('user_text', ''), }
            response = chatterbot.get_response(request.POST.get('user_text', ''))
            conversation['3'] = str(response)
            messages = {
                'length': '2',
                'conversation': conversation,
            }
            return HttpResponse(template.render(messages, request))
        else:
            conversation = {}
            for index in range(0, int(request.POST.get('length', '')) + 1):
                if request.POST.get('message' + str(index + 1), '') != '':
                    conversation[str(index + 1)] = request.POST.get('message' + str(index + 1), '')
            new_length = int(request.POST.get('length', '')) + 2
            conversation[str(new_length)] = request.POST.get('user_text', '')
            print(f"[O] TRAINER <{request.POST.get('user_text', '')}>")
            response = chatterbot.get_response(request.POST.get('user_text', ''))
            print(f"[I] response <{response}>")
            conversation[str(new_length + 1)] = str(response)
            messages = {
                'length': new_length + 1,
                'conversation': conversation,
            }
            print(messages)
            return HttpResponse(template.render(messages, request))
    else:
        print('[I] GET')
        template = loader.get_template('index.html')
        conversation = {
            '1': 'Hola, soy MusicBot. ¡Puedes hacerme cualquier pregunta sobre música! 😄',
        }
        messages = {
            'length': 1,
            'conversation': conversation
        }
        return HttpResponse(template.render(messages, request))
