class SoundController:
    def play_tone(self, freq, duration):
        print(f"[MOCK SOUND] {freq}Hz 주파수를 {duration}초간 재생합니다. 삑-")

    def speak_tts(self, text):
        print(f"[MOCK TTS] 음성 출력: \"{text}\"")
        