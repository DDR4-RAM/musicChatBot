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
trainer.train("chatterbot.corpus.spanish")
trainer.export_for_training('export.yml')

trainer_list.train([
    "musica",
    "Te gusta la musica",
])

trainer_list.train([
    "musica",
    "me gusta el genero rock, a tí?",
])


def send_message(request):
    if request.POST:
        print("[I] POST")
        template = loader.get_template('index.html')
        if request.POST.get('length', '') == '1':
            conversation = {'1': request.POST.get('message1', ''), '2': 'YOU: ' + request.POST.get('user_text', ''), }
            response = chatterbot.get_response(request.POST.get('user_text', ''))
            conversation['3'] = 'BOT: ' + str(response)
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
            conversation[str(new_length)] = 'YOU: ' + request.POST.get('user_text', '')
            print(f"[O] TRAINER <{request.POST.get('user_text', '')}>")
            response = chatterbot.get_response(request.POST.get('user_text', ''))
            print(f"[I] response <{response}>")
            conversation[str(new_length + 1)] = 'BOT: ' + str(response)
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
            '1': 'BOT: Hola, ¿te gustaría saber de musica?',
        }
        messages = {
            'length': 1,
            'conversation': conversation
        }
        return HttpResponse(template.render(messages, request))
