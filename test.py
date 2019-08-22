# from pydub import AudioSegment
from pydub import playback
from pydub import *
# from pydub.playback import play

song = AudioSegment.from_mp3("./sounds/mkultra.mp3")
playback.play(song)
