from access.access import readJson
import random
import sys
import os
from linebot.models import (
    TextSendMessage, FlexSendMessage
)

class EnglishResume():
    def __init__(self, filename=None):
        self.filename = filename
        self.content = {}
        self.titles = [['works', 'education', 'skills'],['mtkasic', 'mtkctd', 'eagle'], ['ntugiee', 'nthucs'], ['software','hardware']]
        self.label_dict = {
            'works': ('Work Experience', 'Show Work Experience'),
            'education': ('Education', 'Show Education'),
            'skills': ('Skills', 'Show Skills'),
            'ntugiee': ('Master in NTUGIEE', 'Show NTU'),
            'nthucs': ('BS in NTHUCS', 'Show NTHU'),
            'mtkasic': ('MediaTek-ASIC', 'Show MediaTek ASIC'),
            'mtkctd': ('MediaTek-CTD', 'Show MediaTek CTD'),
            'eagle': ('Eagle', 'Show Eagle'),
            'software': ('Software Skills', 'Show Software skills'),
            'hardware': ('Hardware Skills', 'Show Hardware skills'),
        }
        if self.filename:
            self.content = self.loadResume(self.filename)
            
    def isOpened(self):
        if not self.content:
            print('Oops, Failed to load your resume, please check again...')
            return False
        return True
    
    def loadResume(self, filename):
        fields = {
            "welcome": None,
            'works': {"entry": None, "details": None},
            'education': {"entry": None, "details": None},
            'skills': {"entry": None, "details": None},
        }
        path = os.path.split(filename)[0]
        titles = ['works', 'education', 'skills']
        template = readJson(filename)

        fields['welcome'] = readJson(os.path.join(path, template['welcome']))
        fields['suggest'] = readJson(os.path.join(path, template['suggest']))
        fields['others'] = readJson(os.path.join(path, template['others']))
        for title in titles:
            fields[title]['entry'] = readJson(os.path.join(path, template[title]['entry']))
            fields[title]['details'] = {}
            for name in template[title]['details']:
                filename = name.split('.')[0]
                fields[title]['details'][filename] = readJson(os.path.join(path, name))
        return fields
        
    def wrapMessage(self, title, types='entry'):
        content = None
        if title in ['welcome', 'others']:
            content = self.content[title]
        elif types == 'entry':
            content = self.content[title][types]
        else:
            content = self.content[title]['details'][types]
        return FlexSendMessage(alt_text='Hello!', contents=content)


    def __suggest(self, types='works'):
        choices = []
        for details in self.titles:
            if types in details:
                index = details.index(types)
                choices = details[0:index] + details[index+1:]
        return random.choice(choices)
            
    def __suggest_label(self, label):
        return self.label_dict[label]

    def suggest(self, types='works'):
        content = self.content['suggest']
        label, text = self.__suggest_label(self.__suggest(types))
        content['footer']['contents'][0]['action']['label'] = label
        content['footer']['contents'][0]['action']['text'] = text
        return FlexSendMessage(alt_text='Hello!', contents=content)

    def welcome(self):
        messages = []
        messages += [TextSendMessage(text="Hello! I'm Weichu.")]
        messages += [TextSendMessage(text="Nice to meet you.")]
        messages += [FlexSendMessage(alt_text='Hello!', contents={
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": "https://i.pinimg.com/originals/7b/39/c6/7b39c67abc82d534cc91a3e6c4cd8609.gif",
                "size": "full",
                "aspectRatio": "20:13",
                "aspectMode": "cover"
            }
        })]
        messages += [FlexSendMessage(alt_text='Hello!', contents=self.content['welcome'])]
        return messages

    def workEntry(self):
        message = self.content['works']['entry']
        return FlexSendMessage(alt_text='Hello!', contents=message)


    def eduEntry(self):
        message = self.content['education']['entry']
        return FlexSendMessage(alt_text='Hello!', contents=message)

    def skillEntry(self):
        message = self.content['skills']['entry']
        return FlexSendMessage(alt_text='Hello!', contents=message)
    '''
    def works(self):
        name, experience = self.content['name'], self.content['works']
        message = '%s had some work experience in: \n' % (name)
        for key, value in experience.items():
            message += '\t%s as %s\n' % (key, value)
        return message
    
    def edu(self):
        name, education = self.content['name'], self.content['education']
        message = '%s studied in: \n' % (name)
        for key, value in education.items():
            message += '\t%s in %s\n' % (key, value)
        return message
    
    def skills(self):
        name, skills = self.content['name'], self.content['skills']
        message = '%s has various and diverse programming skills.\n' % (name)
        for key, value in skills.items():
            message += '\tFor %s field, he has %s abilities.\n' % (key, value)
        return message
    '''

if __name__ == '__main__':
    resumePath = 'template.json'
    resume = EnglishResume(filename=resumePath)