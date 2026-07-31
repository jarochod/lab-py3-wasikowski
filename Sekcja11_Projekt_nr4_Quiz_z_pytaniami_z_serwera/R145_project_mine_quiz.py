# R145. Program Quiz z opentdb.com api

import requests
import html

# Klasa reprezentująca pojedyncze pytanie
class Question:
    def __init__(self, category, questionStr, correctAnswerFlag) -> None:
        self.category = category  # Kategoria pytania
        self.questionStr = questionStr  # Treść pytania
        self.correctAnswerFlag = correctAnswerFlag  # Czy odpowiedź "tak" (True) jest poprawna

# Klasa reprezentująca cały quiz
class Quiz:
    def __init__(self, numQuestions) -> None:
        # Ustawienie adresu API do pobrania pytań (łatwe, poziom trudności "easy", pytania typu tak/nie)
        self.apiUrl = "https://opentdb.com/api.php?difficulty=easy&type=boolean&amount="
        self.numQuestions = numQuestions  # Liczba pytań w quizie
        self.questionsList = []  # Lista obiektów Question
        self.loadQuestions(numQuestions)  # Pobranie pytań od razu przy utworzeniu obiektu

    # Metoda pobierająca pytania z API
    def loadQuestions(self, numQuestions):
        response = requests.get(f"{self.apiUrl}{numQuestions}")  # Wysłanie zapytania do API
        
        if response.ok:
            data = response.json()  # Przekształcenie odpowiedzi na słownik Pythonowy
            results = data["results"]  # Lista pytań

            # Przetwarzanie każdego pytania osobno
            for q in results:
                category = q["category"]
                questionType = q["type"]
                difficulty = q["difficulty"]
                # Odkodowanie znaków HTML (np. &quot; -> ")
                questionStr = html.unescape(q["question"])
                # Zamiana poprawnej odpowiedzi na flagę boolowską (True dla "true", "1", "yes")
                correctAnswerFlag = q["correct_answer"].lower() in ['true', '1', 'yes']

                # Tworzenie obiektu Question i dodanie go do listy pytań
                qObj = Question(category, questionStr, correctAnswerFlag)
                self.questionsList.append(qObj)

    # Metoda uruchamiająca quiz
    def startQuiz(self):
        print("\nWelcome in Quiz!")
        numCorrectUserAnswers = 0  # Licznik poprawnych odpowiedzi
        n = 0
        numQuestions = len(self.questionsList)  # Liczba pytań w quizie

        # Pętla z pytaniami
        while n < numQuestions:
            q = self.questionsList[n]
            print(f"Question number {n+1}: {q.questionStr}")  # Wyświetlenie pytania

            # Pobranie odpowiedzi użytkownika
            answer = input("Give correct answer as y/n: ").strip().lower()
            answerBool = False
            if answer == "y":
                answerBool = True

            # Sprawdzenie odpowiedzi
            if answerBool == q.correctAnswerFlag:
                print("Correct!")
                numCorrectUserAnswers += 1
            else:
                print("Not correct!")
            
            n += 1  # Przejście do następnego pytania

        # Wyświetlenie końcowego wyniku
        print(f"\nNumber of correct answers: {numCorrectUserAnswers} from {numQuestions}")

# Utworzenie instancji quizu z 10 pytaniami i jego uruchomienie
quiz = Quiz(10)
quiz.startQuiz()
