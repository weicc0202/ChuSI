from resume.resume import EnglishResume
from upload import updateLogs
from linebot.models import (
    TextSendMessage, FlexSendMessage
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
        to, messages = event.source.user_id, self.resume.welcome()
        for message in messages:
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
        response, replyMessage = None, []
        if message == 'Show Others':
            replyMessage += [self.resume.wrapMessage(title='others')]
        elif message == 'Show Work Experience':
            replyMessage += [self.resume.wrapMessage(title='works')]
        elif message == 'Show Education':
            replyMessage += [self.resume.wrapMessage(title='education')]
        elif message == 'Show Skills':
            replyMessage += [self.resume.wrapMessage(title='skills')]
        elif message == 'Show NTU':
            types = 'ntugiee'
            updateLogs(event.source.user_id, types)
            replyMessage += [self.resume.wrapMessage(title='education', types='ntugiee')]
            replyMessage += [self.resume.suggest(types=types)]
        elif message == 'Show NTHU':
            types = 'nthucs'
            response = updateLogs(event.source.user_id, types)
            replyMessage += [self.resume.wrapMessage(title='education', types='nthucs')]
            replyMessage += [self.resume.suggest(types=types)]
        elif message == 'Show MediaTek ASIC':
            types = 'mtkasic'
            response = updateLogs(event.source.user_id, types)
            replyMessage += [self.resume.wrapMessage(title='works', types='mtkasic')]
            replyMessage += [self.resume.suggest(types=types)]
        elif message == 'Show MediaTek CTD':
            types = 'mtkctd'
            response = updateLogs(event.source.user_id, types)
            replyMessage += [self.resume.wrapMessage(title='works', types='mtkctd')]
            replyMessage += [self.resume.suggest(types=types)]
        elif message == 'Show Eagle':
            types = 'eagle'
            response = updateLogs(event.source.user_id, types)
            replyMessage += [self.resume.wrapMessage(title='works', types='eagle')]
            replyMessage += [self.resume.suggest(types=types)]
        elif message == 'Show Software skills':
            types = 'software'
            response = updateLogs(event.source.user_id, types)
            replyMessage += [self.resume.wrapMessage(title='skills', types='software')]
            replyMessage += [self.resume.suggest(types=types)]
        elif message == 'Show Hardware skills':
            types = 'hardware'
            response = updateLogs(event.source.user_id, types)
            replyMessage += [self.resume.wrapMessage(title='skills', types=types)]
            replyMessage += [self.resume.suggest(types=types)]
        else:
            replyMessage += self.resume.exceptions()
            replyMessage += [self.resume.wrapMessage(title='others')]
        self.__reply(event, replyMessage)
        if response:
            print(response)
