from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/6ba5162dfcea6af26b0d5.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/142e3e1a1deba0377d0a1.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/money_haterz_chatting_group")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Slayerr_Honey_XD")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5934011554").split()))


FAILED = "https://telegra.ph/file/6ba5162dfcea6af26b0d5.jpg"
