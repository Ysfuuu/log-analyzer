import argparse

parser = argparse.ArgumentParser(
    description="Analyze application log files"
)

parser.add_argument(
    "filename",
    help="Path to the log file to analyze"
)

args = parser.parse_args()

invalid_count = 0

counts = {
    "INFO": 0,
    "WARNING": 0,
    "ERROR": 0
}

try:
    with open(args.filename, "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split()

            if len(parts) < 3:
                invalid_count += 1
                continue

            log_level = parts[2]

            if log_level in counts:
                counts[log_level] += 1
            else:
                invalid_count += 1

except FileNotFoundError:
    print(f"Error: File '{args.filename}' was not found.")
    raise SystemExit(1)


total = sum(counts.values())

print("Log Analysis Summary")
print("--------------------")
print(f"Total log entries: {total}")

for level, count in counts.items():
    print(f"{level}: {count}")

print(f"Invalid entries: {invalid_count}")