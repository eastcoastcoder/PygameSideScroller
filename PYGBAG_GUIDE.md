# Pygbag Web Deployment Guide

## Overview

This project now supports running in web browsers using Pygbag and WebAssembly. The game runs entirely client-side with no server required.

## What is Pygbag?

Pygbag packages Python/Pygame applications to run in web browsers using:

- **WebAssembly**: Compiles Python to run in browsers
- **Emscripten**: The compilation toolchain
- **AsyncIO**: Non-blocking game loop for browser compatibility

## Changes Made for Pygbag Support

### 1. Async Game Loop

The main game loop now uses `async/await` to yield control to the browser's event loop:

```python
async def main():
    # Game initialization
    await game_loop.draw()

# In GameLoop.draw():
while self.is_alive:
    # Game logic
    pygame.display.flip()
    await asyncio.sleep(0)  # Critical: yields to browser
```

### 2. Entry Point

- `main.py` (lowercase) is the Pygbag entry point
- Maintains compatibility with desktop Python execution

### 3. Asset Loading

- Assets must be in the same directory as main.py
- Pygbag bundles all files in the project directory

## Building for Web

### Prerequisites

```bash
source venv/bin/activate
pip install pygbag
```

### Build Commands

**Quick test server:**

```bash
pygbag .
```

This starts a local server at http://localhost:8000

**Build for deployment:**

```bash
pygbag --build .
```

Output: `build/web/` directory contains deployable files

**Custom build script:**

```bash
./build_web.sh
```

## Deployment Options

### Option 1: GitHub Pages

1. Build the project:

   ```bash
   ./build_web.sh
   ```

2. Create a `gh-pages` branch:

   ```bash
   git checkout -b gh-pages
   cp -r build/web/* .
   git add .
   git commit -m "Deploy to GitHub Pages"
   git push origin gh-pages
   ```

3. Enable GitHub Pages in repository settings
   - Go to Settings → Pages
   - Source: gh-pages branch
   - Your game will be at: `https://username.github.io/repo-name/`

### Option 2: itch.io

1. Build the project:

   ```bash
   ./build_web.sh
   ```

2. Create a ZIP of the build/web directory:

   ```bash
   cd build/web
   zip -r game.zip *
   ```

3. Upload to itch.io:
   - Create new project on itch.io
   - Set "Kind of project" to HTML
   - Upload game.zip
   - Check "This file will be played in the browser"
   - Set embed options (800x600 recommended)

### Option 3: Netlify/Vercel

1. Build the project:

   ```bash
   ./build_web.sh
   ```

2. Deploy the `build/web` directory using their CLI or web interface

### Option 4: Self-Hosted

1. Build the project
2. Copy `build/web/*` to your web server
3. Ensure proper MIME types are set:
   - `.wasm`: `application/wasm`
   - `.js`: `application/javascript`

## Testing Locally

### Method 1: Python HTTP Server

```bash
python -m http.server 8000 --directory build/web
```

Open: http://localhost:8000

### Method 2: Pygbag Dev Server

```bash
pygbag --dev .
```

Includes live reload on file changes

## Browser Compatibility

**Supported Browsers:**

- ✅ Chrome/Chromium (recommended)
- ✅ Firefox
- ✅ Edge
- ✅ Safari (macOS/iOS)
- ✅ Opera

**Requirements:**

- WebAssembly support (all modern browsers)
- JavaScript enabled
- SharedArrayBuffer support (for audio)

**Note:** Some older browsers may have limited audio support.

## Performance Considerations

### Browser vs Desktop

- Desktop: ~60 FPS typical
- Browser: 30-60 FPS depending on device

### Optimization Tips

1. Use `await asyncio.sleep(0)` in main loop
2. Minimize file sizes (compress images/audio)
3. Avoid blocking operations
4. Use pygame optimizations (convert_alpha, etc.)

## Troubleshooting

### Game doesn't load

- Check browser console for errors (F12)
- Verify all assets are in the project directory
- Ensure CORS headers if self-hosting

### Audio issues

- Browser audio requires user interaction first
- Some browsers block autoplay
- Check SharedArrayBuffer support

### Performance issues

- Reduce FPS constant if needed
- Optimize sprite rendering
- Check browser's hardware acceleration

### Black screen

- Verify pygame.display.flip() is called
- Check await asyncio.sleep(0) is in game loop
- Ensure assets load correctly

## File Structure for Deployment

```
build/web/
├── index.html          # Main HTML file
├── pythons.js          # Pygbag loader
├── <project>.data      # Game assets
├── <project>.js        # Compiled game
├── <project>.wasm      # WebAssembly binary
└── ...                 # Additional support files
```

## Development Workflow

1. **Develop**: Code and test with `python main.py`
2. **Test Web**: Quick test with `pygbag .`
3. **Build**: Production build with `./build_web.sh`
4. **Deploy**: Upload build/web/\* to hosting

## Additional Resources

- [Pygbag Documentation](https://pygame-web.github.io/)
- [Pygame Documentation](https://www.pygame.org/docs/)
- [WebAssembly](https://webassembly.org/)
- [Example Games](https://pygame-web.github.io/showroom/)

## Known Limitations

1. **File I/O**: Limited compared to desktop
2. **Audio**: May have latency in some browsers
3. **Performance**: Slightly slower than native
4. **Threading**: Limited support
5. **Some Pygame features**: Not all are supported in browser

## Support

For Pygbag-specific issues, see:

- https://github.com/pygame-web/pygbag/issues

For game-specific issues, see project repository.
