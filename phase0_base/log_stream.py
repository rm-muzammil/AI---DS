def read_logs(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line.strip()

def filter_errors(logs):
    for log in logs:
        if "ERROR" in log:
            yield log

logs = read_logs("logs.txt")
errors = filter_errors(logs)

for error in errors:
    print(error)