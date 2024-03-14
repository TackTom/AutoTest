

class TEOP:
    def orig(self):
        a = "1234"
        self.b = a


    def wer(self):
        self.orig()
        n = self.b
        print(n)

TEOP().wer()