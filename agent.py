from resume import EnglishResume
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
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

    # RETURN TYPE: (MESSAGEAPI_TO_SEND, MESSAGEAPI_PARAS)
    def selectAction(self, event):
        replyToken, message = event.reply_token, event.message.text
        replyMessage = ''
        if message == '!works':
            replyMessage = self.resume.works()
        elif message == '!edu':
            replyMessage = self.resume.edu()
        elif message == '!skills':
            replyMessage = self.resume.skills()
        else:
            replyMessage = 'Sorry, Peko cannot understand what you said...'
        
        replyObject = TextSendMessage(text=replyMessage)
        return (self.botApi.reply_message, (replyToken, replyObject))
