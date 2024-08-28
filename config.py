import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7518910639:AAFHZWDwkcTYppqEs6qtPpqeYta6F7BNhuY")
API_ID = int(os.environ.get("API_ID", "21476260"))
API_HASH = os.environ.get("API_HASH", "ec9654f315ce63225cf7b69263347f96")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002240543376"))
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "7358307430").split())
DB_URL = os.environ.get("DB_URL", "mongodb+srv://Smit0987:Smit0987@quotexcluster0.cf4rx.mongodb.net/?retryWrites=true&w=majority&appName=quotexCluster0")
DB_NAME = os.environ.get("DB_NAME", "BroadcastBot")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
