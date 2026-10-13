# 🤖 Claude CI Log Analyzer for DS Portal

An AI-assisted CI/CD testing utility that runs Selenium UI tests against the DS Algo Portal(https://dsportalapp.herokuapp.com/), captures test execution logs, and generates actionable failure analysis reports using Anthropic Claude or an offline fallback.

The project demonstrates how AI-assisted diagnostics can help QA engineers and SDETs investigate automated test failures within a GitHub Actions workflow.

## 📌 Features

- **Automated UI Testing:** Executes PyTest and Selenium WebDriver tests against the DS Portal application.
- **Automated Failure Detection:** Captures test execution output and makes diagnostic analysis conditional on test results.
- **Robust Log Processing:** Reads captured logs and handles common UTF-8 and UTF-16 encoding variations.
- **AI-Powered Failure Analysis:** Uses the Anthropic Claude API to summarize stack traces, identify potential root causes, and recommend debugging steps.
- **Offline Fallback:** Generates a basic diagnostic report when the AI API is unavailable or an API request fails.
- **GitHub Actions Integration:** Runs the test workflow automatically and publishes the analysis to the GitHub Actions job summary.
- **Markdown Reporting:** Generates a readable `analysis_report.md` file containing the failure summary, possible cause, and recommended actions.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Test automation and log analysis |
| PyTest | Test execution and assertions |
| Selenium WebDriver | Browser automation |
| WebDriver Manager | Local browser driver management |
| Anthropic API | AI-assisted log analysis |
| GitHub Actions | CI/CD workflow automation |
| Markdown | Diagnostic reports and job summaries |

## 📁 Repository Structure

```text
Claude-CI-Log-Analyzer/
├── .github/
│   └── workflows/
│       └── test-analyzer.yml
├── scripts/
│   └── analyze_logs.py
├── tests/
│   └── test_dsportal.py
├── sample_logs/
│   └── test-failure.log
├── analysis_report.md
├── requirements.txt
├── .gitignore
└── README.md
```

**Key files**

- `tests/test_dsportal.py` — Contains the Selenium and PyTest test cases.
- `scripts/analyze_logs.py` — Processes test logs and generates AI-assisted or fallback diagnostics.
- `.github/workflows/test-analyzer.yml` — Defines the automated testing and reporting workflow.
- `sample_logs/test-failure.log` — Contains sample failure output for testing the analyzer independently.
- `analysis_report.md` — Generated diagnostic report; its contents depend on the latest analysis run.

## ⚙️ Prerequisites

- Python 3.10 or newer
- Google Chrome, if running the browser tests locally
- Git
- An Anthropic API key for live Claude analysis (optional if fallback mode is supported)

The DS Portal is accessed over the internet, so live UI tests also depend on the target application being reachable and available.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Claude-CI-Log-Analyzer.git
cd Claude-CI-Log-Analyzer
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create and activate a virtual environment

**Windows PowerShell**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS or Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

Create a `requirements.txt` file with the following packages:

```text
pytest
selenium
webdriver-manager
anthropic
```

Install them:

```bash
python -m pip install -r requirements.txt
```

If your analyzer supports offline mode without importing the Anthropic SDK unconditionally, you can omit `anthropic` when running without the API. Otherwise, install the listed dependencies even when using the fallback.

### 4. Configure the Anthropic API key (optional)

Set the API key as an environment variable.

**Windows PowerShell**

```powershell
$env:ANTHROPIC_API_KEY="your_api_key_here"
```

**macOS or Linux**

```bash
export ANTHROPIC_API_KEY="your_api_key_here"
```

Use a valid API key only in your local environment or a secure GitHub Actions secret. Never commit API keys to source control.

For GitHub Actions, add `ANTHROPIC_API_KEY` under your repository's **Settings → Secrets and variables → Actions → New repository secret** if the workflow uses live Claude analysis.

If the key is missing, the analyzer should use its fallback mode when configured to do so.

### 5. Run the Selenium test suite

Run the tests and capture their output in a log file.

**Windows PowerShell**

```powershell
New-Item -ItemType Directory -Force sample_logs
python -m pytest tests/test_dsportal.py --tb=short --capture=tee-sys 2>&1 |
    Tee-Object -FilePath sample_logs/test-failure.log
```

**macOS or Linux**

```bash
mkdir -p sample_logs
python -m pytest tests/test_dsportal.py --tb=short 2>&1 |
    tee sample_logs/test-failure.log
```

These commands preserve the test output in a log file while also displaying it in the terminal. The pipeline's exit status may need special handling if you want the shell to propagate the original PyTest exit code.

For a simpler log-only run, you can use:

```bash
python -m pytest tests/test_dsportal.py --tb=short > sample_logs/test-failure.log 2>&1
```

### 6. Generate the diagnostic report

Run the analyzer:

```bash
python scripts/analyze_logs.py
```

The analyzer should read the configured log file, attempt Claude analysis when available, and generate `analysis_report.md`.

Review the report to distinguish facts explicitly supported by the logs from possible causes suggested by the AI.

## 🧪 Example Diagnostic Report

The following is an illustrative example of the type of output the analyzer can produce.

### Test Failure Summary

A Selenium test failed with a `NoSuchElementException` while attempting to locate an element using the selector `#non-existent-login-button`.

### Evidence

- The test log identifies an element lookup failure.
- The reported selector is `#non-existent-login-button`.
- The test could not locate the requested element at the time of execution.

### Possible Root Cause

The selector may be incorrect, the element may not exist on the page, or the page may not have finished rendering when the lookup occurred.

### Recommended Actions

1. Inspect the page DOM and verify the selector.
2. Confirm that the expected page has loaded before locating the element.
3. Check whether the element is conditionally rendered or inside an iframe.
4. Update the test locator if the application's UI has changed.
5. Rerun the test to confirm the fix.

The example above is illustrative; actual results depend on the captured logs and the analyzer's implementation.

## 🔄 GitHub Actions Workflow

The CI/CD workflow is designed to:

1. Check out the repository.
2. Set up Python and install the required dependencies.
3. Configure the browser environment.
4. Execute the Selenium test suite.
5. Capture the test output and exit status.
6. Invoke the log analyzer when appropriate.
7. Publish the diagnostic report to the GitHub Actions job summary.
8. Preserve the original test result so that a failed test suite is not incorrectly marked as successful.

The test result and the analysis result should be handled separately: the fallback analyzer may successfully generate a report even when the Selenium tests fail, but the overall workflow should still fail if the tests fail.

## 🛡️ Reliability and Security Considerations

- Keep API keys in environment variables or GitHub Actions secrets.
- Avoid logging credentials, session tokens, or other sensitive information.
- Treat AI-generated root causes as hypotheses unless independently verified.
- Preserve the original test exit code when running shell commands or invoking the analyzer.
- Make fallback behavior explicit so that API failures do not silently hide diagnostic limitations.
- Use sample logs to test the analyzer independently of the live application.
- Keep the test suite independent of the AI API so that browser tests can run without AI access.

## 🎯 Project Goals

This project demonstrates practical skills in:

- Selenium and PyTest automation
- CI/CD workflow design
- Failure log collection and processing
- AI-assisted debugging
- Exception handling and fallback design
- Markdown report generation
- Test-result integrity and reproducible diagnostics

## 🔮 Future Enhancements

- Add structured JSON output for diagnostic results.
- Include direct references to failed test names and source-code locations.
- Add unit tests for log parsing and fallback behavior.
- Support additional failure categories, including timeouts, assertion errors, and stale element exceptions.
- Store historical test results and visualize recurring failures.
- Add links from GitHub Actions summaries to uploaded reports and artifacts.

## 👩‍💻 Author

**Meenaa Kannan**

Software Development Engineer in Test (SDET) | Test Automation | Python | Selenium | Playwright | CI/CD | AI-Assisted QA

