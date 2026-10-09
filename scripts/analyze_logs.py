import os
from anthropic import Anthropic

def analyze_failure():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY environment variable is missing.")

    client = Anthropic(api_key=api_key)

    log_path = os.environ.get("LOG_FILE_PATH", "sample_logs/test-failure.log")
    if not os.path.exists(log_path):
        print(f"Log file not found at path: {log_path}")
        return

    with open(log_path, "r", encoding="utf-8") as f:
        raw_logs = f.read()

    failure_snippet = raw_logs[-4000:]

    prompt = f"""
You are an expert QA Automation Lead reviewing a failed CI test log.
Analyze the following test log output and provide a clear, structured summary for developers.

Log Output:
Format your response exactly as Markdown with the following section headers:
### 🚨 Test Failure Summary
Brief 1-2 sentence explanation of what went wrong.

### 🔍 Root Cause Analysis
Explain why the failure occurred (e.g., locator mismatch, timeout, API status error, environment flake).

### 💡 Suggested Action / Fix
Provide the concrete code fix, locator adjustment, or troubleshooting step.
"""

    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=600,
        messages=[{"role": "user", "content": prompt}]
    )

    report_markdown = response.content[0].text

    with open("analysis_report.md", "w", encoding="utf-8") as out_file:
        out_file.write(report_markdown)

    print("Analysis complete! Report written to analysis_report.md")

if __name__ == "__main__":
    analyze_failure()