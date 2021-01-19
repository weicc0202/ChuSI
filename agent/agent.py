from resume.resume import EnglishResume
from linebot.models import (
    TextSendMessage,
)
import os
import sys

class BasicAgent():
    def __init__(self, botApi=None):
        self.history = []
        self.resume = None
        self.botApi = botApi

    def parseResume(self, filename):
        self.resume = EnglishResume(filename=filename)

    def welcome(self, event):
        to, message = event.source.user_id, self.resume.welcome()
        self.botApi.push_message(to, message) 
    
    def __reply(self, event, messages):
        if not messages:
            return

        replyToken, message = event.reply_token, event.message.text
        self.botApi.reply_message(replyToken, messages[0])

        if len(messages) > 1:
            for message in messages[1:]:
                to = event.source.user_id
                self.botApi.push_message(to, message) 

    def reply(self, event):
        replyToken, message = event.reply_token, event.message.text
        replyMessage = []
        if message == 'Show Welcome':
            replyMessage += [self.resume.welcome()]
        elif message == 'Show Work Experience':
            replyMessage += [self.resume.wrapMessage(title='works')]
        elif message == 'Show Education':
            replyMessage += [self.resume.wrapMessage(title='education')]
        elif message == 'Show Skills':
            replyMessage += [self.resume.wrapMessage(title='skills')]
        elif message == 'Show NTU':
            types = 'ntugiee'
            replyMessage += [self.resume.wrapMessage(title='education', types='ntugiee')]
            replyMessage += [self.resume.suggest(types=types)]
        elif message == 'Show NTHU':
            types = 'nthucs'
            replyMessage += [self.resume.wrapMessage(title='education', types='nthucs')]
            replyMessage += [self.resume.suggest(types=types)]
        elif message == 'Show MediaTek ASIC':
            types = 'mtkasic'
            replyMessage += [self.resume.wrapMessage(title='works', types='mtkasic')]
            replyMessage += [self.resume.suggest(types=types)]
        elif message == 'Show MediaTek CTD':
            types = 'mtkctd'
            replyMessage += [self.resume.wrapMessage(title='works', types='mtkctd')]
            replyMessage += [self.resume.suggest(types=types)]
        elif message == 'Show Eagle':
            types = 'eagle'
            replyMessage += [self.resume.wrapMessage(title='works', types='eagle')]
            replyMessage += [self.resume.suggest(types=types)]
        elif message == 'Show Software skills':
            types = 'software'
            replyMessage += [self.resume.wrapMessage(title='skills', types='software')]
            replyMessage += [self.resume.suggest(types=types)]
        elif message == 'Show Hardware skills':
            types = 'hardware'
            replyMessage += [self.resume.wrapMessage(title='skills', types=types)]
            replyMessage += [self.resume.suggest(types=types)]
        else:
            replyMessage += [TextSendMessage(text='Sorry, Peko cannot understand what you said...')]

        self.__reply(event, replyMessage)
