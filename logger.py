import threading
class log:
    def __init__(self):
        self.log_file = open("test_log.log", "w")
        
class logger:
    def __init__(self, name):
        self.name = name