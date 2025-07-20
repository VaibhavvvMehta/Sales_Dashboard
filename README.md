# E-commerce Data Analysis Platform

## Project Overview
A comprehensive data analysis platform that addresses challenges in inventory, sales, and vendor management through automated extraction, transformation, and loading of multiple diverse CSV datasets. This project delivers actionable insights for e-commerce business optimization.

## Key Features
- **Inventory Management**: Turnover analysis and stock optimization
- **Sales Performance**: Revenue trends and customer behavior analysis
- **Vendor Analysis**: Performance metrics and cost analysis
- **Business Intelligence**: KPIs and operational efficiency metrics

## Datasets Analyzed
1. **Amazon Sale Report** (128,975 records) - Main sales data
2. **International Sale Report** (37,432 records) - Global sales
3. **Sale Report** (9,271 records) - General sales data
4. **May 2022 Sales** (1,330 records) - Monthly performance
5. **P&L March 2021** (1,330 records) - Profit/Loss analysis
6. **Cloud Warehouse Comparison** (50 records) - Warehouse analysis
7. **Expense Report** (17 records) - Cost analysis

**Total Records Processed: 178,405**

## Key Insights Generated
- **Revenue Performance**: ₹78.6M total revenue from 128,975 orders
- **Inventory Risk**: 38.9% of SKUs at critical stock levels (3,606 items)
- **Customer Retention**: High loyalty with 216 orders per customer average
- **International Presence**: 173 customers across 37,432 global orders
- **Operational Efficiency**: 13.9 orders per SKU average

## Technical Stack
- **Python**: Data processing and analysis
- **Pandas**: Data manipulation and cleaning
- **Matplotlib/Seaborn**: Data visualization
- **NumPy**: Numerical computations
- **Jupyter Notebook**: Interactive analysis environment

## Project Structure
```
ecommerce/
├── dataset/                    # Raw CSV data files
├── ecommerce_data_analysis.ipynb  # Main analysis notebook
├── data_extraction.py         # ETL pipeline script
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

## Installation & Setup

### Prerequisites
- Python 3.9 or higher
- pip package manager

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ecommerce-data-analysis.git
   cd ecommerce-data-analysis
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # or
   source .venv/bin/activate  # Linux/Mac
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Launch Jupyter Notebook:
   ```bash
   jupyter notebook ecommerce_data_analysis.ipynb
   ```

## Usage

### Running the Analysis
1. **Data Loading**: Automatically loads and processes 7 CSV datasets
2. **Data Cleaning**: Standardizes formats, handles missing values, removes duplicates
3. **Analysis Modules**:
   - Inventory management analysis
   - Sales performance metrics
   - Vendor and cost analysis
   - Business intelligence dashboard
4. **Visualizations**: Interactive charts and graphs
5. **Insights & Recommendations**: Actionable business insights

### Key Analysis Features
- **Automated ETL Pipeline**: Robust data loading with encoding detection
- **Risk Assessment**: Inventory stock level categorization
- **Performance Metrics**: Revenue, customer retention, operational KPIs
- **Visual Analytics**: Multi-chart dashboards for business insights

## Results & Recommendations

### Critical Business Insights
1. **Immediate Action Required**: 3,606 SKUs need restocking
2. **Revenue Optimization**: Focus on high-performing categories
3. **Customer Strategy**: Enhance retention programs (current: 216 orders/customer)
4. **International Growth**: Expand global market presence
5. **Operational Excellence**: Optimize inventory management systems

### Business Impact
- Identified ₹78.6M revenue opportunities
- Highlighted critical inventory risks affecting 38.9% of SKUs
- Provided data-driven recommendations for business growth
- Created automated reporting pipeline for ongoing analysis

## File Descriptions
- **`ecommerce_data_analysis.ipynb`**: Complete analysis workflow with visualizations
- **`data_extraction.py`**: ETL script for data processing and MySQL integration
- **`dataset/`**: Contains all raw CSV data files for analysis
- **`requirements.txt`**: Python package dependencies

## Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
- **Project Author**: [Your Name]
- **Email**: [your.email@example.com]
- **LinkedIn**: [Your LinkedIn Profile]

## Acknowledgments
- Data analysis techniques inspired by modern e-commerce analytics
- Visualization design following data science best practices
- Built with Python data science ecosystem tools

---
*This project demonstrates end-to-end data analysis capabilities for e-commerce business intelligence and decision-making.*
