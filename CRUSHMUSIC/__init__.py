from  CRUSHMUSIC.core.bot import PRASHANT
from  CRUSHMUSIC.core.dir import dirr
from  CRUSHMUSIC.core.git import git
from  CRUSHMUSIC.core.userbot import Userbot
from  CRUSHMUSIC.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = PRASHANT()
userbot = Userbot()

from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
