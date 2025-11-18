
import pandas as pd
import numpy as np
from fredapi import Fred
import os
from dotenv import load_dotenv

pd.set_option("display.max_rows", 20)
pd.set_option("display.max_columns", None)

print("Libraries loaded.")

load_dotenv()
fred_api_key = os.getenv("FRED_API_KEY")

if fred_api_key is None:
    raise ValueError("FRED_API_KEY not found. Make sure it is set as an environment variable.")

fred = Fred(api_key=fred_api_key)

print("FRED API connection initialized.")
