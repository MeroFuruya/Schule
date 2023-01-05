import json
import random
import pathlib

class Questions:
    def __init__(self) -> None:
        random.seed()
        self.last_question: int = -1
        with open(str(pathlib.Path().resolve())+"/questions.json", "r") as f:
            self.questions: dict = json.load(f)
        
    def get_random_question(self):
        self.last_question = random.randint(0, len(self.questions.keys()) - 1)
        return self.questions.get(list(self.questions.keys())[self.last_question])
    
    def check_answer(self, answer: str):
        return answer in self.questions.get(list(self.questions.keys())[self.last_question])