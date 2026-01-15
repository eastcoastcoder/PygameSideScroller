# PygameSideScroller

A side-scrolling action game built with Python and Pygame.

## Features

- Side-scrolling platformer gameplay
- Player combat with sword and gun mechanics
- Enemy AI with melee combat
- Level system with terrain and collision detection
- Ammunition powerup system

## Requirements

- Python 3.8 or higher
- pygame 2.0.0 or higher
- pygbag 0.8.7 or higher (for web deployment)

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd PygameSideScroller
```

2. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Game

### Desktop Version

Activate the virtual environment and run:

```bash
source venv/bin/activate  # On Windows: venv\Scripts\activate
python main.py
```

Or use the convenience script: `./run.sh`

### Web Browser Version (WebAssembly)

This game can run in a web browser using Pygbag and WebAssembly!

**Option 1: Build and test locally**

```bash
# Build for web
./build_web.sh

# Test locally (requires Python's http.server)
python -m http.server 8000 --directory build/web
# Then open http://localhost:8000 in your browser
```

**Option 2: Deploy to GitHub Pages or itch.io**

```bash
# Build creates a build/web directory
./build_web.sh

# The build/web folder contains all files needed for deployment
# Upload to GitHub Pages, itch.io, or any static hosting service
```

**Option 3: Quick test with pygbag server**

```bash
pygbag .
# Opens automatically at http://localhost:8000n/activate  # On Windows: venv\Scripts\activate
python Main.py
```

## Controls

- **W / ↑**: Jump
- **A / ←**: Move Left
- **D / →**: Move Right
- **SPACE**: Attack (shoot with gun / stab with sword)
- **G**: Switch weapon (gun/sword)
- **F**: Toggle sword position (up/down)
- **ESC**: Quit game

## Project Structure

- `Main.py` - Entry point and game initialization
- `GameLoop.py` - Main game loop and state management
- `Player.py` - Player character logic and controls
- `Enemy.py` - Enemy entity behavior
- `EnemyManager.py` - Enemy spawning and AI management
- `Controller.py` - Input handling
- `LevelLoader.py` - Level loading from ASCII maps
- `Terrain.py` - Terrain block entities
- `Gun.py` - Gun weapon implementation
- `Sword.py` - Sword weapon implementation
- `Bullets.py` - Bullet projectile entity
- `BulletManager.py` - Bullet lifecycle management
- `CollisionManager.py` - Collision detection system
- `Constants.py` - Game constants and configuration

## Authors

Joshua Sonnenberg and Ethan Richardson

## License

CS391 Intro to GameDev with Python and Pygame - Final Project
