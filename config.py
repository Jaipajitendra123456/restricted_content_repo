# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "29257881"))
API_HASH = getenv("API_HASH", "3dd9f4e0716871e4b507f9411fd1ee8b")
BOT_TOKEN = getenv("BOT_TOKEN", "7996239291:AAFH8TQReUOEWqfIfMb7Ie8vaikX5z1BPZ8")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7891840370").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://savebot:RxxBfvkv1xnGsbPL@cluster0.9zpw7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "1002330334141")
CHANNEL_ID = int(getenv("CHANNEL_ID", "1002348264995"))
