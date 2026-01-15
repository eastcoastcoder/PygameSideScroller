# Quick Start Guide - Web Deployment

## For Developers

### 1. Test the game works locally

```bash
python main.py
```

### 2. Test in browser (quick)

```bash
pygbag .
```

Opens at http://localhost:8000 automatically

### 3. Build for production

```bash
./build_web.sh
```

Output: `build/web/` directory

### 4. Deploy

**GitHub Pages:**

```bash
# After building
git checkout -b gh-pages
cp -r build/web/* .
git add .
git commit -m "Deploy web version"
git push origin gh-pages
```

Enable in Settings → Pages

**itch.io:**

```bash
cd build/web
zip -r game.zip *
```

Upload to itch.io as HTML project

**Quick hosting test:**

```bash
python -m http.server 8000 --directory build/web
```

Visit http://localhost:8000

## For Players

### Play in Browser

Visit the deployed URL (GitHub Pages, itch.io, etc.)

### Controls

- **W/↑** - Jump
- **A/←** - Move Left
- **D/→** - Move Right
- **SPACE** - Attack
- **G** - Switch Weapon
- **F** - Toggle Sword Position
- **ESC** - Quit

## Common Commands

```bash
# Development
python main.py              # Run desktop version
pygbag .                    # Test web version
./build_web.sh             # Build for production

# Deployment
pygbag --build .           # Build only (no server)
pygbag --archive .         # Create archive for upload
```

## Troubleshooting

**Problem**: Game doesn't load in browser

- **Solution**: Check browser console (F12), ensure all assets are present

**Problem**: No audio

- **Solution**: Click on game canvas first (browser autoplay policy)

**Problem**: pygbag command not found

- **Solution**: `pip install pygbag` in your venv

**Problem**: Build fails

- **Solution**: Ensure all imports are correct and assets exist

## File Checklist

Before building, ensure you have:

- ✅ `main.py` (async entry point)
- ✅ `index.html` (optional custom page)
- ✅ All `.py` game files
- ✅ All asset files (images, sounds)
- ✅ `requirements.txt` with pygame and pygbag

## Next Steps

1. **Customize index.html** - Add your own styling/branding
2. **Optimize assets** - Compress images/audio for faster loading
3. **Test on mobile** - Touch controls may need adjustment
4. **Share your game** - Deploy and share the URL!

## Resources

- Documentation: [PYGBAG_GUIDE.md](PYGBAG_GUIDE.md)
- Pygbag Docs: https://pygame-web.github.io/
- Examples: https://pygame-web.github.io/showroom/
