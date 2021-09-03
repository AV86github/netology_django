from django import template
from datetime import datetime, timedelta


register = template.Library()


@register.filter
def format_date(value):
    dt = datetime.fromtimestamp(value)
    now = datetime.now()
    if dt > now - timedelta(minutes=10):
        return "Только что"
    elif dt >= now - timedelta(days=1):
        return f"{(now - dt).seconds // 3600} часов назад"
    else:
        return dt.strftime("%Y %m %d")


@register.filter
def format_score(value):
    try:
        value = int(value)
    except:
        value = 0
    if value < -5:
        return "Все плохо"
    elif value < 5:
        return "нейтрально"
    else:
        return "Хорошо"


@register.filter
def format_num_comments(value):
    if value == 0:
        return "Оставьте комментарий"
    elif value < 50:
        return value
    else:
        return "50+"


@register.filter
def format_selftext(value, count=None):
    if count is None:
        return value
    txt = value.split()
    return " ".join(txt[:count]) + " ... " + " ".join(txt[-count:])
