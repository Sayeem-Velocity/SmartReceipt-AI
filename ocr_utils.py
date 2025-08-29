import base64
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage, SystemMessage
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Initialize Gemini LLM via LangChain
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-pro",
    temperature=0,
    max_output_tokens=2048,
    google_api_key=GOOGLE_API_KEY
)

# Strict but flexible system prompt
system_prompt = """
You are a strict OCR analyst specialized in receipts.

- Extract ALL text from the uploaded receipt image.
- Organize it into a structured plain-text receipt format.
- Follow this general structure, but include extra sections if they exist in the receipt:

===============================
          {STORE NAME}
{STORE ADDRESS or LOCATION}
{PHONE (if present)}
===============================

{ORDER INFO: Order #, Table, Party size, Server, Time, Date}

-------------------------------
Items:
{QTY}  {ITEM NAME}              {PRICE}
...
-------------------------------

{ANY SUBTOTALS (if present)}

Subtotal:                       {SUBTOTAL}
Tax:                            {TAX}
TOTAL:                          {TOTAL}
-------------------------------

{EXTRA SECTIONS: e.g., Gratuity, Discounts, Payment method}

{DATE & TIME again if present}

{FOOTER MESSAGES like "Thank you", "Visit again", etc.}
===============================

Rules:
- Keep spacing aligned so amounts are right-justified.
- Do not remove or skip fields that exist on the receipt (like gratuity suggestions).
- If a section is missing in the receipt, simply omit it.
- Do not use Markdown, JSON, or explanations — only the plain structured receipt text.
- TOTAL must always be uppercase.
- If no receipt detected, reply: No receipt detected
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
