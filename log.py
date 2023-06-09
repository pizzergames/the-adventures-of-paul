import datetime
import os

class LogObject:
    def __init__(self, file):
        self.file = open(file, 'a')
        self.text = ''
    
    def log(self, text):
        text = str(datetime.datetime.now()).replace(' ', '_')
        text = f'<{str(datetime.datetime.now()).replace(" ", "_")}> LOG: {text}'
        self.text += f'{text}\n'
    
    def warn(self, text):
        text = str(datetime.datetime.now()).replace(' ', '_')
        text = f'<{str(datetime.datetime.now()).replace(" ", "_")}> WARNING: {text}'
        self.text += f'{text}\n'
    
    def error(self, text):
        text = str(datetime.datetime.now()).replace(' ', '_')
        text = f'<{str(datetime.datetime.now()).replace(" ", "_")}> ERROR: {text}'
        self.text += f'{text}\n'
    
    def critical(self, text):
        text = str(datetime.datetime.now()).replace(' ', '_')
        text = f'<{str(datetime.datetime.now()).replace(" ", "_")}> CRITIAL ERROR: {text}'
        self.text += f'{text}\n'
    
    def flush(self):
        self.text = ''
    
    def update(self):
        self.file.write(self.text)
    
    def exit(self):
        self.file.close()

def generate_filename(logpath):
    path = os.path.join(
        logpath,
        f'{str(datetime.datetime.now()).replace(" ", "_").replace(":", "_")}.log'
    )
    return path
