from datafile import question_data_store


class Quiz:
    def __init__(self):
        self.score = 0
        self.total = 0

    def question(self):
        still_working = True
        while still_working:
            for every_question in question_data_store:
                user_answer = input(f'{every_question["text"]} (True or false): ').lower()
                if user_answer == every_question["answer"].lower():
                    report = "correct".lower()
                    self.score += 1
                else:
                    report = "wrong".lower()
                print(report)
                self.total += 1
                print(f'Total score: {self.score} out of {self.total}')
                if self.total == len(question_data_store):
                    still_working = False


quiz = Quiz()
quiz.question()