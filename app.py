import streamlit as st
from PIL import Image
from ocr_utils import extract_receipt_text

# ------------------ Streamlit UI ------------------
st.set_page_config(page_title="SmartReceipt AI", layout="centered")
st.title("SmartReceipt AI")
st.write("Upload a receipt image to extract text into a structured plain-text receipt.")

# Session state for caching
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "last_response" not in st.session_state:
    st.session_state.last_response = None
if "last_file" not in st.session_state:
    st.session_state.last_file = None

# File uploader
uploaded_file = st.file_uploader("Upload a receipt (JPG or PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Show uploaded image (fixed width)
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Receipt", width=400)

    # Only process if it's a new file
    if st.session_state.last_file != uploaded_file.name:
        with st.spinner("Processing receipt with Gemini..."):
            extracted_text = extract_receipt_text(uploaded_file)

        # Cache response
        st.session_state.last_response = extracted_text
        st.session_state.last_file = uploaded_file.name

        # Add to chat history
        st.session_state.chat_history.append(("You", "Uploaded a receipt"))
        st.session_state.chat_history.append(("Gemini", extracted_text))

# Show results
if st.session_state.last_response:
    st.subheader("Extracted Receipt Text")
    st.text_area("Gemini OCR Result", st.session_state.last_response, height=400)

    # Export button
    st.download_button(
        "Download Receipt as TXT",
        data=st.session_state.last_response,
        file_name="receipt_output.txt",
        mime="text/plain"
    )
