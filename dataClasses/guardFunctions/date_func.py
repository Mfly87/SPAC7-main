from datetime import datetime

def date_is_date(self, value: any, format: str) -> datetime | None:
    if value is None:
        return None
    if isinstance(value, datetime):
        return value
    if isinstance(value, str):
        try:
            value = datetime.strftime(value, format)
            return value
        except:
            return None
    return None