Perfect ✅ I’ll write you a clean **README.md** for your project with setup instructions, usage, requirements, and your contact info.

---

## `README.md`

```markdown
# SmartReceipt AI

This project is a **SmartReceipt AI** built with **Google Gemini (via LangChain)** and **Streamlit**.  
It allows you to upload a receipt image and converts it into a **structured plain-text receipt format** (store details, order info, items, totals, gratuity, etc.).  

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

## ⚙️ Installation

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

## 📋 Example Output

```
===============================
          GRAND LUX CAFE
Roosevelt Field
===============================

Order #: 0480    Table: 101    Party: 3
Server: STEPHEN R    SvrCk: 4
Date: 04/25/15   Time: 16:43

-------------------------------
Items:
1  Coffee                     2.95
1  Chicken Parmesan          17.95
1  Prime Top Sirloin         25.95
1  The Bacon-Cheese Burger   13.95
1  Coffee                     2.95
-------------------------------

Sub Total:                   63.75
Tax:                          5.50
TOTAL:                       69.25
-------------------------------

Gratuity Not Included
Suggested Gratuity:
20%                          13.85
18%                          12.47
15%                          10.39

Date: 04/25/15   Time: 17:42

It's been a pleasure to serve you.
Thank you for dining with us
===============================
```

---

## 📧 Contact

For any questions or contributions, feel free to reach out:
📩 **[syaeem26s@gmail.com](mailto:syaeem26s@gmail.com)**

---
