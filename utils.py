from datetime import datetime, timedelta


def format_datetime(iso_str):
    dt = datetime.fromisoformat(iso_str)
    return dt.strftime("%b %d, %Y %I:%M %p")


def time_ago(iso_str):
    dt = datetime.fromisoformat(iso_str)
    now = datetime.now()
    diff = now - dt

    if diff < timedelta(minutes=1):
        return "just now"
    elif diff < timedelta(hours=1):
        minutes = int(diff.total_seconds() // 60)
        return f"{minutes} minute{'s' if minutes > 1 else ''} ago"
    elif diff < timedelta(days=1):
        hours = int(diff.total_seconds() // 3600)
        return f"{hours} hour{'s' if hours > 1 else ''} ago"
    elif diff < timedelta(days=30):
        days = diff.days
        return f"{days} day{'s' if days > 1 else ''} ago"
    else:
        return format_datetime(iso_str)