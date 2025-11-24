import random
import streamlit as st

# Game settings (same as your original)
COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = 4


def generate_code():
    """Generate a random secret code."""
    return [random.choice(COLORS) for _ in range(CODE_LENGTH)]


def check_code(guess, real_code):
    """Return (correct_pos, incorrect_pos) like in your original code."""
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        color_counts[color] = color_counts.get(color, 0) + 1

    # First pass: correct positions
    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1
            color_counts[guess_color] -= 1

    # Second pass: correct color, wrong position
    for guess_color, real_color in zip(guess, real_code):
        if guess_color != real_color and color_counts.get(guess_color, 0) > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1

    return correct_pos, incorrect_pos


def init_game():
    """Initialize game state in Streamlit session_state."""
    st.session_state.code = generate_code()
    st.session_state.history = []  # list of dicts: {guess, correct_pos, incorrect_pos}
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.session_state.status_message = ""


# Initialize game on first load
if "code" not in st.session_state:
    init_game()

st.title("Mastermind – Color Code Breaker 🎯")

st.write(
    """
Welcome to **Mastermind**!  
Try to guess the secret code of **4 colors** in at most **10 tries**.
"""
)

st.markdown(
    """
**Colors:**  
- `R` = Red  
- `G` = Green  
- `B` = Blue  
- `Y` = Yellow  
- `W` = White  
- `O` = Orange  
"""
)

# Sidebar info
st.sidebar.header("Game Info")
st.sidebar.write(f"Available colors: {', '.join(COLORS)}")
st.sidebar.write(f"Code length: {CODE_LENGTH}")
st.sidebar.write(f"Max tries: {TRIES}")

# New game button
if st.button("🔁 New Game"):
    init_game()

st.markdown("---")

# Disable input if game is over
if st.session_state.game_over:
    st.info(st.session_state.status_message)
else:
    st.subheader(f"Attempt {st.session_state.attempts + 1} of {TRIES}")

    st.write("Select your guess:")

    cols = st.columns(CODE_LENGTH)
    current_guess = []

    for i in range(CODE_LENGTH):
        with cols[i]:
            choice = st.selectbox(
                f"Position {i + 1}",
                options=[""] + COLORS,
                key=f"pos_{i}",
                index=0,  # default empty
            )
            current_guess.append(choice)

    submit = st.button("✅ Submit Guess")

    if submit:
        if "" in current_guess:
            st.warning("Please select a color for each position before submitting.")
        else:
            st.session_state.attempts += 1
            correct_pos, incorrect_pos = check_code(current_guess, st.session_state.code)

            st.session_state.history.append(
                {
                    "attempt": st.session_state.attempts,
                    "guess": current_guess.copy(),
                    "correct_pos": correct_pos,
                    "incorrect_pos": incorrect_pos,
                }
            )

            if correct_pos == CODE_LENGTH:
                st.session_state.game_over = True
                st.session_state.status_message = (
                    f"🎉 You cracked the code in {st.session_state.attempts} tries!"
                )
            elif st.session_state.attempts >= TRIES:
                st.session_state.game_over = True
                code_str = " ".join(st.session_state.code)
                st.session_state.status_message = (
                    f"❌ Game over! You ran out of tries.\n\n"
                    f"The secret code was: **{code_str}**"
                )

# Show history
st.markdown("---")
st.subheader("Guess History")

if not st.session_state.history:
    st.write("No guesses yet. Make your first guess!")
else:
    for entry in st.session_state.history[::-1]:
        guess_str = " ".join(entry["guess"])
        st.write(
            f"**Attempt {entry['attempt']}** – Guess: `{guess_str}` | "
            f"✅ Correct position: **{entry['correct_pos']}** | "
            f"🎯 Correct color, wrong position: **{entry['incorrect_pos']}**"
        )

# Show status at the bottom
if st.session_state.game_over:
    st.success(st.session_state.status_message)
