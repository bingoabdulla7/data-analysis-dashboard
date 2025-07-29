# ☕️ Café Sales Dashboard

A modern, interactive café sales analysis application built with Python and Streamlit. This project demonstrates how to create a web-based dashboard for data visualization and analysis, with realistic item sales patterns and revenue simulation.

## 🚀 Features

- **Realistic Café Data**: Simulates daily sales for multiple item types, with temperature-driven demand patterns
- **Revenue Simulation**: Assigns prices to each item and calculates daily revenue
- **Interactive Data Visualization**: Multiple chart types including quantity/revenue trends, heatmaps, and bar charts
- **Data Filtering**: Filter by item type and date range
- **Export Functionality**: Download filtered data as CSV
- **Responsive Design**: Modern, mobile-friendly interface
- **Statistical Analysis**: Summary statistics and item type analysis

## ☕️ Item Types and Prices

| Item Type  | Price ($) |
|------------|-----------|
| Coffee     | 3.00      |
| Tea        | 2.50      |
| Pastry     | 2.00      |
| Sandwich   | 5.00      |
| Juice      | 3.50      |
| Salad      | 4.50      |
| Smoothie   | 4.00      |
| Cake       | 3.50      |

- **Sales patterns are temperature-driven**: e.g., more smoothies/juice on hot days, more coffee/pastry on cold days.

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/cafe-sales-dashboard.git
   cd cafe-sales-dashboard
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
- Generates realistic daily sales for each item type
- Simulates temperature and humidity for each day
- Calculates revenue based on item prices

### Visualizations
- **Quantity Sold Trend**: Line chart showing total quantity sold per day
- **Revenue Trend**: Line chart showing total revenue per day
- **Correlation Heatmap**: Matrix showing relationships between quantity, revenue, temperature, etc.
- **Item Type Distribution**: Bar chart of sales by item type
- **Temperature vs Humidity**: Scatter plot colored by quantity sold

### Data Analysis
- Summary statistics for all numeric columns
- Item type analysis (mean, std, count, revenue, etc.)
- Interactive filtering by item type and date range
- Export filtered data to CSV

## 🏗️ Project Structure

```
cafe-sales-dashboard/
├── app.py                 # Core data analysis functionality
├── streamlit_app.py       # Streamlit web interface
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── .gitignore             # Git ignore file
├── .streamlit/            # Streamlit configuration (optional)
│   └── config.toml
└── DEPLOYMENT.md          # Deployment instructions
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

## 🛠️ Customization

- Add new item types or adjust prices in `app.py`
- Change sales patterns for different weather conditions
- Add new visualizations or metrics in `streamlit_app.py`
- Connect to real café data sources

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
1. Check the Issues page
2. Create a new issue if your problem isn't already addressed
3. Contact the maintainers for urgent issues

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) for the amazing web framework
- [Pandas](https://pandas.pydata.org/) for data manipulation
- [Matplotlib](https://matplotlib.org/) and [Seaborn](https://seaborn.pydata.org/) for visualizations
- [NumPy](https://numpy.org/) for numerical computing

---

**Happy Café Data Analysis! ☕️📊✨** 