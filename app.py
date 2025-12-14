import streamlit as st
import random

st.set_page_config(page_title="Rock Paper Scissors", layout="centered")

# ---------------- GAME LOGIC ----------------

def decide_winner(player, computer):
    if player == computer:
        return "draw"
    if (
        (player == "Rock" and computer == "Scissors") or
        (player == "Paper" and computer == "Rock") or
        (player == "Scissors" and computer == "Paper")
    ):
        return "player"
    return "computer"


def reset_game():
    st.session_state.player_score = 0
    st.session_state.computer_score = 0
    st.session_state.last_player_move = None
    st.session_state.last_computer_move = None
    st.session_state.result = None


# ---------------- SESSION STATE ----------------

if "player_score" not in st.session_state:
    st.session_state.player_score = 0

if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0

if "last_player_move" not in st.session_state:
    st.session_state.last_player_move = None

if "last_computer_move" not in st.session_state:
    st.session_state.last_computer_move = None

if "result" not in st.session_state:
    st.session_state.result = None


# ---------------- UI ----------------

st.title("✊✋✌️ Rock Paper Scissors")

# ---- Scoreboard ----
col1, col2 = st.columns(2)
with col1:
    st.metric("You", st.session_state.player_score)
with col2:
    st.metric("Computer", st.session_state.computer_score)

st.divider()

st.subheader("Make your move")

choices = ["Rock", "Paper", "Scissors"]
cols = st.columns(3)

for i, choice in enumerate(choices):
    with cols[i]:
        if st.button(choice):
            computer_choice = random.choice(choices)

            st.session_state.last_player_move = choice
            st.session_state.last_computer_move = computer_choice

            outcome = decide_winner(choice, computer_choice)
            st.session_state.result = outcome

            if outcome == "player":
                st.session_state.player_score += 1
            elif outcome == "computer":
                st.session_state.computer_score += 1


# ---- Show Moves ----
if st.session_state.last_player_move:
    st.subheader("Last Round")
    st.write(f"**You played:** {st.session_state.last_player_move}")
    st.write(f"**Computer played:** {st.session_state.last_computer_move}")

    if st.session_state.result == "draw":
        st.info("🤝 It's a Draw!")
    elif st.session_state.result == "player":
        st.success("🎉 You Win This Round!")
    else:
        st.error("💻 Computer Wins This Round!")

st.divider()

# ---- Restart ----
st.button("Restart Game", on_click=reset_game)
