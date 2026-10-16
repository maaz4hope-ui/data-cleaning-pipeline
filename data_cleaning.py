import pandas as pd
import numpy as np


class DataManager:
    """
    A class for loading, cleaning, and saving CSV data.

    Attributes:
        total_files_processed (int): Class variable tracking total files loaded.
        file_path (str): Path to the CSV file.
        df (pd.DataFrame): Loaded dataframe.
        cleaned_status (bool): Whether data has been cleaned.
    """
    total_files_processed = 0

    def __init__(self, file_path):
        """
        Initialize DataManager with a file path.

        Args:
            file_path (str): Path to the CSV file.
        """

        self.file_path = file_path
        self.df = None
        self.cleaned_status = False

    def __repr__(self):
        """String representation of DataManager object."""
        status = "loaded" if self.df is not None else "not loaded"
        cleaned = "cleaned" if self.cleaned_status else "not cleaned"
        rows = len(self.df) if self.df is not None else 0
        return f"DataManager(file='{self.file_path}', rows={rows}, {status}, {cleaned})"

    def load_data(self):
        """
        Load CSV file into a pandas DataFrame.

        Returns:
            pd.DataFrame: Loaded data, or None if file not found or error occurs.
        """
        try:
            self.df = pd.read_csv(self.file_path)
            print(f"✅ Data loaded! Rows: {self.df.shape[0]}, Columns: {self.df.shape[1]}")
            DataManager.total_files_processed += 1
        except FileNotFoundError:
            print(f"File Not Found: {self.file_path}")
        except Exception as e:
            print(f"Error: {e}")
        return self.df

    def clean_data(self):
        """
        Clean the loaded data: remove duplicates, fill missing values, convert dates.

        Returns:
            pd.DataFrame: Cleaned data, or None if data not loaded.
        """
        if self.df is None or self.df.empty:
            print("🚨 Load data first!")
            return None

        try:
            self.df = self.df.drop_duplicates()
            numeric_cols = self.df.select_dtypes(include=np.number).columns
            text_cols = self.df.select_dtypes(include=['object', 'category']).columns
            for col in numeric_cols:
                self.df[col] = self.df[col].fillna(self.df[col].median())
            for col in text_cols:
                mode_val = self.df[col].mode()
                self.df[col] = self.df[col].fillna(mode_val[0] if not mode_val.empty else 'Unknown')

            # Try to convert text columns to datetime if possible
            date_keywords=['date','time','day','month','year','dob','created','updated']
            for col in self.df.select_dtypes(include=['object']).columns:
                if any(keyword in col.lower() for keyword in date_keywords):
                    try:
                        self.df[col] = pd.to_datetime(self.df[col])
                    except (ValueError,TypeError):
                        pass

            self.cleaned_status = True
            print(f"✅ Cleaned! Remaining rows: {len(self.df)}")
        except Exception as e:
            print(f"Error: {e}")
        return self.df

    def remove_outlier(self, threshold=1.5):
        """
        Remove outliers from numeric columns using IQR method.

        Args:
            threshold (float): Multiplier for IQR bounds. Default 1.5.

        Returns:
            pd.DataFrame: Data with outliers removed.
        """
        if self.df is None or self.df.empty:
            print("🚨 Load data first!")
            return None

        if not self.cleaned_status:
            print("🚨 Warning Data is not cleaned yet, Cleaning Now....")
            self.clean_data()

        try:
            num_col = self.df.select_dtypes(include=np.number).columns
            initial_rows = len(self.df)
            for col in num_col:
                Q1 = self.df[col].quantile(0.25)
                Q3 = self.df[col].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - threshold * IQR
                upper_bound = Q3 + threshold * IQR
                self.df = self.df[(self.df[col] >= lower_bound) & (self.df[col] <= upper_bound)]
            remove = initial_rows - len(self.df)
            print(f"✅ {remove} outliers removed!")
        except Exception as e:
            print(e)

        self.df=self.df.reset_index(drop=True)
        return self.df

    def get_summary(self):
        """
        Print a summary of the dataframe: info, numeric and text description.
        """
        if self.df is None or self.df.empty:
            print("Load Data First!")
            return None


        print(f"\n📊 Data Info: ")
        self.df.info()
        print(f"\n📉Data Description: ")

        #For Numeric Data..
        print("🔢Numeric Summary:")
        print(self.df.describe())

        #For Text Data..
        print("Text Summary: ")
        print(self.df.describe(include=['object','category']))

        print("Columns Data Types:")
        for col in self.df.columns:
            print(f"{col} : {self.df[col].dtype}")

    def save_data(self, output_path="cleaned_data.csv"):
        """
        Save cleaned data to a CSV file.
        
        Args:
            output_path (str): Destination path. Default 'cleaned_data.csv'.
        """
        if self.df is None or self.df.empty:
            print("🚨 Data is empty!")
            return

        if not output_path.endswith('.csv'):
            print(f"⚠️Warning! '{output_path}' should end with '.csv'")

        self.df.to_csv(output_path, index=False)
        print(f"📤 Saved to {output_path}")

    @staticmethod
    def check_column_exists(df, col_name):
        """
        Check if a column exists in a DataFrame.
        
        Args:
            df (pd.DataFrame): DataFrame to check.
            col_name (str): Column name to search.
            
        Returns:
            bool: True if column exists, False otherwise.
        """
        if df is None:
            return False
        return col_name in df.columns
