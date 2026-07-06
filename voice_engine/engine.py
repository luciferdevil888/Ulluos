from voice_engine.config import WAKE_WORD


class VoiceEngine:
    def __init__(self):
        self.active = False

    def is_awake(self):
        return self.active

    def wake(self):
        self.active = True

    def sleep(self):
        self.active = False

    def check_wake_word(self, text):
        if not text:
            return False
        return WAKE_WORD in text.lower()


engine = VoiceEngine()
