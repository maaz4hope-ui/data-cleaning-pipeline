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
```

### Usage

```python
from data_cleaning import DataManager

# Initialize with file path
manager = DataManager("raw_data.csv")

# Load data
manager.load_data()

# Clean data (duplicates, missing values, dates)
manager.clean_data()

# Remove outliers (IQR method)
manager.remove_outlier()

# View summary
manager.get_summary()

# Save cleaned data
manager.save_data("cleaned.csv")
```

## 🧪 Running Tests

```bash
pytest test_cleaning_data.py -v
```

**Expected:** 11 tests passed ✅

## 📸 Sample Output

```python
>>> from data_cleaning import DataManager
>>> manager = DataManager("raw_data.csv")
>>> print(manager)
DataManager(file='raw_data.csv', rows=0, not loaded, not cleaned)

>>> manager.load_data()
✅ Data loaded! Rows: 1000, Columns: 15

>>> manager.clean_data()
✅ Cleaned! Remaining rows: 950

>>> manager.remove_outlier()
✅ 25 outliers removed!
```

## 📊 Test Coverage

| Test                                 | What it Checks                   |
|--------------------------------------|----------------------------------|
| test_file_not_found.                 | Error handling for missing files |
| test_load_data_success.              | CSV loading.                     |
| test_data_cleaning_fill_missing.     | Missing value imputation         |
| test_data_cleaning_remove_duplicates | Duplicate removal                |
| test_remove_outliers                 | IQR-based outlier detection.     |
| test_check_column_exists             | Static helper method.            |
| test_total_files_processed.          | Class variable tracking          |
| test_empty_csv.                      | Edge case: empty CSV             |
| test_save_data                       | CSV export                       |
| test_date_column_conversion.         | Datetime conversion.             |
| test_invalid_date_handling.          | Invalid date handling            |

## 📁 Project Structure

```
data-cleaning-pipeline/
├── data_cleaning.py         # Main DataManager class
├── test_cleaning_data.py    # 11 unit tests
├── requirements.txt         # Dependencies
├── LICENSE                  # MIT License
├── .gitignore               # Git ignore rules
└── README.md                # Documentation
```

## 🛠️ Tech Stack

- **Language:** Python 3.8+
- **Libraries:** pandas, numpy
- **Testing:** pytest
- **Design:** Object-Oriented Programming (OOP)

## 👤 Author

**Shaikh Muhammad Maaz**
- GitHub: [@maaz4hope-ui](https://github.com/maaz4hope-ui)

## 🎓 What I Learned

- Object-Oriented Programming (Classes, Methods, Static Methods)
- Writing unit tests with pytest (11 tests)
- Error handling with try-except
- Data cleaning best practices
- Git and GitHub workflow
- Writing professional documentation

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

⭐ **If you find this project useful, please give it a star!**
