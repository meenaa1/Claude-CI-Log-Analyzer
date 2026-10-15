# Claude CI Log Analyzer for DS Portal

A small project exploring how Claude can help analyze automated test failures. It runs Selenium UI tests against the [DS Algo Portal](https://dsportalapp.herokuapp.com/), captures test logs, and generates a diagnostic report with possible causes and suggested debugging steps.

## What It Does

- Runs automated UI tests using Python, Pytest, and Selenium.
- Uses Anthropic's Claude API to analyze test failure logs.
- Generates a Markdown report with possible causes and debugging suggestions.
- Provides a basic offline fallback when Claude analysis is unavailable.
- Runs through GitHub Actions and publishes the analysis to the job summary.

## Quick Start

### 1. Install Dependencies

Clone the repository:

```bash
git clone https://github.com/meenaa1/Claude-CI-Log-Analyzer.git
cd Claude-CI-Log-Analyzer
```

Create a virtual environment and install dependencies:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Install the required packages:

```bash
python -m pip install -r requirements.txt
```

### 2. Configure Claude (Optional)

Set your Anthropic API key as an environment variable to enable AI-powered analysis.

Windows PowerShell:

```powershell
$env:ANTHROPIC_API_KEY="your_api_key_here"
```

macOS/Linux:

```bash
export ANTHROPIC_API_KEY="your_api_key_here"
```

### 3. Run the Tests

```bash
python -m pytest tests/test_dsportal.py --tb=short
```

### 4. Generate the Analysis Report

```bash
python scripts/analyze_logs.py
```

The analyzer processes the available test logs and generates `analysis_report.md`.

## Project Structure

- `tests/test_dsportal.py` — Selenium and Pytest test cases.
- `scripts/analyze_logs.py` — Processes logs and generates the analysis report.
- `.github/workflows/test-analyzer.yml` — GitHub Actions workflow.
- `sample_logs/` — Sample test logs.
- `analysis_report.md` — Diagnostic report.

## Technologies Used

Python · Pytest · Selenium WebDriver · Anthropic Claude API · GitHub Actions

## Author

**Meenaa Kannan**
Software Development Engineer in Test (SDET)
