
from functools import wraps
import re

def exception_handling(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error occured: {func.__name__} - {e}")
            return None
    
    return wrapper


@exception_handling
def parse_log_line(line: str) -> dict:   
    """ parse log string into dictionary
        required string structure: date hour level message  
    """
    
    log_components = dict()
    pattern = r"\d{4}(-\d{2}){2}\s(\d){2}:(\d){2}:(\d){2}\s(INFO|DEBUG|ERROR|WARNING)\s(\w|\W)+"

    if re.match(pattern, line):
        date, hour, level, *message = line.strip().split()    
        log_components["date"] = date
        log_components["hour"] = hour
        log_components["level"] = level
        log_components["message"] = ' '.join(message)
        return log_components
    else:
        raise Exception("Invalid data structure")


@exception_handling
def load_logs(file_path: str) -> list:
    """ get all logs from a given file"""

    with open(file_path, 'r', encoding="utf-8") as file:
        log_list = []
        for line in file:
            result = parse_log_line(line)
            if result:
                log_list.append(result)
            else:
                return log_list.clear()
    return log_list

            


