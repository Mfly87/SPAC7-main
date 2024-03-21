from datetime import datetime

def date_is_date(value: any, format: str) -> datetime | None:
    if value is None:
        return None
    if isinstance(value, datetime):
        return value
    if isinstance(value, str):
        try:
            value = datetime.strptime(value, format)
            return value
        except:
            return None
    return None