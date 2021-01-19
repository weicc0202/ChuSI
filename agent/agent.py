from resume.resume import EnglishResume
from linebot.models import (
    TextSendMessage, ImageSendMessage
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
        imageUrl = 'https://i.pinimg.com/originals/7b/39/c6/7b39c67abc82d534cc91a3e6c4cd8609.gif'
        to, message = event.source.user_id, self.resume.welcome()
        self.botApi.push_message(to, TextSendMessage(text="Hello! I'm Weichu."))
        self.botApi.push_message(to, TextSendMessage(text="Nice to meet you."))
        self.botApi.push_message(to, ImageSendMessage(
            original_content_url=imageUrl,
            preview_image_url=imageUrl
        ))
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
            qrcode = 'https://imgur.com/32eTpuX.png'
            replyMessage += [TextSendMessage(text='Sorry, I cannot understand...')]
            replyMessage += [TextSendMessage(text='Check out my Github to follow the latest feature and future plan.')]
            replyMessage += [ImageSendMessage(
                original_content_url=qrcode,
                preview_image_url=qrcode
            )]
            replyMessage += [self.resume.wrapMessage(title='others')]
        self.__reply(event, replyMessage)
