import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from app import DataAnalyzer
from datetime import datetime

# Set page configuration
st.set_page_config(
    page_title="Café Sales Dashboard",
    page_icon="☕️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #8d5524;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Header
    st.markdown('<h1 class="main-header">☕️ Café Sales Dashboard</h1>', unsafe_allow_html=True)
    
    # Initialize the analyzer
    analyzer = DataAnalyzer()
    
    # Sidebar controls
    st.sidebar.header("⚙️ Controls")
    
    # Data generation controls
    st.sidebar.subheader("Data Settings")
    num_rows = st.sidebar.slider("Number of data points", 50, 500, 100, 10)
    
    if st.sidebar.button("🔄 Generate New Data"):
        st.session_state.data_generated = False
    
    # Generate data if not already done
    if 'data_generated' not in st.session_state or not st.session_state.data_generated:
        with st.spinner("Generating sample data..."):
            data = analyzer.generate_sample_data(num_rows)
            st.session_state.data = data
            st.session_state.analyzer = analyzer  # Store analyzer with data
            st.session_state.data_generated = True
            st.success("Data generated successfully!")
    
    # Main content
    if st.session_state.data_generated:
        data = st.session_state.data
        
        # Key metrics
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            st.metric("Total Records", len(data))
        
        with col2:
            avg_qty = data['quantity_sold'].mean()
            st.metric("Avg. Quantity Sold", f"{avg_qty:.1f}")
        
        with col3:
            avg_temp = data['temperature'].mean()
            st.metric("Avg. Temperature", f"{avg_temp:.1f}°C")
        
        with col4:
            avg_humidity = data['humidity'].mean()
            st.metric("Avg. Humidity", f"{avg_humidity:.1f}%")
        
        with col5:
            total_revenue = data['revenue'].sum()
            avg_revenue = data['revenue'].mean()
            st.metric("Total Revenue", f"${total_revenue:,.2f}")
            st.caption(f"Avg. Revenue/Record: ${avg_revenue:,.2f}")
        
        # Data overview
        st.subheader("📋 Data Overview")
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.dataframe(data.head(10), use_container_width=True)
        
        with col2:
            st.write("**Dataset Info:**")
            st.write(f"- Shape: {data.shape}")
            st.write(f"- Date Range: {data['date'].min().strftime('%Y-%m-%d')} to {data['date'].max().strftime('%Y-%m-%d')}")
            st.write(f"- Item Types: {data['item_type'].unique().tolist()}")
        
        # Charts section
        st.subheader("📈 Visualizations")
        
        # Chart selection
        chart_type = st.selectbox(
            "Select Chart Type",
            ["Quantity Sold Trend", "Revenue Trend", "Correlation Heatmap", "Item Type Distribution", "Temperature vs Humidity"]
        )
        
        if chart_type == "Quantity Sold Trend":
            fig = st.session_state.analyzer.create_quantity_chart()
            if fig:
                st.pyplot(fig)
                st.caption("Total quantity sold trend over time.")
        
        elif chart_type == "Revenue Trend":
            fig = st.session_state.analyzer.create_revenue_chart()
            if fig:
                st.pyplot(fig)
                st.caption("Total revenue trend over time.")
        
        elif chart_type == "Correlation Heatmap":
            fig = st.session_state.analyzer.create_correlation_heatmap()
            if fig:
                st.pyplot(fig)
                st.caption("Correlation matrix between numeric variables.")
        
        elif chart_type == "Item Type Distribution":
            fig, ax = plt.subplots(figsize=(8, 6))
            data['item_type'].value_counts().plot(kind='bar', ax=ax)
            ax.set_title('Distribution by Item Type')
            ax.set_xlabel('Item Type')
            ax.set_ylabel('Count')
            plt.tight_layout()
            st.pyplot(fig)
            st.caption("Distribution of records across item types.")
        
        elif chart_type == "Temperature vs Humidity":
            fig, ax = plt.subplots(figsize=(10, 6))
            scatter = ax.scatter(data['temperature'], data['humidity'], 
                               c=data['quantity_sold'], cmap='viridis', alpha=0.6)
            ax.set_xlabel('Temperature (°C)')
            ax.set_ylabel('Humidity (%)')
            ax.set_title('Temperature vs Humidity (colored by Quantity Sold)')
            plt.colorbar(scatter, ax=ax, label='Quantity Sold')
            plt.tight_layout()
            st.pyplot(fig)
            st.caption("Scatter plot showing relationship between temperature and humidity, colored by quantity sold.")
        
        # Data analysis section
        st.subheader("🔍 Data Analysis")
        
        # Summary statistics
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Summary Statistics:**")
            st.dataframe(st.session_state.analyzer.get_summary_stats())
        
        with col2:
            st.write("**Item Type Analysis:**")
            item_type_stats = data.groupby('item_type').agg({
                'quantity_sold': ['mean', 'std', 'count'],
                'revenue': ['sum', 'mean'],
                'temperature': 'mean',
                'humidity': 'mean'
            }).round(2)
            st.dataframe(item_type_stats)
        
        # Filtering options
        st.subheader("🔍 Data Filtering")
        col1, col2 = st.columns(2)
        
        with col1:
            selected_item_type = st.selectbox("Filter by Item Type", ['All'] + data['item_type'].unique().tolist())
        
        with col2:
            date_range = st.date_input(
                "Select Date Range",
                value=(data['date'].min().date(), data['date'].max().date()),
                min_value=data['date'].min().date(),
                max_value=data['date'].max().date()
            )
        
        # Apply filters
        filtered_data = data.copy()
        
        if selected_item_type != 'All':
            filtered_data = filtered_data[filtered_data['item_type'] == selected_item_type]
        
        if len(date_range) == 2:
            start_date, end_date = date_range
            filtered_data = filtered_data[
                (filtered_data['date'].dt.date >= start_date) &
                (filtered_data['date'].dt.date <= end_date)
            ]
        
        st.write(f"**Filtered Data ({len(filtered_data)} records):**")
        st.dataframe(filtered_data, use_container_width=True)
        
        # Download option
        st.subheader("💾 Export Data")
        csv = filtered_data.to_csv(index=False)
        st.download_button(
            label="📥 Download Filtered Data as CSV",
            data=csv,
            file_name=f"filtered_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv"
        )

if __name__ == "__main__":
    main() 