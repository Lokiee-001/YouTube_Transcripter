# 🎙️ YouTube_Transcripter

**YouTube_Transcripter** is a full-stack web application built with Flask that allows users to extract and summarize transcripts from YouTube videos. With a clean UI, login/register functionality, and customizable routes, this app makes it easy to convert video content into readable and summarized text.

---

## 🌟 Features

- 🔗 **YouTube Transcript Summarization**  
  Paste any YouTube video link and get a concise summary of the transcript.

- 👥 **User Authentication System**  
  Includes login, registration, and logout functionality with session management.

- ⚡ **Flash Messaging**  
  Instant feedback for user actions like login, logout, and errors.

- 📋 **Multiple Routes**  
  - `/` or `/index.html` - Home  
  - `/summarize` - Summarization action  
  - `/login` and `/register` - Auth routes  
  - `/about`, `/dashboard`, `/contact` - Informational pages

- 🧠 **Custom Summarization Logic**  
  Uses a modular `utils/summarizer.py` for easy integration with different NLP models.

---

## 🛠️ Tech Stack

| Layer       | Technology             |
|-------------|------------------------|
| Frontend    | HTML, CSS (Bootstrap optional) |
| Backend     | Python (Flask)         |
| Summarizer  | Custom summarizer using `get_summary()` in Python |
| Auth        | Flask Sessions         |

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.x installed
- `pip` (Python package manager)

### 📦 Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/YouTube_Transcripter.git
cd YouTube_Transcripter
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the app

bash
Copy
Edit
python app.py
Open in browser

cpp
Copy
Edit
http://127.0.0.1:5000
📂 Project Structure
csharp
Copy
Edit
YouTube_Transcripter/
├── app.py                      # Main Flask application
├── requirements.txt
├── README.md                   # This file
│
├── utils/
│   └── summarizer.py           # Contains get_summary() logic
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── about.html
│   ├── contact.html
│   └── dashboard.html
│
└── static/                     # (Optional) CSS/JS assets
🔑 Environment Variables
You can optionally set a secure Flask secret key using a .env file or export command:

bash
Copy
Edit
export FLASK_SECRET_KEY=your-secret-key
Defaults to 'dev-secret-key' if not set.

⚠️ Notes
This version uses a dummy in-memory user store (Python dictionary).
✅ For production, replace it with a proper database (e.g., SQLite, PostgreSQL) and hashed passwords.

🧠 Future Enhancements
Integrate actual YouTube Transcript API

Switch to database-backed user authentication

Use NLP models like T5, BART, or GPT for summarization

UI improvements with Tailwind or Bootstrap

Export summaries in PDF, DOCX formats

Add voice input support

Add video upload-to-transcript option

📷 Screenshots
Include screenshots of homepage, login page, and summarizer output

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss.

📄 License
This project is licensed under the MIT License.
See the LICENSE file for details.

🙌 Acknowledgements
Flask

YouTube Transcript API

Python & Open Source Community

📬 Contact
For feedback, collaboration, or questions:
📧 your.email@example.com
🔗 LinkedIn

yaml
Copy
Edit

---

Let me know if you want help generating a `requirements.txt`, a custom logo badge section, or sample `.![Screenshot 2025-04-13 010716](https://github.com/user-attachments/assets/0016f4b4-b7a9-4669-b26c-568ede58a6d4)
