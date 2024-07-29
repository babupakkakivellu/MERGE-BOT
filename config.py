import os


class Config(object):
    API_HASH = os.environ.get("ed25a3c999b0849364a83b11bea390a0")
    BOT_TOKEN = os.environ.get("7148596098:AAEIpVWjhx84ybHMkAD9pbkmHgJtq7GkmQA.")
    TELEGRAM_API = os.environ.get("27476108")
    OWNER = os.environ.get("5422016608")
    OWNER_USERNAME = os.environ.get("BlasterOriginals")
    PASSWORD = os.environ.get("DINESH")
    DATABASE_URL = os.environ.get("mongodb+srv://9390463439a:edCbX0A2SXuvDjW3@cluster0.cbischq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    LOGCHANNEL = os.environ.get("-1002046586432")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
