def calculate(days):
    bonus = 0
    if days >= 14 and days < 30:
        bonus = 50
        income = days*200 + 50*(days-14)
    elif days >= 30 and days < 60:
        bonus = 80
        income = days*200 + 80*(days-30)
    elif days > 60:
        bonus = 100
        income = days*200 + 100*(days-60)
    return income