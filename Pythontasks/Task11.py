def process_log_file(filename):
    error_count = 0

    try:
        with open(filename, "r") as file:
            for line in file:
                if "ERROR" in line:
                    error_count += 1

        print(f"Total 'ERROR' lines: {error_count}")

    except FileNotFoundError:
        print(" File not found.")
    except Exception as e:
        print(f" Something went wrong: {e}")

process_log_file("log.txt")