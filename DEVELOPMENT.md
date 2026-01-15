# Development Guide

## Getting Started

### First Time Setup

```bash
./setup.sh
```

### Running the Game

```bash
./run.sh
```

Or manually:

```bash
source venv/bin/activate
python Main.py
```

## Development Workflow

### Activating Virtual Environment

Always activate the virtual environment before working:

```bash
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate     # Windows
```

### Deactivating Virtual Environment

```bash
deactivate
```

### Installing New Dependencies

```bash
pip install <package-name>
pip freeze > requirements.txt  # Update requirements file
```

## Code Style Guidelines

### 1. Type Hints

Always add type hints to function signatures:

```python
def my_function(x: int, y: str) -> bool:
    return True
```

### 2. Docstrings

Use Google-style docstrings:

```python
def example_function(param1: int, param2: str) -> None:
    """Brief description of function.

    Args:
        param1: Description of param1.
        param2: Description of param2.
    """
    pass
```

### 3. Imports

- Use specific imports, not wildcard imports
- Group imports: standard library, third-party, local
- One import per line

```python
# Good
import os
import pygame
from Constants import SCREEN_WIDTH, SCREEN_HEIGHT

# Avoid
from Constants import *
```

### 4. Constants

- Use UPPER_CASE for constants
- Add type hints with Final

```python
from typing import Final

SCREEN_WIDTH: Final[int] = 800
```

### 5. Naming Conventions

- Classes: PascalCase (e.g., `GameLoop`, `EnemyManager`)
- Functions/methods: snake_case (e.g., `update_position`, `check_collision`)
- Constants: UPPER_SNAKE_CASE (e.g., `PLAYER_SPEED`, `MAX_HEALTH`)
- Private methods: \_leading_underscore (e.g., `_internal_method`)

## Project Architecture

### Main Components

1. **Main.py**: Entry point, initializes pygame and starts game loop
2. **GameLoop.py**: Main game loop, handles game state
3. **Player.py**: Player character with movement and combat
4. **EnemyManager.py**: Spawns and manages all enemies
5. **LevelLoader.py**: Loads levels from ASCII maps
6. **CollisionManager.py**: Handles collision detection

### Adding New Features

#### Adding a New Enemy Type

1. Extend the `Enemy` class
2. Register in `EnemyManager.spawn()`
3. Add to level ASCII map key

#### Adding New Weapons

1. Create new weapon class extending `pygame.Rect`
2. Add to `Player` class
3. Update `Controller` for input handling

#### Adding New Levels

1. Create ASCII map string in `LevelLoader`
2. Add level number case in `load()` method

## Testing

Currently no automated tests. To test:

1. Run the game
2. Test all controls
3. Test weapon switching
4. Test enemy interactions
5. Test level scrolling

## Debugging

### Common Issues

**ImportError**: Make sure virtual environment is activated

```bash
source venv/bin/activate
```

**Missing Assets**: Ensure asset files (_.wav, _.jpg) are in project root

**pygame.error**: Check pygame version

```bash
pip install --upgrade pygame
```

### Adding Debug Output

Use proper logging instead of print:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.debug(f"Player position: {self.x}, {self.y}")
```

## Performance Tips

1. Minimize object creation in game loop
2. Use sprite groups for batch rendering
3. Cache loaded images
4. Profile with cProfile if needed

## Git Workflow

### Before Committing

1. Test the game runs without errors
2. Check no venv/ files are being committed
3. Update requirements.txt if dependencies changed

### Commit Message Format

```
type: Brief description

Longer description if needed
```

Types: feat, fix, docs, style, refactor, test, chore

### Example

```
feat: Add double jump mechanic

- Added jump counter to Player class
- Updated jump logic in update_jump()
- Added constant MAX_JUMPS = 2
```

## Resources

- [Pygame Documentation](https://www.pygame.org/docs/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)
- [PEP 8 Style Guide](https://peps.python.org/pep-0008/)
