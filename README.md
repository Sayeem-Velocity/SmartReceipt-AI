# SmartReceipt AI

**SmartReceipt AI** is a multimodal receipt OCR extractor built with **Streamlit**, **Google Gemini (via LangChain)**, and **Groq Whisper** for audio transcription.
It allows users to upload receipt images or provide speech input and converts them into a **structured plain-text receipt format**, preserving store info, order details, items, totals, gratuity, footers, and optionally splitting bills among guests.

---

## Features

* Upload receipt images (`.jpg`, `.jpeg`, `.png`) or provide voice input for instructions.
* Transcribe speech into English using **Groq Whisper**.
* Extract **all visible text** from receipts using **Google Gemini multimodal model**.
* Convert unstructured OCR into a **receipt-style structured layout**.
* Preserve:

  * Store details
  * Order information (order #, table, party size, server, date/time)
  * Items with quantity and price
  * Subtotals, tax, TOTAL
  * Extra sections (gratuity, discounts, payment method)
  * Footer messages (e.g., “Thank you”, “Visit again”)
* **Split the bill** automatically when requested, supporting both numeric and word formats (`4`, `four`, `five persons`, `guest 3`, etc.).
* Chat-like interface with conversation memory and continuous input.
* Export extracted receipts to `.txt` files for easy use.

---

## Project Structure

```
.
├── app.py            # Streamlit UI: upload, audio input, display, export
├── ocr_utils.py      # Gemini OCR + Groq Whisper transcription + split bill logic
├── requirements.txt  # Python dependencies
├── .env              # Environment variables (API keys)
└── README.md         # Project documentation
```

---

## Requirements

* Python 3.10 or higher
* Google Gemini API key (obtain from [https://aistudio.google.com/](https://aistudio.google.com/))
* Groq API key (for Whisper transcription)

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/receipt-ocr-bot.git
   cd receipt-ocr-bot
   ```

2. Create and activate a virtual environment (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux/Mac
   venv\Scripts\activate         # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your API keys:

   ```
   GOOGLE_API_KEY=your_google_gemini_api_key_here
   GROQ_API_KEY=your_groq_api_key_here
   ```

---

## Running the Application

Start the Streamlit app:

```bash
streamlit run app.py
```

The app will launch in your browser at:

```
http://localhost:8501
```

---

## Usage

1. **Text or Voice Input**:

   * Type instructions or speech (e.g., “Split the bill among 4”).
   * Optionally, record speech using the mini recorder — the app will transcribe to English automatically.
2. **Upload Receipt**:

   * Upload a receipt image (`.jpg`, `.jpeg`, `.png`).
3. **Process OCR**:

   * Click **Analyze Receipt**.
   * The app extracts all receipt details and formats them in a structured plain-text layout.
4. **Split Bill (Optional)**:

   * If the user requested a split in text/speech, the output automatically shows per-person amounts at the end of the receipt.
5. **Download Result**:

   * Use the **Download as TXT** button to export the structured receipt.

---

## Notes

* The system prompt is strictly tuned for **receipts only**.
* TOTAL amounts are always displayed in uppercase.
* Bill splitting supports **both numbers and words** (`4`, `four`, `three people`, `guest 2` etc.).
* Model output is **plain text**; no JSON or Markdown.
* If no receipt is detected, the model will return: `No receipt detected`.

---

## Production Workflow

1. **Audio Input (Optional)** → Transcribed by **Groq Whisper** → Text prompt.
2. **Receipt Image Upload** → OCR by **Google Gemini** → Raw text.
3. **Structured Formatting** → Apply receipt layout rules and alignment.
4. **Split Bill Logic** → Handled automatically by the system prompt when requested.
5. **Display & Export** → Streamlit shows structured receipt + download option.

---

## Support

For issues, questions, or collaboration, contact:
**[syaeem26s@gmail.com](mailto:syaeem26s@gmail.com)**

---

If you want, I can also **update your `app.py` in a fully production-ready style** with:

* Clean UI
* Mini voice recorder + text input combined
* Auto split bill handled via system prompt
* Continuous session state for chat-like experience
