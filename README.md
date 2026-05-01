# ⚔️ Slay The Terminal

A fan-made, terminal-based RPG game inspired by Slay the Spire. Built with pure Python — no libraries, no frameworks, just code.

> "It is a fanmade game, so have fun"

---

## 🎮 How To Play

### Requirements
- Python 3.x

### Run The Game
```bash
cd src
python main.py
```

### Controls
When it's your turn, choose an action by typing a number:
```
1. Attack  — deal damage to the enemy
2. Block   — gain shield to absorb incoming damage
3. Skip    — skip your turn (you'll take full damage)
```

---

## 🗂️ Project Structure

```
slay_the_terminal/
├── src/
│   ├── main.py      # entry point, title screen, game start
│   ├── player.py    # Player class with stats and actions
│   ├── enemy.py     # Enemy class with intent system
│   └── combat.py    # combat loop logic
└── README.md
```

---

## ⚔️ Current Features

- Turn-based combat system
- Player stats: HP, Block, Damage
- Enemy intent system (shows what enemy will do next turn)
- Block mechanic (absorbs damage before HP)
- Win/Lose conditions

---

## 🚧 Planned Features

- [ ] Card system (deck building)
- [ ] Multiple enemy types
- [ ] XP and leveling system
- [ ] Multiple floors/areas
- [ ] Boss fights
- [ ] Save system

---

## 👨‍💻 Author

Made by Saidhon4ik — built from scratch as a Python learning project.
