sentence=""
class Exercise2:
    def __init__(self,sentence):
        self.sentence=sentence
    def get_string(self):
        sentence = input("Type a sentence:")
        return sentence
    def display_string(sentence):
        sentence=Exercise2.get_string(sentence)
        sentence=sentence.upper()
        print(sentence)
        return sentence
Exercise2.display_string(sentence)