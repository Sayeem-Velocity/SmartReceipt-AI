# SmartReceipt AI

This project is a **SmartReceipt AI** built with **Google Gemini (via LangChain)** and **Streamlit**.  
It allows you to upload a receipt image and converts it into a **structured plain-text receipt format** (store details, order info, items, totals, gratuity, etc.).  

---

## Features
- Upload receipt images (`.jpg`, `.jpeg`, `.png`)
- Extract **all text** using Gemini multimodal model
- Format into a **structured receipt-style layout**
- Preserve **items, totals, tax, gratuity, and footer messages**
- Display results in a clean Streamlit interface
- Export receipt text as a `.txt` file

---

## Project Structure
```

receipt-ocr-bot/
│── app.py              # Streamlit app (UI)
│── ocr\_utils.py        # OCR + Gemini logic
│── requirements.txt    # Dependencies
│── .env                # API key (Google Gemini)
│── README.md

````

---

## Installation

1. **Clone this repo**  
   ```bash
   git clone https://github.com/your-username/receipt-ocr-bot.git
   cd receipt-ocr-bot
````

2. **Create and activate virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your API key**

   * Create a `.env` file in the project root:

     ```
     GOOGLE_API_KEY=your_google_gemini_api_key_here
     ```

---

## Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

Open the local URL (e.g., `http://localhost:8501`) in your browser.

1. Upload a receipt image (JPG or PNG).
2. The extracted **structured text** will appear in the output box.
3. You can download the result as `receipt_output.txt`.

---

## Contact

For any questions or contributions, feel free to reach out:
**[syaeem26s@gmail.com](mailto:syaeem26s@gmail.com)**

---

