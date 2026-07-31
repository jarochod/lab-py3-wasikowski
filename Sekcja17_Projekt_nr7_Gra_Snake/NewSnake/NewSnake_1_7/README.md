# Snake Game (NewSnake 1.7)

This is a classic Snake game implemented using **Pygame**.

## 🎮 Features

- **Classic Gameplay**: Control a snake to eat food and grow longer.
- **Collision Detection**: Game over if the snake hits itself or the boundaries.
- **Wrapping Borders**: The snake appears on the opposite side of the screen when it goes off-screen.
- **High Score**: Keeps track of your highest score.
- **Pause Functionality**: Pause and resume the game at any time.
- **Sound Effects**: Simple sound effects for eating food and game over.

## 🕹️ How to Play

1. **Run the game**: Execute the Python script (e.g., `python main.py`).

2. **Controls**:
   - `W` or **Up Arrow**: Move Up
   - `S` or **Down Arrow**: Move Down
   - `A` or **Left Arrow**: Move Left
   - `D` or **Right Arrow**: Move Right
   - `P`: Pause / Resume the game
   - `R`: Restart after "Game Over"
   - `ESC`: Exit the game

## 🧰 Requirements

- **Python 3.x**
- **Pygame** library

To install Pygame, use:

```bash
pip install pygame
```

## 📁 Project Structure

```
NewSnake/
├── main.py               # Main game file with logic and classes
├── files/
│   ├── eat.mp3           # Sound for eating food
│   ├── gameover.mp3      # Sound for game over
│   └── highscore.txt     # File storing the high score
```

## 🆕 Changes in NewSnake 1.7 (from version 1.6)

- **Visual Enhancement**:  
  The snake's head is now rendered in a **lighter green**, while the rest of the body is a **darker green**, providing a clearer visual distinction between the head and body.

---

Enjoy the game!
