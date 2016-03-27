import datetime

class Intercept:

    frequency_kHz = 0
    time_of_intercept = datetime.MINYEAR

    def __init__(self, time_of_intercept= datetime.MINYEAR, frequency_kHz = 0):
        self.time_of_intercept = time_of_intercept
        self.frequency_kHz = frequency_kHz

