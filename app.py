import streamlit as st
from PIL import Image
from ocr_utils import extract_receipt_text, extract_from_text, transcribe_audio
from streamlit_mic_recorder import mic_recorder
import tempfile
import os

# ------------------ Streamlit UI ------------------
st.set_page_config(page_title="SmartReceipt AI", layout="centered")
st.title("SmartReceipt AI")
st.write("Provide your text or speech And upload a receipt image to extract structured plain-text.")

# Session state
if "user_text" not in st.session_state:
    st.session_state.user_text = ""
if "uploaded_image" not in st.session_state:
    st.session_state.uploaded_image = None
if "ocr_result" not in st.session_state:
    st.session_state.ocr_result = None

# ---------------- Input: User Text or Speech ----------------
st.subheader("Enter text or record speech")

# Text input field
st.session_state.user_text = st.text_area("Type your input here:", st.session_state.user_text, height=100)

# Mic recorder
audio = mic_recorder(
    start_prompt="Start Recording",
    stop_prompt="Stop Recording",
    just_once=True,
    use_container_width=True
)

if audio and "bytes" in audio:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
        tmp_file.write(audio["bytes"])
        tmp_path = tmp_file.name

    transcribed_text = transcribe_audio(tmp_path)
    st.session_state.user_text = transcribed_text
    st.text_area("Transcribed Text:", transcribed_text, height=100)
    os.remove(tmp_path)

# ---------------- Input: Receipt Image ----------------
uploaded_file = st.file_uploader("Upload a receipt (JPG/PNG)", type=["jpg", "jpeg", "png"])
if uploaded_file:
    st.session_state.uploaded_image = uploaded_file
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Receipt", width=400)

# ---------------- Run OCR ----------------
if st.button("Run OCR"):
    if st.session_state.user_text.strip() and st.session_state.uploaded_image:
        with st.spinner("Processing..."):
            ocr_text = extract_receipt_text(st.session_state.uploaded_image)
            model_input_text = st.session_state.user_text
            final_result = extract_from_text(f"User Prompt: {model_input_text}\n\n{ocr_text}")
            st.session_state.ocr_result = final_result
    else:
        st.warning("Please provide both a user prompt (text or speech) and a receipt image.")

# ---------------- Show Result ----------------
if st.session_state.ocr_result:
    st.subheader("Extracted Receipt Text")
    st.text_area("OCR Result", st.session_state.ocr_result, height=400)
    st.download_button(
        "Download Receipt as TXT",
        data=st.session_state.ocr_result,
        file_name="receipt_output.txt",
        mime="text/plain"
    )
