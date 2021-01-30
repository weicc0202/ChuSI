from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer
from rasa_nlu.model import Interpreter
from rasa_nlu.test import run_evaluation
import pprint
import json

def interpret(sentence, interpreter):
    # interpreter = Interpreter.load(nlu_path)
    return [interpreter.parse(sentence)['intent']['name']]
    # pprint.pprint(interpreter.parse("Share some latest news around the world?"))
    # pprint.pprint(interpreter.parse("What is going on in technology?"))
    # pprint.pprint(interpreter.parse("What is going on in education?"))

if __name__ == '__main__':
    interpreter = Interpreter.load('./models/current/nlu')
    results = []
    results += interpret('Hi', interpreter)
    results += interpret("Who's weichu?", interpreter)
    results += interpret("show weichu's work experience", interpreter)
    results += interpret("show me work experience", interpreter)
    print(results)