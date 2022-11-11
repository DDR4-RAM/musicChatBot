from django.http import HttpResponse
from bot.process.validator import Validator
from bot.process.musicChatBot import MusicChatBot
from django.template import loader

chatBot = MusicChatBot('Bot de Musica')
chatBot.train()


def send_message(request):
    if request.POST:
        print("[I] POST")
        template = loader.get_template('index.html')
        if request.POST.get('length', '') == '1':
            conversation = {'1': request.POST.get('message1', ''), '2': request.POST.get('user_text', ''), }
            response = chatBot.get_response(request.POST.get('user_text', ''))
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
            response = chatBot.get_response(request.POST.get('user_text', ''))
            print(f"[I] response <{response}>")
            conversation[str(new_length + 1)] = str(response)
            messages = {
                'length': new_length,
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
