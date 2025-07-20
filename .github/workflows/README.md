# Azure OpenAI Responses API Test Workflow

This GitHub Action tests the `responses-basic-aoai-v1.py` script to ensure it returns a valid response from Azure OpenAI.

## How to Run

1. Go to the **Actions** tab in the GitHub repository
2. Select **"Test Azure OpenAI Responses API"** workflow
3. Click **"Run workflow"** button
4. Click **"Run workflow"** to confirm

## Required Environment Secrets

The workflow uses the following secrets from the `responses` environment:

- `AZURE_OPENAI_API_KEY` - Your Azure OpenAI API key
- `AZURE_OPENAI_V1_API_ENDPOINT` - Your Azure OpenAI v1 API endpoint (e.g., `https://your-resource.openai.azure.com/openai/v1/`)
- `AZURE_OPENAI_API_MODEL` - The model name to use (e.g., `gpt-4o`)

## Test Results

The workflow generates test artifacts that include:

### JSON Results (`test-results.json`)
```json
{
  "test_last_run_date": "2025-07-20T23:01:29Z",
  "output": "Why don't scientists trust atoms? Because they make up everything!",
  "pass_fail": "PASS",
  "error_code": ""
}
```

### Human-Readable Summary (`test-summary.txt`)
```
Azure OpenAI Responses API Test Results
========================================
Test Run Date: 2025-07-20T23:01:29Z
Result: PASS
Error Code: 

Output:
Why don't scientists trust atoms? Because they make up everything!
```

## Test Criteria

The test passes if:
- The Python script executes without errors
- The script produces output
- The output contains valid string content (not empty, no error indicators)

The test fails if:
- Environment variables are missing
- The script fails to execute
- No output is produced
- Output contains error indicators (error, exception, traceback, failed, none, null)

## Artifacts

Test results are uploaded as artifacts with:
- **Name**: `azure-openai-test-results`
- **Retention**: 30 days
- **Contents**: Both JSON and human-readable results

## Troubleshooting

If the workflow fails:
1. Check that all required environment secrets are set in the `responses` environment
2. Verify that the Azure OpenAI service is accessible
3. Review the workflow logs for specific error messages
4. Check the uploaded artifacts for detailed test results