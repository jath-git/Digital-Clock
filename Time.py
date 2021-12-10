class Time(object):
    hour = 12
    minute = 0
    second = 0
    midday = 'AM'

    # construct
    def __init__(self, hour, minute, second, midday):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.midday = midday

    # update time fields
    def nextSecond(self):
        if (self.second < 59):
            self.second += 1
        else:
            self.second = 0
            self.nextMinute()

    def nextMinute(self):
        if (self.minute < 59):
            self.minute += 1
        else:
            self.minute = 0
            self.nextHour()

    def nextHour(self):
        if (self.hour < 11):
            self.hour += 1
        elif (self.hour == 11):
            self.hour = 12
            self.nextMidday()
        else:
            self.hour = 1

    def nextMidday(self):
        self.midday = 'AM' if self.midday == 'PM' else 'PM'
