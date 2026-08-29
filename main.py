from datetime import datetime


def read_log_file():
    try:
        with open("server.log", "r") as file:
            lines = file.readlines()

        clean_lines = []

        for line in lines:
            clean_lines.append(line.strip())

        return clean_lines

    except FileNotFoundError:
        print("Error: server.log file not found.")
        return []


def analyze_logs(logs):
    info_count = 0
    warning_count = 0
    error_count = 0
    errors = []

    for line in logs:
        if "INFO" in line:
            info_count += 1

        elif "WARNING" in line:
            warning_count += 1

        elif "ERROR" in line:
            error_count += 1
            errors.append(line)

    return info_count, warning_count, error_count, errors


def display_summary(info_count, warning_count, error_count):
    print("\n===== LOG SUMMARY =====")
    print("INFO:", info_count)
    print("WARNING:", warning_count)
    print("ERROR:", error_count)

    if error_count > 3:
        print("\nStatus: ALERT")
        print("Warning: High number of errors detected!")
    else:
        print("\nStatus: NORMAL")


def display_errors(errors):
    print("\n===== ERROR LOGS =====")

    if not errors:
        print("No errors found.")
        return

    for error in errors:
        print(error)


def search_logs(logs):
    keyword = input("\nEnter keyword to search: ").strip().lower()

    found = False

    print("\n===== SEARCH RESULTS =====")

    for line in logs:
        if keyword in line.lower():
            print(line)
            found = True

    if not found:
        print("No matching logs found.")


def generate_report(info_count, warning_count, error_count, errors):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("monitoring_report.txt", "w") as file:
        file.write("===== SERVER LOG MONITORING REPORT =====\n")
        file.write(f"Generated: {current_time}\n\n")

        file.write(f"INFO: {info_count}\n")
        file.write(f"WARNING: {warning_count}\n")
        file.write(f"ERROR: {error_count}\n\n")

        if error_count > 3:
            file.write("Status: ALERT\n")
            file.write("Warning: High number of errors detected!\n")
        else:
            file.write("Status: NORMAL\n")

        file.write("\n===== ERROR LOGS =====\n")

        for error in errors:
            file.write(error + "\n")

    print("\nReport generated successfully!")
    print("Saved as: monitoring_report.txt")


def main():
    logs = read_log_file()

    if not logs:
        return

    info_count, warning_count, error_count, errors = analyze_logs(logs)

    while True:
        print("\n===== SERVER LOG MONITOR =====")
        print("1. View Log Summary")
        print("2. View Errors")
        print("3. Search Logs")
        print("4. Generate Report")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_summary(
                info_count,
                warning_count,
                error_count
            )

        elif choice == "2":
            display_errors(errors)

        elif choice == "3":
            search_logs(logs)

        elif choice == "4":
            generate_report(
                info_count,
                warning_count,
                error_count,
                errors
            )

        elif choice == "5":
            print("Exiting Server Log Monitor...")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")


main()