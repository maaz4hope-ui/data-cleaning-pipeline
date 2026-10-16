# 🧹 Data Cleaning Pipeline

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/pandas-2.0%2B-green)](https://pandas.pydata.org/)
[![Tests](https://img.shields.io/badge/tests-11%20passed-brightgreen)]()
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

A production-ready Python class for automated data cleaning with 11 unit tests.

## ✨ Features

- Load CSV files with robust error handling
- Remove duplicate rows automatically
- Fill missing values (median for numeric, mode for text)
- Auto-detect and convert date columns
- Remove outliers using IQR method
- Save cleaned data to CSV
- 11 unit tests with pytest
- Type hints and docstrings throughout

## 🚀 Quick Start

### Installation

```bash
git clone https://github.com/maaz4hope-ui/data-cleaning-pipeline.git
cd data-cleaning-pipeline
pip install -r requirements.txt
