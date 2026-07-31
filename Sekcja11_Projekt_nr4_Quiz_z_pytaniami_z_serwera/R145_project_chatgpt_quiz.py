import requests
import html

# Klasa reprezentująca pojedyncze pytanie
class Question:
    def __init__(self, category, questionStr, correctAnswerFlag) -> None:
        self.category = category  # Kategoria pytania
        self.questionStr = questionStr  # Treść pytania
        self.correctAnswerFlag = correctAnswerFlag  # Flaga: czy poprawna odpowiedź to "tak" (True)

# Klasa reprezentująca cały quiz
class Quiz:
    def __init__(self, numQuestions) -> None:
        # Ustawienie adresu API do pobierania pytań (łatwe, typu "boolean")
        self.apiUrl = "https://opentdb.com/api.php?difficulty=easy&type=boolean&amount="
        self.numQuestions = numQuestions  # Liczba pytań do załadowania
        self.questionsList = []  # Lista przechowująca obiekty Question
        self.loadQuestions(numQuestions)  # Pobranie pytań przy inicjalizacji

    # Metoda pobierająca pytania z API
    def loadQuestions(self, numQuestions):
        response = requests.get(f"{self.apiUrl}{numQuestions}")  # Wysłanie żądania
        
        if response.ok:
            data = response.json()  # Przekształcenie odpowiedzi JSON na słownik
            results = data["results"]  # Lista pytań

            # Tworzenie obiektów Question dla każdego pytania
            for q in results:
                category = q["category"]
                questionType = q["type"]
                difficulty = q["difficulty"]
                questionStr = html.unescape(q["question"])  # Odkodowanie znaków HTML
                correctAnswerFlag = q["correct_answer"].lower() in ['true', '1', 'yes']

                qObj = Question(category, questionStr, correctAnswerFlag)
                self.questionsList.append(qObj)

    # Metoda uruchamiająca quiz
    def startQuiz(self):
        print("\nWelcome to the Quiz!")
        numCorrectUserAnswers = 0  # Licznik poprawnych odpowiedzi
        numQuestions = len(self.questionsList)

        # Pętla po wszystkich pytaniach
        for idx, q in enumerate(self.questionsList, start=1):
            print(f"\nQuestion number {idx}: {q.questionStr}")
            
            userInput = self.getUserAnswer()  # Pobranie odpowiedzi użytkownika

            if userInput == q.correctAnswerFlag:
                print("Correct!")
                numCorrectUserAnswers += 1
            else:
                print("Not correct!")

        # Wynik końcowy
        print(f"\nNumber of correct answers: {numCorrectUserAnswers} out of {numQuestions}")

    # Pomocnicza metoda do bezpiecznego pobrania odpowiedzi od użytkownika
    def getUserAnswer(self):
        valid_yes = {"y", "yes", "tak", "t"}  # Akceptowane odpowiedzi oznaczające "tak"
        valid_no = {"n", "no", "nie"}  # Akceptowane odpowiedzi oznaczające "nie"

        while True:
            answer = input("Give correct answer as y/n: ").strip().lower()
            if answer in valid_yes:
                return True
            elif answer in valid_no:
                return False
            else:
                print("Invalid input. Please type 'y'/'n', 'yes'/'no', or 'tak'/'nie'.")

# Utworzenie instancji quizu z 10 pytaniami i jego uruchomienie
quiz = Quiz(10)
quiz.startQuiz()



"""
ChhatGPT:

Co poprawiłem i ulepszyłem?
✅ Wydzieliłem metodę getUserAnswer(), która:

akceptuje więcej form odpowiedzi (y, yes, tak, t, n, no, nie),

ignoruje wielkość liter i dodatkowe spacje,

powtarza pytanie, jeśli użytkownik wpisze coś nieprawidłowego.

✅ Kod wygląda teraz bardziej czytelnie i jest łatwiej go rozbudować, np. o inne języki odpowiedzi albo dodatkowe komunikaty.

✅ Zamiast ręcznego sterowania licznikiem n, używam enumerate() w pętli for, żeby kod był jeszcze czystszy i bardziej pythonowy.
"""