# Fibonacci CI/CD Demo

A simple Python app that generates the Fibonacci series for a given number of terms (default 0), wired to GitHub Actions so every push automatically tests the code and shows the output.

## Project Structure

```
fibonacci-ci-demo/
├── .github/
│   └── workflows/
│       └── ci.yml            <- GitHub Actions pipeline
├── tests/
│   └── test_fibonacci.py     <- unit tests (run by CI)
├── fibonacci.py              <- main application
├── requirements.txt          <- pytest dependency
└── README.md
```

## Run Locally

```bash
python fibonacci.py        # default 0 -> empty series
python fibonacci.py 7      # -> [0, 1, 1, 2, 3, 5, 8]
pytest tests/ -v           # run tests locally
```

## Push to GitHub (triggers the pipeline)

```bash
git init                                          # initialise a new repo
git add .                                         # stage all files
git commit -m "Initial commit: Fibonacci CI/CD"   # first commit
git branch -M main                                # rename branch to main
git remote add origin https://github.com/<your-username>/fibonacci-ci-demo.git   # link remote
git push -u origin main                           # push -> CI/CD triggers automatically
```

## Where to See the Output

1. Go to your repo on GitHub -> **Actions** tab.
2. Click the latest run of **Fibonacci CI/CD**.
3. Open the **Build, Test and Run Fibonacci** job — each step shows its logs.
4. The **job summary page** shows the Fibonacci output in a formatted block.

## Manual Run with a Custom Number

1. Actions tab -> **Fibonacci CI/CD** -> **Run workflow** button.
2. Enter any number (e.g. 10) in the input box -> Run.
3. The pipeline runs and prints the series for your number.

## How the Pipeline Works

1. **Trigger**: push to main, pull request, or manual dispatch.
2. **CI**: checks out code, installs Python 3.12 and pytest, runs 5 unit tests. A failed test fails the whole run.
3. **CD/Output**: runs the app with the default (0) and with an input number, then writes the result to the job summary so it is visible without digging through logs.
