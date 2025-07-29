import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import streamlit as st

class DataAnalyzer:
    """A café sales analysis tool for Streamlit, with realistic item sales patterns and revenue calculation."""
    
    def __init__(self):
        self.data = None
    
    def generate_sample_data(self, rows=100):
        """Generate sample café sales data with realistic patterns and revenue."""
        np.random.seed(42)
        dates = pd.date_range(start='2023-01-01', periods=rows, freq='D')
        item_types = ['Coffee', 'Tea', 'Pastry', 'Sandwich', 'Juice', 'Salad', 'Smoothie', 'Cake']
        prices = {
            'Coffee': 3.0,
            'Tea': 2.5,
            'Pastry': 2.0,
            'Sandwich': 5.0,
            'Juice': 3.5,
            'Salad': 4.5,
            'Smoothie': 4.0,
            'Cake': 3.5
        }
        data = {
            'date': [],
            'item_type': [],
            'quantity_sold': [],
            'temperature': [],
            'humidity': [],
            'price': [],
            'revenue': []
        }
        for i in range(rows):
            date = dates[i]
            temp = np.random.normal(20, 10)
            humidity = np.random.uniform(30, 80)
            for item in item_types:
                # Base sales
                base = 80 if item in ['Coffee', 'Tea'] else 40
                # Adjust for temperature
                if item == 'Coffee':
                    qty = np.random.poisson(base + max(0, 15 - temp) * 3)
                elif item == 'Tea':
                    qty = np.random.poisson(base + max(0, 10 - temp) * 2)
                elif item == 'Smoothie':
                    qty = np.random.poisson(30 + max(0, temp - 18) * 3)
                elif item == 'Juice':
                    qty = np.random.poisson(25 + max(0, temp - 15) * 2)
                elif item == 'Salad':
                    qty = np.random.poisson(20 + max(0, temp - 20) * 2)
                elif item == 'Pastry':
                    qty = np.random.poisson(30 + max(0, 15 - temp) * 2)
                elif item == 'Sandwich':
                    qty = np.random.poisson(35 + max(0, temp - 10))
                elif item == 'Cake':
                    qty = np.random.poisson(20 + max(0, 12 - temp))
                else:
                    qty = np.random.poisson(20)
                price = prices[item]
                revenue = qty * price
                data['date'].append(date)
                data['item_type'].append(item)
                data['quantity_sold'].append(qty)
                data['temperature'].append(temp)
                data['humidity'].append(humidity)
                data['price'].append(price)
                data['revenue'].append(revenue)
        self.data = pd.DataFrame(data)
        return self.data
    
    def get_summary_stats(self):
        """Get summary statistics of the data."""
        if self.data is None:
            return None
        return self.data.describe()
    
    def create_quantity_chart(self):
        """Create a quantity sold trend chart (total per day)."""
        if self.data is None:
            return None
        daily = self.data.groupby('date')['quantity_sold'].sum()
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(daily.index, daily.values)
        ax.set_title('Total Quantity Sold Trend Over Time')
        ax.set_xlabel('Date')
        ax.set_ylabel('Total Quantity Sold')
        ax.tick_params(axis='x', rotation=45)
        plt.tight_layout()
        return fig
    
    def create_revenue_chart(self):
        """Create a daily revenue trend chart."""
        if self.data is None:
            return None
        daily = self.data.groupby('date')['revenue'].sum()
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(daily.index, daily.values, color='green')
        ax.set_title('Total Revenue Trend Over Time')
        ax.set_xlabel('Date')
        ax.set_ylabel('Total Revenue ($)')
        ax.tick_params(axis='x', rotation=45)
        plt.tight_layout()
        return fig
    
    def create_correlation_heatmap(self):
        """Create a correlation heatmap for numeric columns."""
        if self.data is None:
            return None
        numeric_data = self.data[['quantity_sold', 'temperature', 'humidity', 'price', 'revenue']]
        correlation_matrix = numeric_data.corr()
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, ax=ax)
        ax.set_title('Correlation Heatmap')
        plt.tight_layout()
        return fig
    
    def filter_by_item_type(self, item_type):
        """Filter data by item type."""
        if self.data is None:
            return None
        return self.data[self.data['item_type'] == item_type]

def main():
    """Main function to run the application."""
    analyzer = DataAnalyzer()
    data = analyzer.generate_sample_data()
    print("Sample café sales data generated successfully!")
    print(f"Dataset shape: {data.shape}")
    print("\nFirst few rows:")
    print(data.head())
    print("\nSummary Statistics:")
    print(analyzer.get_summary_stats())
    return analyzer

if __name__ == "__main__":
    analyzer = main() 