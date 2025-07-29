#!/usr/bin/env python3
"""
Simple test script to verify the data analyzer works correctly.
"""

import sys
import os

# Add the current directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import DataAnalyzer

def test_data_analyzer():
    """Test the DataAnalyzer class functionality."""
    print("🧪 Testing DataAnalyzer...")
    
    # Initialize analyzer
    analyzer = DataAnalyzer()
    
    # Test data generation
    print("📊 Generating sample data...")
    data = analyzer.generate_sample_data(50)
    print(f"✅ Generated {len(data)} records")
    print(f"📋 Data shape: {data.shape}")
    print(f"📅 Date range: {data['date'].min()} to {data['date'].max()}")
    
    # Test summary statistics
    print("\n📈 Testing summary statistics...")
    stats = analyzer.get_summary_stats()
    if stats is not None:
        print("✅ Summary statistics generated successfully")
        print(stats)
    else:
        print("❌ Failed to generate summary statistics")
    
    # Test chart generation
    print("\n📊 Testing chart generation...")
    sales_chart = analyzer.create_sales_chart()
    if sales_chart is not None:
        print("✅ Sales chart generated successfully")
    else:
        print("❌ Failed to generate sales chart")
    
    heatmap = analyzer.create_correlation_heatmap()
    if heatmap is not None:
        print("✅ Correlation heatmap generated successfully")
    else:
        print("❌ Failed to generate correlation heatmap")
    
    # Test filtering
    print("\n🔍 Testing data filtering...")
    filtered_data = analyzer.filter_by_category('A')
    if filtered_data is not None:
        print(f"✅ Filtered data: {len(filtered_data)} records for category 'A'")
    else:
        print("❌ Failed to filter data")
    
    print("\n🎉 All tests completed!")

if __name__ == "__main__":
    test_data_analyzer() 