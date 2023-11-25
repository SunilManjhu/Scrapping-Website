# NIFTY 50 Historical Data Extractor

This Python script is designed to extract historical data for the NIFTY 50 index from the NSE Nifty Indices website. The extracted data includes information such as the date, open, high, low, close, and volume.

## Prerequisites

Before running the script, make sure you have the following dependencies installed:

- Python 3.x
- requests library: `pip install requests`
- BeautifulSoup library: `pip install beautifulsoup4`
- pandas library: `pip install pandas`

## Usage

1. Clone this repository or download the `nifty50_historical_data.py` script.

```bash
git clone https://github.com/your-username/nifty50-historical-data-extractor.git
cd nifty50-historical-data-extractor
```

2. Run the script using the following command:

```bash
python nifty50_historical_data.py
```

3. The script will fetch the historical data from the NSE Nifty Indices website and save it as a CSV file named `nifty50_historical_data.csv` in the same directory.

## Notes

- Ensure that web scraping is allowed according to the terms of service on the NSE Nifty Indices website.
- The HTML structure of the website may change over time, so you may need to update the script accordingly.
- If you encounter any issues, please check the status code returned by the website and review the script.

