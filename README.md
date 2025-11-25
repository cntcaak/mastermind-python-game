<p align="center">
  <img src="Mastermind%20python%20game.png" alt="Mastermind Python Project Banner" width="100%">
</p>

# 🎯 Mastermind — Python Game Project

A classic **Mastermind color code-breaking game** built completely in Python as my first programming project.  
I first created a **terminal-based (console) version**, and then expanded it into a **web version using Streamlit** so anyone can play it directly in a browser.

---

## 🧠 Game Concept

The computer generates a hidden code consisting of **4 colors**, randomly selected from a set of 6 possible colors:

`R = Red | G = Green | B = Blue | Y = Yellow | W = White | O = Orange`

Your goal is to guess the secret sequence within **10 attempts**.

After each guess, the game provides feedback:

| Feedback            | Meaning                                      |
|---------------------|----------------------------------------------|
| Correct positions   | Color is correct and in the correct position |
| Incorrect positions | Color is correct but in the wrong position   |

Example:
```text
Correct positions: 2
Incorrect positions: 1

🕹️ Play the Game Online

You can play the Mastermind game directly in your browser here:

👉 Play Now: https://mastermind-app-vrjyghel2eubzjc4mpytef.streamlit.app/

💻 Code Structure

This repository contains two versions of the game:

mastermind_console.py   # Original Python console-based version
app.py                  # Streamlit web app version


Console version (mastermind_console.py)

Pure Python

Runs in the terminal (VS Code / any terminal)

Handles input, validates guesses, provides feedback, and tracks attempts

Streamlit version (app.py)

Uses the same core game logic

Adds a browser-based UI with dropdowns for color selection

Shows guess history and feedback for each attempt

Includes a "New Game" button and stateful session handling

🛠️ Technologies Used
Technology	Purpose
Python	Game logic and core functionality
Streamlit	Interactive web interface
Git/GitHub	Version control and hosting
🚀 How to Run Locally
1️⃣ Clone the repository
git clone https://github.com/cntcaak?tab=repositories
cd mastermind-python-game


2️⃣ Run the console version
python mastermind_console.py


You can now play the game in your terminal by entering color codes like:

R G B Y
G G R W

3️⃣ Run the Streamlit (browser) version

Install Streamlit (if you don’t have it yet):

pip install streamlit


Then run:

streamlit run app.py


This will open the game in your browser (usually at http://localhost:8501).

📍 Features

✅ Random secret code generation

✅ Input validation for guesses

✅ Feedback on:

Correct positions

Correct colors in wrong positions

✅ Limited number of tries (10 attempts)

✅ Web UI with:

Color selection dropdowns

Guess history

Game status messages

New Game button

📚 What I Learned

Writing clean, reusable functions in Python

Using lists and dictionaries to manage game logic

Handling user input and validation in a console app

Converting a console program into a web app using Streamlit

Structuring a small project and publishing it on GitHub

🔗 Useful Links

🌐 Live Game: [STREAMLIT_APP_URL_HERE](https://mastermind-app-vrjyghel2eubzjc4mpytef.streamlit.app/)

📁 Repository: [GITHUB_REPO_URL_HERE](https://github.com/cntcaak?tab=repositories)

💼 LinkedIn: [LINKEDIN_URL_HERE](https://www.linkedin.com/in/cntcaak/)

🙌 Feedback & Contributions

I’m open to suggestions and improvements!

Found a bug?
→ Open an issue.

Have an idea (e.g., difficulty levels, more colors, scoring)?
→ Feel free to create a pull request.

If you like this project, consider ⭐ starring the repo — it really motivates me to keep learning and building.

👤 Author

Akber Ali Khan
Mechanical Engineer exploring Python, AI, and software development.
---

## 📸 Screenshots

### Console Version (VS Code / Terminal)
This is the original Python console-based gameplay.

![Console Screenshot](console_screenshot.png)

---

### Streamlit Web Version
Browser-based UI with dropdowns, game history, feedback, and restart button.

![Streamlit Screenshot](streamlit_screenshot.png)

---
