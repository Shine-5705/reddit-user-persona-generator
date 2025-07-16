# 🧠 Reddit Persona Generator (Offline Version)

This is a fully offline Python tool that scrapes any public Reddit user's posts and comments and generates a basic user persona using rule-based local logic. It does **not** require OpenAI, Gemini, or any external LLM API.

---

## 📦 Features

- ✅ Scrapes public Reddit activity using PRAW (Reddit API)
- 🧠 Generates personality traits using simple keyword-based logic
- 📄 Outputs results to a text file
- ❌ Works entirely offline (no API calls to OpenAI or Gemini)

---

## 📁 Project Structure

reddit_persona_offline/
├── generate_persona.py # Main script
├── requirements.txt # Dependencies
├── .env.example # Reddit API credentials template
├── persona_outputs/ # Output folder (auto-created)


---

## 🛠 Requirements

- Python 3.7 or higher
- Reddit developer account (free)
- `praw` and `python-dotenv` libraries

Install requirements:

```bash
pip install -r requirements.txt
```

Reddit API Setup
Go to: https://www.reddit.com/prefs/apps
Click “Create App”
    Choose:
    Name: any name (e.g., persona_tool)
    Type: script
    Redirect URI: http://localhost
After submitting:
    Copy the Client ID (shown under the app name)
    Copy the Secret value
    Note your Reddit username
Use your actual Reddit username in the user agent for best results.


## How to Run for Any Reddit User

Open terminal and run:

'''bash
python generate_persona.py
```
Then when prompted:
🔗 Enter Reddit user profile URL: https://www.reddit.com/user/spez/

The tool will:
    Scrape recent posts and comments
    Analyze content for tone, interests, and engagement style
    Save the result in persona_outputs/<username>_persona.txt
        


## 📂 Output Directory: `persona_outputs`

After running the script, all generated user personas will be saved in the `persona_outputs` folder. This folder contains:

- `.txt` files named after the Reddit username you provided.
- Each file contains the user's profile summary, including extracted posts, comments, and the generated persona.

### Example
If you enter:
https://www.reddit.com/user/Hungry-Move-6603/comments/


You will get:
persona_outputs/kojied_persona.txt

This file contains a detailed persona generated from `u/spez`'s public Reddit activity.

> 📌 Make sure the folder `persona_outputs/` exists. The script will create it automatically if not found.
