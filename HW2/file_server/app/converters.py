from datetime import date


class ISO_Date():
    regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}'

    def to_python(self, value):
        # from string into view func - date
        return date.fromisoformat(value)

    def to_url(self, value):
        # from python type to string
        return value.strftime("%Y-%m-%d")
