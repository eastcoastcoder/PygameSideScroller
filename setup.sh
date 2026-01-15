#!/bin/bash
# Setup script for first-time installation

echo "Setting up PygameSideScroller..."

# Check if venv exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
else
    echo "Virtual environment already exists."
fi

# Activate venv and install dependencies
echo "Installing dependencies..."
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "Setup complete!"
echo "To run the game, use: ./run.sh"
echo "Or manually: source venv/bin/activate && python main.py"
