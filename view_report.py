"""
Simple script to open the HTML report in your default browser
"""
import os
import webbrowser

# Path to the HTML report
html_report = os.path.join(os.getcwd(), "analysis_output", "Data_consistency.html")

if os.path.exists(html_report):
    print(f"Opening report: {html_report}")
    webbrowser.open(f"file://{html_report}")
    print("\nReport opened in your default browser!")
else:
    print(f"Report not found at: {html_report}")
    print("\nPlease run the analysis first:")
    print("  uv run python analyze_sales_data.py")
