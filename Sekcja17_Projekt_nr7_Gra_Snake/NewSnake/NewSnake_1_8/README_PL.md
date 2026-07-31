# Gra w Węża (NewSnake 1.7)

To jest klasyczna gra w Węża zaimplementowana przy użyciu biblioteki **Pygame**.

## 🎮 Funkcje

- **Klasyczna rozgrywka**: Steruj wężem, aby jeść jedzenie i stawać się dłuższym.
- **Wykrywanie kolizji**: Koniec gry, jeśli wąż zderzy się ze sobą lub z granicami ekranu.
- **Zawijanie ekranu**: Wąż pojawia się po przeciwnej stronie ekranu, gdy z niego wyjdzie.
- **Najlepszy wynik**: Gra zapamiętuje Twój najwyższy wynik.
- **Funkcja pauzy**: Możliwość wstrzymania i wznowienia gry w dowolnym momencie.
- **Efekty dźwiękowe**: Proste efekty dźwiękowe przy jedzeniu i końcu gry.

## 🕹️ Jak grać

1. **Uruchom grę**: Uruchom skrypt Pythona (np. `python main.py`).

2. **Sterowanie**:
   - `W` lub **Strzałka w górę**: Ruch w górę
   - `S` lub **Strzałka w dół**: Ruch w dół
   - `A` lub **Strzałka w lewo**: Ruch w lewo
   - `D` lub **Strzałka w prawo**: Ruch w prawo
   - `P`: Pauza / Wznów grę
   - `R`: Restart po "Końcu Gry"
   - `ESC`: Wyjście z gry

## 🧰 Wymagania

- **Python 3.x**
- **Biblioteka Pygame**

Aby zainstalować Pygame, użyj:

```bash
pip install pygame
```

## 📁 Struktura projektu

```
NewSnake/
├── main.py               # Główny plik gry z logiką i klasami
├── files/
│   ├── eat.mp3           # Dźwięk przy jedzeniu
│   ├── gameover.mp3      # Dźwięk końca gry
│   └── highscore.txt     # Plik przechowujący najlepszy wynik
```

## 🆕 Zmiany w NewSnake 1.7 (w porównaniu do wersji 1.6)

- **Ulepszenia wizualne**:  
  Głowa węża jest teraz wyświetlana w **jaśniejszym zielonym** kolorze, a reszta ciała w **ciemniejszym odcieniu zieleni**, co zapewnia lepsze rozróżnienie wizualne.

---

Miłej zabawy!
