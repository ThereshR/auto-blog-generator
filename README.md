# 📝 Auto Blog Generator

An AI-powered backend system that automates blog generation based on trending topics, keyword research, and web research. This project leverages trending data, performs intelligent research, and generates blog content using local LLMs — all in a single streamlined Python pipeline.

---

## 🚀 What It Does

This tool performs the full workflow of automated blog creation:
1. **Fetches trending topics** using Google Trends via SerpAPI
2. **Performs keyword research** to identify SEO-rich terms
3. **Selects the most relevant topic** using smart heuristics or AI logic
4. **Performs web research** using SerpAPI-powered Google Search
5. **Generates blog content** (500+ words) using Ollama with the `gemma:2b` model

Ideal for content creators, SEO marketers, and developers building content automation tools.

---

## 📁 Folder Structure
my_blog_project/
├── data/ # Output blog data
├── models/
│ └── blog_writer.py # Uses Ollama subprocess to generate blogs
├── utils/
│ ├── trends.py # Fetch trending topics via SerpAPI
│ └── research.py # Conducts related web research
├── generate_blog.py # Orchestrates the entire blog pipeline
├── requirements.txt
├── .gitignore
├── README.md
└── LICENSE  


---

## 🧠 Tech Used

- **Python 3.10+**
- **Ollama** with `gemma:2b` model for LLM-powered blog writing
- **SerpAPI** for trending topics & research
- **Standard libraries**: `subprocess`, `requests`, `json`, `os`, `datetime`

---

## ⚙️ Setup Instructions

### 1. Clone This Repo
```bash
git clone https://github.com/YOUR_USERNAME/auto-blog-generator.git
cd auto-blog-generator


****Install Requirements****
bash
pip install -r requirements.txt


****Add Your API Keys****
Open utils/trends.py and utils/research.py

Replace your_serpapi_key with your actual SerpAPI key

(Recommended) Use a .env file or a secure config manager


****Run the Generator*****
bash
python generate_blog.py


**This will:**
Print trending topics
Fetch keyword suggestions
Perform related research
Generate a blog post (~500+ words)

✅ Requirements
Python ≥ 3.10

Ollama with gemma:2b model downloaded

SerpAPI key for search & trends



🔒 Security Notes
All secrets should be stored in environment variables or ignored via .gitignore

Sensitive files like API keys should never be committed to version control

📄 License
This project is licensed under the MIT License.


👨‍💻 Author
Theresh I
🔗 GitHub

