**AI BOOK PUBLICATION**

This project is a lightweight AI-powered reviewer system designed to automate the evaluation of content for an automation-focused book. It offers voice-enabled input/output, agentic pipeline orchestration, version tracking, and semantic understanding to streamline AI-assisted content iteration.
🚀 Live 
👉 Soon....
Streamlit Demo
Preview link : [https://drive.google.com/file/d/1Mj_CX5GGpW3Sq9fPrPv8YHgmHBjDt7gJ/view?usp=sharing]

---

##  process Implemented 

-  **Automated Screenshot & Text Extraction**: Captures page screenshots using Playwright and extracts text using beautifulsoup.
-  **Chapter Content Generation**: Sends the extracted text (chapter.txt) to Gemini API for rewriting into a polished chapter .
-  **AI Reviewer**: sends the AI-written chapter for aireviewer which reviews consistency, tone, and grammar.
-  **Interactive Streamlit UI**: Allows human-in-the-loop editing and final approval of the AI-generated content.
-  **Final Storage**: Saves the edited and approved chapter text for publication.

---
---

## Coming Soon

-  **Voice Input/Output Support** :(via Whisper ASR and ElevenLabs TTS)
-  **Semantic Search** :using Embeddings + FAISS/ChromaDB
-  **deploying**: Streamlit Deployement
---
Tech Stack

**Web Automation**: Playwright
**text_extraction**: Beautifulsoup
**LLM**: gemini-1.5-flash
**Frontend**: Streamlit

Deployment
(Upcoming: Streamlit Cloud)


How It Works
**Automated Screenshot Capture**
The system uses Playwright to open a web page and capture screenshots of book content.
**Text Extraction from Image**
Screenshots are processed using Beautifulsoup to extract text, saved as chapter.txt.
**AI-Powered Rewriting with Gemini**
The raw chapter text is sent to Google Gemini for intelligent rewriting based on defined prompts.
**Automated Review System**
An AI Reviewer Agent analyzes the rewritten content and offers constructive suggestions.
**Human-in-the-Loop Review with Streamlit**
A Streamlit web interface displays the AI-reviewed text, allowing humans to make final edits and save the approved version as chapter_final.txt.


📂 Folder Structure
```bash
AI_Book_Publication/
├── Python/
├── datafolder/
│   └── data/
├── app.py
├── main.py
├── scrapper.py
├── aiwriter.py
├── aireviewer.py
├── requirements.txt
├── README.md
└── .gitignore
```
## 🚀 Getting Started

### 🧰 Prerequisites
- Python 3.9+
- Git
- Gemini API key

### ⚙️ Installation

```bash
```bash
# Clone the repo
git clone https://github.com/Ruthvik11/AI_Book_publication.git
cd AI_Book_publication

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set your OpenAI API key
echo Gemini_API_KEY=your-api-key-here > .env


# Run the frontend
streamlit run app.py```



🤝 Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes. For major changes, open an issue first to discuss.


