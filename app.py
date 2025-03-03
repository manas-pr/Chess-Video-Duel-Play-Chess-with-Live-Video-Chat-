import streamlit as st
import chess
import chess.svg
import streamlit.components.v1 as components
from streamlit_webrtc import webrtc_streamer
import av

# Initialize game state
if 'board' not in st.session_state:
    st.session_state.board = chess.Board()

st.title("♟️ Chess Video Duel 🎥")
st.subheader("Play Chess with Live Video Chat!")

# Display Chess Board
board_svg = chess.svg.board(st.session_state.board)
components.html(board_svg, height=400)

# Move Input
move = st.text_input("Enter your move (e.g., e2e4):")
if st.button("Make Move"):
    try:
        st.session_state.board.push(chess.Move.from_uci(move))
    except:
        st.error("Invalid move! Try again.")

# WebRTC Video Call
st.header("🎥 Video Call with Opponent")
def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")
    return av.VideoFrame.from_ndarray(img, format="bgr24")

webrtc_streamer(key="chess-video", video_frame_callback=video_frame_callback)

# Reset Game
if st.button("Reset Game"):
    st.session_state.board = chess.Board()
