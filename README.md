# 🚀 Space Ranger

A Space Invaders-style game built with Python & Pygame, playable in the browser via WebAssembly (Pygbag).

## 🎮 Play Online
👉 **[Play Space Ranger](https://zoinairfan15.github.io/Space-ranger/)**

## Controls
| Key | Action |
|-----|--------|
| `A` | Move Left |
| `D` | Move Right |
| `SPACE` | Fire Laser |
| `F` | Start / Restart Game |

## 🛠 Run Locally

### Requirements
- Python 3.10+
- pygame

```bash
pip install pygame
python spaceranger.py
```

### Run as Web App (Pygbag)
```bash
pip install pygbag
pygbag .
# Open http://localhost:8000
```

## 📁 Project Structure
```
space-ranger/
├── spaceranger.py   # Main game loop
├── rocket.py        # Player ship
├── chicken.py       # Enemy chickens
├── laser.py         # Player projectile
├── egg.py           # Enemy projectile
├── image/           # Game sprites
└── sound1/          # Sound effects
```

## 🚀 Deploy to GitHub Pages
This project is configured to auto-build and deploy via GitHub Actions.
Push to `main` branch → game goes live automatically.
 
