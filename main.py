import os

LINE = "Sandra rescheduled the launch review six times, and when the seventh invite landed I realized the launch had already shipped last month."

def main():
    for base in ("/output", "./output"):
        try:
            os.makedirs(base, exist_ok=True)
            with open(os.path.join(base, "entry.txt"), "w", encoding="utf-8") as f:
                f.write(LINE)
            return
        except OSError:
            continue

if __name__ == "__main__":
    main()
