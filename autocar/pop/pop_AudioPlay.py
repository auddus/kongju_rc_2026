import time

from pop import AudioPlay, AudioRecord

with AudioRecord("my_recording.wav") as record:
    record.run()
    