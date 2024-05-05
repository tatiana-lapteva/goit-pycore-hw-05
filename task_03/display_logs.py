

def display_log_counts(counts: dict) -> str:
    """ display number of logs by level in a table """
   
    message = f"""
    Рівень логування | Кількість
    -----------------|----------
    INFO             | {counts['INFO']}
    DEBUG            | {counts['DEBUG']}
    ERROR            | {counts['ERROR']}
    WARNING          | {counts['WARNING']}

    """
    return message


def display_log_details(logs: list) -> str:
    """ display log details in format: date time - message"""

    log_details = ""
    for i in range(len(logs)):
        log_details += f"{logs[i]['date']} {logs[i]['hour']} - {logs[i]['message']}\n"
    return log_details



