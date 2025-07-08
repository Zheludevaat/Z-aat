from pathlib import Path

def show_lesson(filename: str):
    path = Path(__file__).resolve().parent / filename
    if path.exists():
        print(path.read_text())
    else:
        print(f"Missing lesson: {filename}")
