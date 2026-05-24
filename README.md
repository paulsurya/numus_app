# 💸 NumuS

> *Track your coins before they ghost you.*

---

```
███╗   ██╗██╗   ██╗███╗   ███╗██╗   ██╗███████╗
████╗  ██║██║   ██║████╗ ████║██║   ██║██╔════╝
██╔██╗ ██║██║   ██║██╔████╔██║██║   ██║███████╗
██║╚██╗██║██║   ██║██║╚██╔╝██║██║   ██║╚════██║
██║ ╚████║╚██████╔╝██║ ╚═╝ ██║╚██████╔╝███████║
╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝ ╚═════╝ ╚══════╝
```

**NumuS** is a no-nonsense personal finance tracker built with Flask. Log your spending, see where your money's actually going, and maybe cry a little — but at least you'll know *why*.

---

## ✨ What It Does

| Feature | Status |
|---|---|
| 📥 Log expenses & incomes | ✅ Done |
| 📊 Interactive Dashboard | ✅ Done |
| 🏷️ Categories (Food, Travel, Custom) | ✅ Done |
| 💅 Styled with Tailwind CDN | ✅ Done |
| 🔐 User auth with Flask-Login | ✅ Done |

---

## 🛠️ Tech Stack

- **Backend** — Flask (Python)
- **Styling** — Tailwind CSS via CDN *(because CSS files are the enemy)*
- **Auth** — Flask-Login + UserMixin
- **DB** — SQLAlchemy (SQLite by default)

---

## 🚀 Getting Started

### 1. Clone it

```bash
git clone https://github.com/paulsurya/numus_app.git
cd numus
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run it

```bash
flask run
```

Then open `http://localhost:5000` and start logging your poor financial decisions.

---

## 📁 Project Structure

```
numus_app/
├── instance/
│   └── database.db          # SQLite database lives here
├── numus/
│   ├── static/              # CSS, JS, images
│   ├── templates/
│   │   ├── base.html        # Layout wrapper
│   │   ├── dashboard.html   # The money charts page
│   │   ├── input.html       # Log your expenses/incomes
│   │   └── login.html       # Auth page
│   ├── views/
│   │   ├── __init__.py
│   │   ├── auth.py          # Login/register routes
│   │   ├── dashboard.py     # Dashboard routes
│   │   └── input.py         # Input routes
│   ├── __init__.py
│   └── models.py            # User table & DB models
├── app.py                   # Entry point
├── requirements.txt
└── README.md                # you are here
```

---

## 📦 Requirements

All dependencies are in `requirements.txt`. Just run:

```bash
pip install -r requirements.txt
```

No venv drama. No Docker. Just vibes and pip.

---

## 🗺️ Roadmap

- [ ] Charts that actually slap on the dashboard
- [ ] Budget limits per category
- [ ] Monthly summaries
- [ ] Export to CSV (so you can cry in Excel too)
- [ ] Dark mode (obviously)

---

## 🤝 Contributing

Found a bug? Got an idea? Open an issue or just yell at me in the DMs. PRs welcome, roasts optional.

---

## 📜 License

MIT — do whatever you want with it, just don't blame me when you see your food spending.

---

<p align="center">Made with 🩵 and mild financial anxiety</p>
