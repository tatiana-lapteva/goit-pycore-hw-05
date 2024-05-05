


def filter_logs_by_level(logs: list[dict], level: str) -> list[dict]: 
    """ filter logs list by requested level"""
    
    filtered_result = list(filter(lambda d: d['level'] in level, logs))

    return filtered_result



# OPTION 1: count logs using DefaultDict:
from collections import defaultdict

def count_logs_by_level(logs: list[dict]) -> dict[int]:
    """ count logs by level"""
     
    log_dict = defaultdict(int)

    for i in range(len(logs)):
        log_dict[logs[i]['level']] += 1      
    
    return log_dict
       


# OPTION 2: count logs using Counter:
from collections import Counter

def count_logs_by_level(logs: list[dict]) -> dict[int]:
    log_dict = Counter(item['level'] for item in logs)
    
    return dict(log_dict)


