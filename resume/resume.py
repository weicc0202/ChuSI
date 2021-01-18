from access.access import readJson
import sys
import os
from linebot.models import (
    TextSendMessage, FlexSendMessage
)

class EnglishResume():
    def __init__(self, filename=None):
        self.filename = filename
        self.content = {}
        
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
        for title in titles:
            fields[title]['entry'] = readJson(os.path.join(path, template[title]['entry']))
            fields[title]['details'] = readJson(os.path.join(path, template[title]['details']))
        return fields
        
    def welcome(self):
        message = self.content['welcome']
        return FlexSendMessage(alt_text='Hello!', contents=message)

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
    print(resume.works())
    print(resume.edu())
    print(resume.skills())