def generate_markdown(summary):
    with open("data/outputs/weekly_report.md", "w") as f:
        f.write("# Weekly Report\n\n")
        f.write(summary)