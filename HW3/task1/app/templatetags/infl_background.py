from django import template


register = template.Library()


@register.filter
def infl_background(val, header):
    if not val or header == "Год":
        return ""
    val = float(val)
    style = "background-color: "
    if header == "Суммарная":
        return f"{style}grey"
    elif val < 0:
        return f"{style}green"
    elif 1 <= val < 2:
        return f"{style}#e38686"
    elif 2 <= val < 5:
        return f"{style}#e35454"
    elif val >= 5:
        return f"{style}#fa0000"
    else:
        return ""
