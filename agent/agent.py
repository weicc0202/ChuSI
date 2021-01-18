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
    
    def reply(self, event):
        replyToken, message = event.reply_token, event.message.text
        replyMessage = None
        if message == 'Show Work Experience':
            replyMessage = self.resume.wrapMessage(title='works')
        elif message == 'Show Education':
            replyMessage = self.resume.wrapMessage(title='edu')
        elif message == 'Show Skills':
            replyMessage = self.resume.wrapMessage(title='skills')
        elif message == 'Show NTU':
            replyMessage = self.resume.wrapMessage(title='edu', types='ntugiee')
        elif message == 'Show NTHU':
            replyMessage = self.resume.wrapMessage(title='edu', types='nthucs')
        elif message == 'Show MediaTek ASIC':
            replyMessage = self.resume.wrapMessage(title='works', types='mtkasic')
        elif message == 'Show MediaTek CTD':
            replyMessage = self.resume.wrapMessage(title='works', types='mtkvyf')
        elif message == 'Show Eagle':
            replyMessage = self.resume.wrapMessage(title='edu', types='eagle')
        elif message == 'Show Software skills':
            replyMessage = self.resume.wrapMessage(title='edu', types='software')
        elif message == 'Show Hardware skills':
            replyMessage = self.resume.wrapMessage(title='edu', types='hardware')
        else:
            replyMessage = TextSendMessage(text='Sorry, Peko cannot understand what you said...')

        self.botApi.reply_message(replyToken, replyMessage)

        to, message = event.source.user_id, TextSendMessage(text='Pekopekopekopeko')
        self.botApi.push_message(to, message) 
