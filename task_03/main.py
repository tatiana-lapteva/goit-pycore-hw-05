
import argparse
from pathlib import Path
from load_logs import load_logs
from log_reporting import filter_logs_by_level, count_logs_by_level
from display_logs import display_log_counts, display_log_details


parser = argparse.ArgumentParser()
parser.add_argument('file_path')
parser.add_argument('-log_level', default=None)

args = parser.parse_args()
file_path, log_level = args.file_path, args.log_level


try:
    if Path(file_path).exists():
        log_list = load_logs(file_path)
        

        if len(log_list) > 0:

            logs_by_level_count = count_logs_by_level(log_list)

            if log_level:
                filtered_logs_by_level = filter_logs_by_level(log_list, log_level.upper())
                log_detail = display_log_details(filtered_logs_by_level)
    
            print(display_log_counts(logs_by_level_count))
    
            if log_level:
                print(log_detail)
        
    else:
        print("file not exists")
except Exception as e:
    print(e)
    
