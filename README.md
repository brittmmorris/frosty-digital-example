# Frosty AI DigitalOcean Starter

🚀 A FastAPI-based Python app that calls Frosty AI’s routing API using the official `frosty-ai` SDK.  
Designed for easy deployment on [DigitalOcean App Platform](https://www.digitalocean.com/products/app-platform).

---

## ⚙️ Local Setup

1. **Clone this repo**

```bash
git clone https://github.com/your-username/frosty-digital-example
cd frosty-digital-example
```

2. **Create a virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Create an `.env` file**

```bash
cp .env.example .env
```

Then fill in your values from the [Frosty Console](https://console.gofrosty.ai):

```env
ROUTER_ID=your-router-id
ROUTER_KEY=your-router-key
```

5. **Run the app**

```bash
uvicorn main:app --reload
```

Visit `http://localhost:8000` to hit the test route.

---

## 🧠 What It Does

- Calls Frosty’s `chat()` function using the Python SDK.
- Returns a basic AI response to the root (`/`) endpoint.
- Automatically logs usage metrics.
- Ready for 1-click deploy on DigitalOcean.

---

## 💡 Example Response

```json
{
  "chat": {
    "response": "Here's a silly joke for you: Why can't a bicycle stand up by itself? It's two-tired!",
    "provider": "Anthropic",
    "model": "claude-3-sonnet",
    "rule": "cost"
  }
}
```

---

## ☁️ Deploy to DigitalOcean

This app was built to run on [DigitalOcean App Platform](https://www.digitalocean.com/products/app-platform):

1. Push this repo to GitHub (if you haven’t already).
2. In DO’s App Platform:
   - Choose “Deploy from GitHub”.
   - Select your repo.
   - Set your environment variables (`ROUTER_ID` and `ROUTER_KEY`) under **Settings → Environment Variables**.
   - That’s it! DO will auto-detect FastAPI and deploy it as a web service.

---

## 📌 Helpful Links

- 🔐 [Frosty Console](https://console.gofrosty.ai)
- 📚 [Frosty API Docs](https://docs.gofrosty.ai)

---

