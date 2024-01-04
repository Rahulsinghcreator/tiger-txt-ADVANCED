import os

API_ID = API_ID = 23621134

API_HASH = os.environ.get("API_HASH", "3e49039179441fb424d90680ecffe365"

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6561995810:AAGvDAcE28oD6MG39DJhMTz-4cpRuST31cM"

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 1002140049222

LOG = -4099057818

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6333211826").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


