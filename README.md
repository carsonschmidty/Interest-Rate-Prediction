# Federal Funds Rate Prediction Using Big Mac Index & FRED Data

This project uses machine learning regression methods to predict the U.S. Federal Funds Rate
based on macroeconomic indicators from Federal Reserve Economic Data (FRED) and the Big Mac Index
(purchasing power parity metrics published by The Economist).

You will need a FRED api key to replicate this project.
To beign, get your api key from: https://fredaccount.stlouisfed.org/apikey
Store it in a variable named FRED_API_KEY within a .env file.

## 📌 Project Goals
- Build a monthly macroeconomic dataset with aligned mixed-frequency indicators
- Engineer lagged, rolling, and growth features for time-series prediction
- Compare Linear Regression, Ridge/Lasso, KNN Regression, and Support Vector Regression (SVR)
- Evaluate error and directional accuracy on 2016–2024 out-of-sample forecasts

## 📂 Repository Structure
