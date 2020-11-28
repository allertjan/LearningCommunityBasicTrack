class MyTime:

    def __init__(self, hrs=0, min=0, sec=0):
        """ Create a MyTime object initialized to hrs, mins, secs """
        self.totalsecs = hrs * 3600 + min * 60 + sec
        self.hours = self.totalsecs // 3600
        leftoversecs = self.totalsecs % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60

    def __str__(self):
        return "({0}, {1}, {2})".format(self.hours, self.minutes, self.seconds)

    def increment(self, hrs=0, min=0, sec=0):
        self.totalsecs += (hrs * 3600 + min * 60 + sec)

        self.hours = self.totalsecs // 3600
        leftoversecs = self.totalsecs % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60

        return self.hours, self.minutes, self.seconds

    def to_seconds(self):
        """ Return the number of seconds represented by this instance"""
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def between(self, t1, object_time):
        if self.to_seconds() < t1.to_seconds():
            return self.to_seconds() < object_time.to_seconds() <= t1.to_seconds()
        else:
            return t1.to_seconds() < object_time.to_seconds() <= self.to_seconds()

    def __gt__(self, other):
        """ Return True if I am strictly greater than time2 """
        return self.to_seconds() > other.to_seconds()



