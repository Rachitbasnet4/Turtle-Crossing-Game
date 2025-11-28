# Turtle Crossing Game 🐢🚦

A simple arcade-style game built using Python's `turtle` module.  
Guide the turtle across a busy road while avoiding moving cars. The game increases in difficulty with each successful crossing.

---

## 🎮 Game Description

The objective of the game is to safely move the turtle from the bottom to the top of the screen without colliding with any cars. Each time the turtle reaches the finish line, the level increases and the cars move faster.

---

## ⬇️ Installation
```bash
1. **Clone the repository:**
git clone https://github.com/Rachitbasnet4/Turtle-Crossing-Game.git
cd Turtle-Crossing-Game
2. (Optional but recommended) Create a virtual environment:
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
3. Install dependencies (if any):
pip install -r requirements.txt
```
Note: This game only uses Python's standard library (turtle), so no additional packages are required.

---

▶️ How to Run

Run the main game script:
```bash
python main.py
```
🎹 Controls
1. Up Arrow: Move the turtle forward

---

🏆 Features

1. Player-controlled turtle character
2. Randomly generated cars moving across the screen
3. Increasing difficulty as levels progress
4. Collision detection and Game Over screen
5. Level tracking with scoreboard

---

📂 Project Structure
```bash
turtle_crossing_game/
│
├─ main.py             # Main game loop
├─ player.py           # Player class
├─ car_manager.py      # CarManager class
├─ scoreboard.py       # Scoreboard class
├─ requirements.txt    # Dependencies (optional)
├─ README.md           # Project description
└─ .gitignore          # Git ignore file
```
📜 License

This project is open-source and free to use.

---

Made with ❤️ by Rachit Basnet
