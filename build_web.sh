#!/bin/bash
# Build script for Pygbag web deployment

echo "Building for web with Pygbag..."

# Check if pygbag is installed
if ! command -v pygbag &> /dev/null; then
    echo "Error: pygbag is not installed."
    echo "Install it with: pip install pygbag"
    exit 1
fi

# Build the web version
echo "Running pygbag build..."
pygbag --build --cdn https://pygame-web.github.io/archives/0.9/ .

echo ""
echo "Build complete!"
echo "To test locally, run: python -m http.server 8000 --directory build/web"
echo "Then open: http://localhost:8000"
echo ""
echo "NOTE: If you see 404 errors for pygame packages, packages will be loaded from CDN."
