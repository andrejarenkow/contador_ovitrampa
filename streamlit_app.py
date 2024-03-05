import streamlit as st
from streamlit_webrtc import webrtc_streamer

def main():
    st.title("Webcam Stream")

    webrtc_ctx = webrtc_streamer(key="example", video_transformer_factory=None)

    if webrtc_ctx.video_receiver:
        st.write("Capturing...")
        video_frame = webrtc_ctx.video_receiver.get_frame()
        st.image(video_frame)

if __name__ == "__main__":
    main()
