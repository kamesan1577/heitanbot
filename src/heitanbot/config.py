from dotenv import load_dotenv
import os

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
IS_DEV = os.getenv("IS_DEV") == "True"
prefix = "/"

resources_path = os.path.join(os.path.dirname(__file__), "resources")
quote_path = os.path.join(resources_path, "quote")
