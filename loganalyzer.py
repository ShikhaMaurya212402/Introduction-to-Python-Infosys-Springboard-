from collections import defaultdict, Counter

def analyze_logs(logs):
    log_counts = defaultdict(int)
    error_messages = []

    for log in logs:
        # Split into date, time, level, message
        parts = log.split(" ", 3)
        level = parts[2]
        message = parts[3]

        # Count log levels
        log_counts[level] += 1

        # Collect error messages
        if level == "ERROR":
            error_messages.append(message)

    # Find most common error message
    most_common_error = None
    if error_messages:
        most_common_error = Counter(error_messages).most_common(1)[0][0]

    # Prepare final result
    result = {
        "INFO": log_counts.get("INFO", 0),
        "WARNING": log_counts.get("WARNING", 0),
        "ERROR": log_counts.get("ERROR", 0),
        "most_common_error": most_common_error
    }

    return result
logs = [
    "2026-01-02 10:15:32 ERROR Database connection failed",
    "2026-01-02 10:16:10 INFO User logged in",
    "2026-01-02 10:17:45 WARNING Disk space low",
    "2026-01-02 10:18:20 ERROR Database connection failed",
    "2026-01-02 10:19:00 INFO File uploaded"
]

output = analyze_logs(logs)
print(output)
