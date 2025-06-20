# 🎨 Vistora - AI-Powered Image Generator

Vistora is a full-stack AI web application that transforms your text prompts into stunning, high-quality visuals using **Stable Diffusion XL (SDXL)**. Built with security, extensibility, and user experience in mind.

![Thumbnail](static/assets/vistora_thumbnail.png)

---

## 🚀 Features

- ✅ Secure **User Login & Registration**
- 🎯 **Credits System** to manage usage limits
- 📨 **Email Notifications** for generated images
- 🖼️ **Real-time Image Generation** (Hugging Face SDXL)
- 📁 **Prompt History**, Batch Downloads, Auto Cleanup
- 🛠️ **Admin Dashboard** (Manage users, refill credits)
- 🌗 Light/Dark **Theme Toggle**
- 🗣️ **Multilingual Prompt Support**
- ☁️ Cloud-Ready with **Firebase / S3** support

---

## 🧱 Tech Stack

- **Python 3.10+**
- **Streamlit** (UI)
- **Torch + Diffusers** (for SDXL)
- **SMTP** (Email alerts via Gmail)
- **JSON** (Data persistence)

---

## 📂 Project Structure

```bash
vistora/
├── app.py                    # Main Streamlit app
├── utils/
│   ├── auth.py              # Login, registration, password logic
│   ├── credits.py           # Credit management system
│   ├── emailer.py           # Email notification module
│   ├── admin.py             # Admin dashboard features
│   └── generator.py         # Image generation via SDXL
├── static/
│   ├── generated/           # Output images
│   └── assets/              # Thumbnails, logos
├── data/
│   ├── users.json           # User credentials & credit tracking
│   └── prompt_history.json  # Saved prompt logs
├── .streamlit/config.toml   # Custom theme config
├── requirements.txt         # Python dependencies
└── README.md
```

---

## 🔐 Setup Instructions

1. **Clone the repo**
```bash
git clone https://github.com/yourusername/vistora.git
cd vistora
```

2. **Create a virtual environment & install dependencies**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

3. **Add your Hugging Face Access Token**
In `generator.py`, replace:
```python
HF_TOKEN = "your_token_here"
```
Get your token from: [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

4. **Run the app**
```bash
streamlit run app.py
```

> ⚠️ Make sure you have GPU support for optimal image generation speeds.

---

## ✉️ Gmail SMTP Setup (for email alerts)
Enable "Less Secure Apps" (or use an App Password) and set credentials in `emailer.py`:
```python
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"
```

---

## 📸 Example Output

![Example](static/generated/example_vistora_output.png)

---

## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

---

## 📃 License
[MIT License](LICENSE)

---

## 📌 Credits
- [Hugging Face Diffusers](https://huggingface.co/docs/diffusers/index)
- [Streamlit](https://streamlit.io/)
- [PyTorch](https://pytorch.org/)

---

### 👤 Built with ❤️ by Fahad Nasir — "Visualize your imagination with **Vistora**"

---
