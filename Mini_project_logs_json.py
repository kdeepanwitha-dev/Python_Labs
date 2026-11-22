import json
from collections import Counter

FILENAME = "unit_4/logs.json"


def analyze_logs():
    try:
        # 1. Read the JSON file
        with open(FILENAME, "r") as file:
            logs = json.load(file)

        if not isinstance(logs, list):
            print("Error: Invalid JSON structure. Expected a list of log records.")
            return

        # 2. Display all log records
        print("\n===== All Log Records =====")
        print(f"{'Timestamp':<12} {'Level':<10} {'Message'}")
        print("-" * 60)

        for log in logs:
            timestamp = log.get("timestamp", "N/A")
            level = log.get("level", "UNKNOWN")
            message = log.get("message", "No message")
            print(f"{timestamp:<12} {level:<10} {message}")

        print("-" * 60)

        # 3. Count the total number of INFO, WARNING and ERROR messages
        levels = [log.get("level", "UNKNOWN").upper() for log in logs]
        counts = Counter(levels)

        info_count = counts.get("INFO", 0)
        warning_count = counts.get("WARNING", 0)
        error_count = counts.get("ERROR", 0)

        # 4. Display the summary of each log category
        print("\n===== Log Summary =====")
        print(f"INFO     : {info_count}")
        print(f"WARNING  : {warning_count}")
        print(f"ERROR    : {error_count}")
        print(f"Total Logs: {len(logs)}")
        print("=" * 25 + "\n")

    except FileNotFoundError:
        print(f"Error: The file '{FILENAME}' does not exist.")
    except json.JSONDecodeError:
        print(f"Error: The file '{FILENAME}' contains invalid JSON data.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    analyze_logs()