import serial

class serial_reader:
    def __init__(self, tty, baud):
        self.baud = baud
        self.tty = tty
        self.reader = serial.Serial(f"/dev/{self.tty}", self.baud)
        self.reader.open()
        self.line = ""
    
    def read_line(self):
        while self.reader.in_waiting != 0:
            byte = self.reader.read(1)
            self.line =+ byte
            if byte == '\n':
                new_line = self.line
                self.line = ""
                return new_line
            return ""

    def stop_reader(self):
        self.reader.close()