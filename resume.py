import json
import sys

class EnglishResume():
    def __init__(self, filename=None):
        self.filename = filename
        self.content = None
        
        if self.filename:
            self.content = self.loadResume(self.filename)
            
    def isOpened(self):
        if not self.content:
            print('Oops, Failed to load your resume, please check again...')
            return False
        return True
    
    def loadResume(self, filename):
        dumpedResume = None
        with open(filename, 'r') as f:
            dumpedResume = json.loads(f.read())
        return dumpedResume
        
        
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

if __name__ == '__main__':
    resumePath = 'template.json'
    resume = EnglishResume(filename=resumePath)
    print(resume.works())
    print(resume.edu())
    print(resume.skills())