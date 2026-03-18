from ingestion.excel_loader import load_excel
from processing.metrics import compute_metrics
from ai.summarizer import generate_summary
from reporting.markdown_report import generate_markdown

def main():
    data = load_excel("data/raw/sample.xlsx")

    metrics = compute_metrics(data)

    summary = generate_summary(metrics)

    generate_markdown(summary)

    print("Report generated successfully")

if __name__ == "__main__":
    main()