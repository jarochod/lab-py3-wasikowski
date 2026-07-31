# 🐍 Snake Game in Pygame

A modern implementation of the classic Snake game using Python and Pygame.

## 🎮 Features

- Smooth snake movement and growing
- Food respawns in random free tiles
- Collision detection (including self-collision)
- Sound effects (`eat.mp3`, `gameover.mp3`)
- Pause (`P`), restart (`R`), and exit (`ESC`) controls
- Score and highscore tracking (`highscore.txt`)
- Fully wrapped screen (snake reappears on the opposite side)

## 🖼️ Screenshot

> *(Optionally insert an image of the game here)*

## 🚀 How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the game:
   ```bash
   python snake_game.py
   ```

   *(Replace `snake_game.py` with your actual filename.)*

## 📁 Folder Structure

```
project_folder/
│
├── snake_game.py
├── requirements.txt
├── README.md
└── files/
    ├── eat.mp3
    ├── gameover.mp3
    └── highscore.txt
```

> Note: `highscore.txt` can be an empty file or will be created automatically.

## 🎹 Controls

| Key | Action           |
|-----|------------------|
| W   | Move up          |
| A   | Move left        |
| S   | Move down        |
| D   | Move right       |
| P   | Pause/Unpause    |
| R   | Restart game     |
| ESC | Exit game        |

## ✅ Requirements

- Python 3.7+
- Pygame 2.0+

## 📜 License

This project is open-source. You can use, modify, and distribute it freely.
