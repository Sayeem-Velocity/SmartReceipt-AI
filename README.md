# SmartReceipt AI

**SmartReceipt AI** is a receipt OCR extractor built with **Streamlit** and **Google Gemini (via LangChain)**.
It allows users to upload receipt images and converts them into a **structured plain-text receipt format**, preserving store info, order details, items, totals, gratuity, and footers.

---

## Features

* Upload a receipt image (`.jpg`, `.jpeg`, `.png`)
* Extract **all visible text** using Google Gemini multimodal model
* Convert unstructured OCR into a **receipt-style structured layout**
* Preserve store details, order info, items, totals, gratuity, and footer messages
* Chat-like interface with conversation history
* Export extracted receipts to `.txt` files for easy use

---

## Project Structure

```
.
├── app.py            # Streamlit UI (upload, display, export)
├── ocr_utils.py      # Gemini OCR + formatting logic
├── requirements.txt  # Python dependencies
├── .env              # Environment variables (API key)
└── README.md         # Documentation
```

---

## Requirements

* Python 3.10 or higher
* A Google Gemini API key (obtain from [https://aistudio.google.com/](https://aistudio.google.com/))

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

4. Create a `.env` file in the project root and add your Gemini API key:

   ```
   GOOGLE_API_KEY=your_google_gemini_api_key_here
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

1. Upload a receipt image (JPG or PNG).
2. The extracted **structured text receipt** will appear in the output area.
3. Use the **Download as TXT** button to export the result.

---

## Notes

* The system prompt is tuned for **receipts** only.
* If no receipt is detected, the model will return: `No receipt detected`.
* Model output is plain text (no JSON/Markdown).
* Totals are always displayed in uppercase (`TOTAL`).

---

## Support

For issues, questions, or collaboration, contact:
**[syaeem26s@gmail.com](mailto:syaeem26s@gmail.com)**

---

