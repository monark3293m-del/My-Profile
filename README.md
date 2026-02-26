# Monark Mehta — Portfolio Website

A personal portfolio website built with **Python Flask** (backend) and **HTML/CSS/JavaScript** (frontend).

## Project Structure

```
portfolio/
├── app.py               # Flask backend + all profile data
├── requirements.txt     # Python dependencies
├── templates/
│   └── index.html       # Main HTML template (Jinja2)
└── static/
    ├── css/
    │   └── style.css    # Full stylesheet
    └── js/
        └── main.js      # Animations & interactivity
```

---

## Local Setup

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run locally
```bash
python app.py
```

Open: [http://localhost:5000](http://localhost:5000)

---

## Deployment Options

### Option A — Render (Free, Recommended)

1. Push your project to GitHub.
2. Go to [https://render.com](https://render.com) → New → Web Service.
3. Connect your GitHub repo.
4. Set:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
5. Click **Deploy**. Your site will be live at `https://your-name.onrender.com`.

Also add `gunicorn` to `requirements.txt`:
```
flask>=3.0.0
gunicorn
```

---

### Option B — Railway

1. Push to GitHub.
2. Go to [https://railway.app](https://railway.app) → New Project → Deploy from GitHub.
3. Add environment variable: `PORT=5000`
4. Railway auto-detects Flask. Done!

---

### Option C — PythonAnywhere (Free Tier)

1. Sign up at [https://www.pythonanywhere.com](https://www.pythonanywhere.com)
2. Upload your files via the Files tab.
3. Go to Web tab → Add a new web app → Flask.
4. Set the source code path to your project directory.
5. Configure the WSGI file to point to `app.py`.

---

### Option D — VPS / Cloud VM (AWS, DigitalOcean, etc.)

```bash
# Install nginx + gunicorn
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app

# Configure nginx to proxy to port 5000
```

---

## Customization

To update your profile data, edit the `profile_data` dictionary in **`app.py`**:
- Update email, LinkedIn, GitHub links
- Add certifications
- Add/remove projects
- Update publication DOI links

---

## Tech Stack

- **Backend**: Python 3, Flask
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Fonts**: Syne (display), IBM Plex Mono, IBM Plex Sans
- **Design**: Industrial dark theme, animated UI, scroll-triggered reveals
"# My-Profile" 
