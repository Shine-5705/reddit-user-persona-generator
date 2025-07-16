import os
import re
from dotenv import load_dotenv
import praw

# Load environment variables
load_dotenv()

# Setup Reddit API
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT"),
    check_for_async=False
)
reddit.read_only = True

def extract_username(url):
    match = re.search(r"reddit\.com/user/([^/]+)", url)
    return match.group(1) if match else None

def fetch_user_data(username, limit=100):
    user = reddit.redditor(username)
    posts = [f"[POST] {post.title}\n{post.selftext}" for post in user.submissions.new(limit=limit)]
    comments = [f"[COMMENT] {comment.body}" for comment in user.comments.new(limit=limit)]
    return posts, comments

def generate_persona(posts, comments):
    combined_text = "\n".join(posts + comments).lower()

    traits = []

    if any(word in combined_text for word in ["python", "code", "developer", "bug", "script"]):
        traits.append("Interested in programming or software development.")
    if any(word in combined_text for word in ["anime", "manga", "naruto", "one piece", "otaku"]):
        traits.append("Enjoys anime or Japanese pop culture.")
    if any(word in combined_text for word in ["game", "gamer", "fps", "rpg", "steam", "playstation"]):
        traits.append("Likely a gamer and engages in video game communities.")
    if any(word in combined_text for word in ["fitness", "gym", "workout", "protein"]):
        traits.append("Values health and fitness.")

    if any(word in combined_text for word in ["lol", "lmao", "haha", "funny", "joke"]):
        traits.append("Has a humorous or casual tone.")
    if any(word in combined_text for word in ["depressed", "anxious", "sad", "stress"]):
        traits.append("May express emotional vulnerability or mental health struggles.")
    if any(word in combined_text for word in ["opinion", "debate", "argument", "disagree"]):
        traits.append("Likes to engage in discussions or debates.")

    if not traits:
        traits.append("Not enough information to determine strong personality traits.")

    summary = "🧠 Persona Summary (Local Heuristics):\n\n"
    for i, trait in enumerate(traits, 1):
        summary += f"{i}. {trait}\n"

    return summary

def save_output(username, persona_text):
    os.makedirs("persona_outputs", exist_ok=True)
    filename = f"persona_outputs/{username}_persona.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(persona_text)
    print(f"✅ Persona saved to {filename}")

if __name__ == "__main__":
    print("CLIENT ID:", os.getenv("REDDIT_CLIENT_ID"))
    reddit_url = input("🔗 Enter Reddit user profile URL: ")
    username = extract_username(reddit_url)

    if not username:
        print("❌ Invalid Reddit URL")
        exit()

    print(f"📥 Scraping user: {username} ...")
    posts, comments = fetch_user_data(username)

    print("🤖 Generating persona locally (no LLM)...")
    persona = generate_persona(posts, comments)

    print("💾 Saving persona to file...")
    save_output(username, persona)
