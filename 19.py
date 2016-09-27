# I have a lot of unnecessary loops, etc, I will streamline if needed


def is_leap_year(year):
    if year == 1900:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def days_in_month(month, year):
    if month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    else:
        return 31


class Date:
    # everything is one-indexed
    def __init__(self, day_in_month, month, year, day_in_week):
        self.month = month
        self.year = year
        self.day_in_month = day_in_month
        self.day_in_week = day_in_week
        return

    def is_first_and_sunday(self):
        return self.day_in_month == 1 and self.day_in_week == 1 and self.year > 1900

    def go_next_day(self):
        # day_in_week
        if self.day_in_week == 7:
            self.day_in_week = 1
        else:
            self.day_in_week += 1

        # day_in_month
        # New month
        if self.day_in_month == days_in_month(self.month, self.year):
            # New year
            if self.month == 12:
                self.day_in_month = 1
                self.month = 1
                self.year += 1
            # Same year
            else:
                self.month += 1
                self.day_in_month = 1
        # Same Month
        else:
            self.day_in_month += 1

    def __str__(self):
        return "Year: " + \
                str(self.year) + \
                " Month: " + \
                str(self.month) + \
                " Date: " + \
                str(self.day_in_month) + \
                " Weekday: " + \
                str(self.day_in_week)


instances = 0
crawler = Date(1, 1, 1900, 2)
while crawler.year < 2001:
    print(crawler)
    if crawler.is_first_and_sunday():
        print("yay")
        instances += 1
    crawler.go_next_day()

print(instances)
