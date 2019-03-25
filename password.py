class Password:

    def init(self, password):
        self.pwd = password

    def check(self, test):
        return self.pwd == test
