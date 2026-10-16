import pandas as pd
import pytest
import os
from data_cleaning import DataManager
def test_file_not_found():
    """Test that load_data returns None when file doesn't exist."""
    manager=DataManager("non_Existant.csv")
    result=manager.load_data()
    assert result is None

def test_load_data_success(tmp_path):
    """Test that data loads correctly from a valid CSV."""
    csv_file=tmp_path/"sample.csv"
    csv_file.write_text("Name,Age,Salary\nAli,22,35000\nSara,25,40000")
    manager=DataManager(csv_file)
    result=manager.load_data()
    assert result is not None
    assert result.shape == (2,3)
    assert list(result.columns) == ["Name","Age","Salary"]

def test_data_cleaning_fill_missing(tmp_path):
    """Test that missing values are filled correctly."""
    csv_file=tmp_path/"sample.csv"
    csv_file.write_text("Name,Age,Salary\nAli,,35000\n,22,22000\n")
    manager=DataManager(str(csv_file))
    manager.load_data()
    result=manager.clean_data()
    assert result.isnull().sum().sum() == 0
    assert len(result) == 2

def test_data_cleaning_remove_duplicates(tmp_path):
    """Test that duplicate rows are removed."""
    csv_file=tmp_path/"sample.csv"
    csv_file.write_text("Name,Age,Salary\nAli,22,22000\nAli,22,22000\nSara,24,34000\n")
    manager=DataManager(str(csv_file))
    manager.load_data()
    result=manager.clean_data()
    assert len(result)  == 2

def test_remove_outliers(tmp_path):
    """Test that outliers are removed using IQR method."""
    csv_file=tmp_path/"sample.csv"
    csv_file.write_text("Age,Salary\n22,24000\n32,44000\n26,30000\n200,5000000\n")
    manager=DataManager(csv_file)
    manager.load_data()
    result=manager.remove_outlier()
    assert len(result) <4
    assert result['Age'].max() < 100

def test_check_column_exists():
    """Test the static method check_column_exists."""
    df=pd.DataFrame({"Name":["Ali"],"Age":[22]})
    assert DataManager.check_column_exists(df,"Name") is True
    assert DataManager.check_column_exists(df,"Salary") is False
    assert DataManager.check_column_exists(None,"Age") is False

def test_total_files_processed(tmp_path):
    """Test that total_files_processed increments correctly."""
    file1=tmp_path/"file1.csv"
    file1.write_text("Name,Age\nAli,22\n")

    file2=tmp_path/"file2.csv"
    file2.write_text("City,Population\nKarachi,30000000\n")

    DataManager.total_files_processed=0

    manager1=DataManager(str(file1))
    manager2=DataManager(str(file2))

    manager1.load_data()
    manager2.load_data()

    assert DataManager.total_files_processed==2

def test_empty_csv(tmp_path):
    """Test behavior when CSV contains only headers."""
    csv_file = tmp_path / "empty.csv"
    csv_file.write_text("Name,Age\n")  # Sirf header, koi data nahi

    manager = DataManager(str(csv_file))
    result = manager.load_data()

    assert result is not None
    assert result.shape==(0,2)

def test_save_data(tmp_path):
    """Test that cleaned data is saved to CSV."""
    csv_file=tmp_path/"sample.csv"
    csv_file.write_text("Name,Age\nAli,22\n")

    output_file=tmp_path/"output.csv"

    manager=DataManager(str(csv_file))
    manager.load_data()
    manager.clean_data()
    manager.save_data(str(output_file))

    assert output_file.exists() is True

def test_date_column_conversion(tmp_path):
    """Test that date-like columns are converted to datetime."""
    csv_file = tmp_path / "sample.csv"
    csv_file.write_text("Name,join_date\nAli,2024-01-15\nSara,2024-03-20\n")

    manager = DataManager(str(csv_file))
    manager.load_data()
    result = manager.clean_data()

    assert pd.api.types.is_datetime64_any_dtype(result['join_date'])

def test_invalid_date_handling(tmp_path):
    """Test that invalid dates don't crash the cleaning process."""
    csv_file = tmp_path / "sample.csv"
    csv_file.write_text("Name,join_date\nAli,2024-01-15\nSara,not_a_date\n")

    manager = DataManager(str(csv_file))
    manager.load_data()
    result = manager.clean_data()

    assert result is not None
