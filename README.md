# 💸 NumuS

> *Track your coins before they ghost you.*

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

## ✨ Features

| Feature | Status |
|---|---|
| 📥 Log expenses & incomes | ✅ Done |
| 📊 Interactive Dashboard | ✅ Done |
| 🏷️ Categories (Food, Travel, Custom) | ✅ Done |
| 💅 Styled with Tailwind CSS (CDN) | ✅ Done |
| 🔐 User auth with Flask-Login | ✅ Done |

---

## 🛠️ Tech Stack

- **Backend** — Flask (Python)
- **Styling** — Tailwind CSS via CDN *(because CSS files are the enemy)*
- **Auth** — Flask-Login + UserMixin
- **Database** — SQLAlchemy with SQLite (by default)
- **Migrations** — Flask-Migrate + Alembic

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/paulsurya/numus_app.git
cd numus_app
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Initialize the database

```bash
flask db upgrade
```

### 4. Run it

```bash
python run.py
```

Then open [http://localhost:5000](http://localhost:5000) and start logging your poor financial decisions.

---

## 📁 Project Structure

```
numus_app/
├── instance/
│   └── database.db           # SQLite database lives here
├── migrations/               # Alembic migration scripts
├── numus/
│   ├── static/               # CSS, JS, images
│   ├── templates/
│   │   ├── base.html         # Layout wrapper
│   │   ├── dashboard.html    # The money charts page
│   │   ├── input.html        # Log your expenses/incomes
│   │   └── login.html        # Auth page
│   ├── views/
│   │   ├── __init__.py
│   │   ├── auth.py           # Login/register routes
│   │   ├── dashboard.py      # Dashboard routes
│   │   └── input.py          # Input routes
│   ├── __init__.py
│   └── models.py             # User & transaction DB models
├── run.py                    # Entry point
├── requirements.txt
├── LICENSE.md
└── README.md                 # you are here
```

---

## 📦 Requirements

All dependencies are in `requirements.txt`. Core ones include:

| Package | Version |
|---|---|
| Flask | 3.1.3 |
| Flask-Login | 0.6.3 |
| Flask-SQLAlchemy | 3.1.1 |
| Flask-Migrate | 4.1.0 |
| SQLAlchemy | 2.0.49 |
| Werkzeug | 3.1.8 |

Just run `pip install -r requirements.txt` and you're good to go. No venv drama. No Docker. Just vibes and pip.

---

## 🗺️ Roadmap

- [ ] Charts that actually slap on the dashboard
- [ ] Budget limits per category
- [ ] Monthly spending summaries
- [ ] Export to CSV *(so you can cry in Excel too)*
- [ ] Dark mode *(obviously)*

---

## 🤝 Contributing

Found a bug? Got a feature idea? Open an issue or submit a PR — contributions are always welcome. Roasts optional.

1. Fork the repo
2. Create your feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📜 License

This project is licensed under the [MIT License](LICENSE.md) — do whatever you want with it, just don't blame me when you see your food spending.

---

Made with 🩵 and mild financial anxiety by [@paulsurya](https://github.com/paulsurya)
