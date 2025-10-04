from datetime import datetime


def get_days_from_today(date):
    format_date = datetime.strptime(date, '%Y-%m-%d').date()
    today_date = datetime.today().date()
    difference = (today_date - format_date).days
    
    
    return difference