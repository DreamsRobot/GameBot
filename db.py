from pymongo import MongoClient
from config import MONGO_URI, DB_NAME

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

xo_collection = db["xo_games"]
uno_collection = db["uno_games"]
