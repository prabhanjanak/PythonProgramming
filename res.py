import streamlit as st
import tempfile
from pydub import AudioSegment
from pydub.utils import which
from transformers import pipeline
import imageio
import os

# Configure pydub to use the FFmpeg installed by imageio
ffmpeg_path = imageio.plugins.ffmpeg.download()
AudioSegment.converter = ffmpeg_path

# Title of the app
st.title("Video Summarizer App")
st.write("Upload a video file to get a summarized transcript.")

# Step 1: Upload Video File
uploaded_file = st.file_uploader("Upload your video file", type=["mp4", "mov", "avi", "mkv"])

if uploaded_file is not None:
    st.video(uploaded_file)

    # Step 2: Extract Audio from Video
    with st.spinner("Processing video and extracting audio..."):
        temp_video_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
        temp_video_file.write(uploaded_file.read())

        audio_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        audio = AudioSegment.from_file(temp_video_file.name)
        audio.export(audio_file.name, format="mp3")

    st.success("Audio extracted successfully!")

    # Step 3: Transcribe Audio
    st.write("### Step 1: Transcription")
    with st.spinner("Transcribing audio using Whisper..."):
        asr_pipeline = pipeline("automatic-speech-recognition", model="openai/whisper-base")
        transcription = asr_pipeline(audio_file.name)
        transcript_text = transcription['text']

    st.write("#### Transcript:")
    st.text_area("Full Transcript", transcript_text, height=200)

    # Step 4: Summarize Transcript
    st.write("### Step 2: Summarization")
    with st.spinner("Summarizing the transcript..."):
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        summary = summarizer(transcript_text, max_length=150, min_length=40, do_sample=False)
        summarized_text = summary[0]['summary_text']

    st.write("#### Summarized Transcript:")
    st.text_area("Summary", summarized_text, height=150)

    # Cleanup temporary files
    os.remove(temp_video_file.name)
    os.remove(audio_file.name)
    st.success("Process completed successfully!")
