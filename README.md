# python-challenge
PYChallenge

# Data Analysis Projects

This repository contains two Python scripts for analyzing datasets:

---

## 📊 1. Financial Analysis

**Script:** `financial_analysis.py`  
**Input File:** `budget_data.csv`

### Description:
This script processes a CSV file containing monthly profit/loss data and computes the following:

- Total number of months in the dataset
- Net total amount of "Profit/Losses" over the period
- Average of monthly changes in "Profit/Losses"
- Greatest increase in profits (date and amount)
- Greatest decrease in profits (date and amount)

### Output:
- Results are printed to the terminal
- Results are saved to `financial_analysis_results.txt` in the same directory

---

## 🗳️ 2. Election Analysis

**Script:** `election_analysis.py`  
**Input File:** `election_data.csv`

### Description:
This script analyzes voting data to determine the election outcome based on popular vote. It calculates:

- Total number of votes cast
- Complete list of candidates who received votes
- Total and percentage of votes each candidate won
- The winner of the election

### Output:
- Results are printed to the terminal
- Results are saved to `election_results.txt` in the same directory

---

## 🛠️ Usage

Ensure the input CSV files (`budget_data.csv`, `election_data.csv`) are located in the same directory as the scripts. Run the scripts with:

```bash
python financial_analysis.py
python election_analysis.py
