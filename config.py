from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "1b4cdb255f37262200981dbbf87a1fa0")
      API_ID = int(getenv("API_ID", "22696222"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "8096179406:AAGvFyNW9O9O994VxrlR_aPkZj1RiroWA3M")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1001722984461:-1001623633000").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
