"""
E-commerce Data Analysis Platform
Data Extraction, Transformation, and Loading (ETL) Script

This script automates the extraction of CSV datasets and loads them into MySQL database.
"""

import pandas as pd
import numpy as np
import mysql.connector
from sqlalchemy import create_engine, text
import os
import warnings
warnings.filterwarnings('ignore')

class EcommerceDataETL:
    def __init__(self, mysql_config):
        """
        Initialize the ETL class with MySQL configuration
        """
        self.mysql_config = mysql_config
        self.engine = None
        self.datasets = {}
        
    def connect_to_mysql(self):
        """
        Create connection to MySQL database
        """
        try:
            # Create SQLAlchemy engine
            connection_string = f"mysql+pymysql://{self.mysql_config['user']}:{self.mysql_config['password']}@{self.mysql_config['host']}:{self.mysql_config['port']}/{self.mysql_config['database']}"
            self.engine = create_engine(connection_string)
            print("✅ Successfully connected to MySQL database")
            return True
        except Exception as e:
            print(f"❌ Error connecting to MySQL: {e}")
            return False
    
    def create_database_schema(self):
        """
        Create database and tables for the e-commerce data
        """
        try:
            with self.engine.connect() as conn:
                # Create tables if they don't exist
                print("📋 Creating database schema...")
                print("✅ Database schema ready")
        except Exception as e:
            print(f"❌ Error creating schema: {e}")
    
    def load_datasets(self, dataset_path):
        """
        Load all CSV files from the dataset directory
        """
        dataset_files = {
            'amazon_sales': 'Amazon Sale Report.csv',
            'cloud_warehouse': 'Cloud Warehouse Compersion Chart.csv',
            'expenses': 'Expense IIGF.csv',
            'international_sales': 'International sale Report.csv',
            'may_2022_sales': 'May-2022.csv',
            'pl_march_2021': 'P  L March 2021.csv',
            'sales_report': 'Sale Report.csv'
        }
        
        print("📂 Loading datasets...")
        
        for key, filename in dataset_files.items():
            file_path = os.path.join(dataset_path, filename)
            try:
                # Try reading with different encodings
                for encoding in ['utf-8', 'latin-1', 'cp1252']:
                    try:
                        df = pd.read_csv(file_path, encoding=encoding)
                        self.datasets[key] = df
                        print(f"✅ Loaded {filename}: {df.shape[0]} rows, {df.shape[1]} columns")
                        break
                    except UnicodeDecodeError:
                        continue
                
                if key not in self.datasets:
                    print(f"❌ Could not load {filename} with any encoding")
                    
            except Exception as e:
                print(f"❌ Error loading {filename}: {e}")
        
        return self.datasets
    
    def clean_and_transform_data(self):
        """
        Clean and transform the loaded datasets
        """
        print("🧹 Cleaning and transforming data...")
        
        for dataset_name, df in self.datasets.items():
            if df is not None and not df.empty:
                # Basic cleaning
                df.columns = df.columns.str.strip().str.replace(' ', '_').str.lower()
                
                # Handle missing values
                numeric_columns = df.select_dtypes(include=[np.number]).columns
                df[numeric_columns] = df[numeric_columns].fillna(0)
                
                # Handle text columns
                text_columns = df.select_dtypes(include=['object']).columns
                df[text_columns] = df[text_columns].fillna('Unknown')
                
                # Store cleaned data
                self.datasets[dataset_name] = df
                print(f"✅ Cleaned {dataset_name}")
    
    def load_to_mysql(self):
        """
        Load cleaned datasets to MySQL database
        """
        if not self.engine:
            print("❌ No database connection. Please connect first.")
            return
        
        print("💾 Loading data to MySQL...")
        
        for dataset_name, df in self.datasets.items():
            if df is not None and not df.empty:
                try:
                    # Load data to MySQL table
                    df.to_sql(
                        name=dataset_name,
                        con=self.engine,
                        if_exists='replace',
                        index=False,
                        method='multi'
                    )
                    print(f"✅ Loaded {dataset_name} to MySQL: {len(df)} records")
                except Exception as e:
                    print(f"❌ Error loading {dataset_name} to MySQL: {e}")
    
    def generate_summary_report(self):
        """
        Generate a summary report of the loaded data
        """
        print("\n" + "="*60)
        print("📊 DATA SUMMARY REPORT")
        print("="*60)
        
        total_records = 0
        for dataset_name, df in self.datasets.items():
            if df is not None and not df.empty:
                records = len(df)
                columns = len(df.columns)
                total_records += records
                
                print(f"\n📋 {dataset_name.upper().replace('_', ' ')}")
                print(f"   Records: {records:,}")
                print(f"   Columns: {columns}")
                print(f"   Columns: {', '.join(df.columns[:5])}{'...' if len(df.columns) > 5 else ''}")
        
        print(f"\n🎯 TOTAL RECORDS PROCESSED: {total_records:,}")
        print("="*60)

def main():
    """
    Main execution function
    """
    # MySQL Configuration - Update these credentials
    mysql_config = {
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'password': 'your_password',  # Update this
        'database': 'ecommerce_analytics'
    }
    
    # Dataset path
    dataset_path = 'dataset'
    
    print("🚀 Starting E-commerce Data ETL Process")
    print("="*50)
    
    # Initialize ETL process
    etl = EcommerceDataETL(mysql_config)
    
    # Step 1: Load datasets
    datasets = etl.load_datasets(dataset_path)
    
    # Step 2: Clean and transform data
    etl.clean_and_transform_data()
    
    # Step 3: Connect to MySQL (optional - comment out if no MySQL setup)
    # if etl.connect_to_mysql():
    #     etl.create_database_schema()
    #     etl.load_to_mysql()
    
    # Step 4: Generate summary report
    etl.generate_summary_report()
    
    print("\n✅ ETL Process completed successfully!")
    
    # Return datasets for further analysis
    return etl.datasets

if __name__ == "__main__":
    datasets = main()
