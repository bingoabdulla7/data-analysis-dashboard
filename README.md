# 📊 Data Analysis Dashboard

A modern, interactive data analysis application built with Python and Streamlit. This project demonstrates how to create a web-based dashboard for data visualization and analysis.

## 🚀 Features

- **Interactive Data Visualization**: Multiple chart types including line plots, heatmaps, and scatter plots
- **Real-time Data Generation**: Generate sample data with customizable parameters
- **Data Filtering**: Filter data by category and date range
- **Export Functionality**: Download filtered data as CSV
- **Responsive Design**: Modern, mobile-friendly interface
- **Statistical Analysis**: Summary statistics and category analysis

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/data-analysis-dashboard.git
   cd data-analysis-dashboard
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

### Running Locally

1. **Start the Streamlit app**:
   ```bash
   streamlit run streamlit_app.py
   ```

2. **Open your browser** and navigate to `http://localhost:8501`

### Running the Core Application

You can also run the core Python application without the web interface:

```bash
python app.py
```

## 📊 Dashboard Features

### Data Generation
- Generate sample data with customizable number of records
- Data includes sales, temperature, humidity, and category information
- Realistic data patterns for demonstration purposes

### Visualizations
- **Sales Trend**: Line chart showing sales over time
- **Correlation Heatmap**: Matrix showing relationships between variables
- **Category Distribution**: Bar chart of data distribution by category
- **Temperature vs Humidity**: Scatter plot with sales coloring

### Data Analysis
- Summary statistics for all numeric columns
- Category-wise analysis with aggregations
- Interactive filtering by category and date range
- Export filtered data to CSV

## 🏗️ Project Structure

```
data-analysis-dashboard/
├── app.py                 # Core data analysis functionality
├── streamlit_app.py       # Streamlit web interface
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── .gitignore           # Git ignore file
└── .streamlit/          # Streamlit configuration (optional)
    └── config.toml
```

## 🚀 Deployment

### Deploy to Streamlit Cloud

1. **Push your code to GitHub**:
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud**:
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Connect your GitHub account
   - Select your repository
   - Set the main file path to `streamlit_app.py`
   - Click "Deploy"

### Deploy to Heroku

1. **Create a `Procfile`**:
   ```
   web: streamlit run streamlit_app.py --server.port=$PORT --server.address=0.0.0.0
   ```

2. **Deploy using Heroku CLI**:
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

## 🛠️ Customization

### Adding New Chart Types

1. Add new methods to the `DataAnalyzer` class in `app.py`
2. Update the chart selection in `streamlit_app.py`
3. Add corresponding visualization code

### Modifying Data Structure

1. Update the `generate_sample_data` method in `app.py`
2. Adjust the dashboard components in `streamlit_app.py`
3. Update the filtering and analysis sections as needed

## 📝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Support

If you have any questions or need help with the project, please:

1. Check the [Issues](https://github.com/yourusername/data-analysis-dashboard/issues) page
2. Create a new issue if your problem isn't already addressed
3. Contact the maintainers for urgent issues

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) for the amazing web framework
- [Pandas](https://pandas.pydata.org/) for data manipulation
- [Matplotlib](https://matplotlib.org/) and [Seaborn](https://seaborn.pydata.org/) for visualizations
- [NumPy](https://numpy.org/) for numerical computing

---

**Happy Data Analysis! 📊✨** 