from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer


class Trainer:

    def __init__(self, chatbot):
        self.chatbot = chatbot
        self.trainer = ChatterBotCorpusTrainer(chatbot)
        self.trainer_list = ListTrainer(chatbot)

    def train(self):
        self.trainer.train("chatterbot.corpus.spanish")
        self.trainer.export_for_training('export.yml')

        self.trainer_list.train([
            "musica",
            "Te gusta la musica",
        ])

        self.trainer_list.train([
            "musica",
            "me gusta el genero rock, a tí?",
        ])
        # self.trainer.train([
        #    "Greetings!",
        #    "Hello",
        # ])
        # self.trainer.train([
        #    "How are you?",
        #    "I am good.",
        #    "That is good to hear.",
        #    "Thank you",
        #    "You are welcome.",
        # ])
