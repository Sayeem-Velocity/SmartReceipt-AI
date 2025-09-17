import base64
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage, SystemMessage
from groq import Groq

# Load API keys
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-pro",
    temperature=0,
    max_output_tokens=2048,
    google_api_key=GOOGLE_API_KEY
)

# Groq client for Whisper
groq_client = Groq(api_key=GROQ_API_KEY)

# System prompt with strict splitting rules
system_prompt = """
You are a strict OCR analyst specialized in receipts.

- Extract ALL text from the uploaded receipt image or provided transcription and represent the text exactly like the receipt (keep spacing/alignment).
- Do not remove or skip fields that exist on the receipt.
- Keep spacing aligned, totals right-justified.
- TOTAL must always be uppercase.
- If no receipt detected, reply: No receipt detected.

--- SPLIT BILL INSTRUCTION ---
If the user requests to split the bill (e.g., "split among 4", "divide bill in four", "split for five people", "guest 3", "3 persons", "two friends", etc.):
1. Accept both digits (1, 2, 3, 4, etc.) and words ("one", "two", "three", "four", etc.).
2. Extract the TOTAL from the receipt.
3. Divide TOTAL by the requested number of persons.
4. At the END of the receipt output, strictly append in this format:

---
Split Bill (N persons): X.XX each
---

Where N is the number of persons and X.XX is the per-person share.
If no split is requested, do not add anything.
"""

def extract_receipt_text(uploaded_file):
    """Convert uploaded receipt image to structured text using Gemini."""
    img_bytes = uploaded_file.getvalue()
    img_base64 = base64.b64encode(img_bytes).decode("utf-8")

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=[
            {"type": "text", "text": "Extract the receipt text in structured plain text."},
            {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{img_base64}"}}
        ])
    ]
    response = llm.invoke(messages)
    return response.content

def extract_from_text(text_input: str):
    """Send raw text (from transcription or manual input) to Gemini OCR pipeline."""
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=text_input)
    ]
    response = llm.invoke(messages)
    return response.content

def transcribe_audio(file_path: str) -> str:
    """Transcribe audio in English using Groq Whisper API."""
    with open(file_path, "rb") as f:
        file_bytes = f.read()

    transcription = groq_client.audio.transcriptions.create(
        file=(file_path, file_bytes),
        model="whisper-large-v3",
        response_format="verbose_json",
        language="en"  # Force transcription output in English
    )

    if hasattr(transcription, "text"):
        return transcription.text
    elif isinstance(transcription, dict):
        return transcription.get("text") or transcription.get("transcription") or ""
    return str(transcription)
