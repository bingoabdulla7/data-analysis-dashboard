import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import streamlit as st

class DataAnalyzer:
    """A simple data analysis tool that can be used with Streamlit."""
    
    def __init__(self):
        self.data = None
    
    def generate_sample_data(self, rows=100):
        """Generate sample data for demonstration."""
        np.random.seed(42)
        dates = pd.date_range(start='2023-01-01', periods=rows, freq='D')
        
        data = {
            'date': dates,
            'sales': np.random.normal(1000, 200, rows),
            'temperature': np.random.normal(20, 10, rows),
            'humidity': np.random.uniform(30, 80, rows),
            'category': np.random.choice(['A', 'B', 'C'], rows)
        }
        
        self.data = pd.DataFrame(data)
        return self.data
    
    def get_summary_stats(self):
        """Get summary statistics of the data."""
        if self.data is None:
            return None
        return self.data.describe()
    
    def create_sales_chart(self):
        """Create a sales trend chart."""
        if self.data is None:
            return None
        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(self.data['date'], self.data['sales'])
        ax.set_title('Sales Trend Over Time')
        ax.set_xlabel('Date')
        ax.set_ylabel('Sales')
        ax.tick_params(axis='x', rotation=45)
        plt.tight_layout()
        return fig
    
    def create_correlation_heatmap(self):
        """Create a correlation heatmap."""
        if self.data is None:
            return None
        
        numeric_data = self.data.select_dtypes(include=[np.number])
        correlation_matrix = numeric_data.corr()
        
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, ax=ax)
        ax.set_title('Correlation Heatmap')
        plt.tight_layout()
        return fig
    
    def filter_by_category(self, category):
        """Filter data by category."""
        if self.data is None:
            return None
        return self.data[self.data['category'] == category]

def main():
    """Main function to run the application."""
    analyzer = DataAnalyzer()
    
    # Generate sample data
    data = analyzer.generate_sample_data()
    print("Sample data generated successfully!")
    print(f"Dataset shape: {data.shape}")
    print("\nFirst few rows:")
    print(data.head())
    
    # Show summary statistics
    print("\nSummary Statistics:")
    print(analyzer.get_summary_stats())
    
    return analyzer

if __name__ == "__main__":
    analyzer = main() 