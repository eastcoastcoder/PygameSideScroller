"""
Python RC file for Pygbag - handles WebAssembly initialization.
This file is loaded before the main game starts in the browser.
"""

import sys
import asyncio
import platform

# Detect if running in WebAssembly/browser environment
if platform.system() == "Emscripten":
    print("Running in WebAssembly/browser environment")
else:
    print("Running in native Python environment")

# Configure for browser environment
sys.setrecursionlimit(1000)  # Lower recursion limit for browser safety

print("pythonrc.py loaded successfully")
