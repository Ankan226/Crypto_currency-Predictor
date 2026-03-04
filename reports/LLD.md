# Low Level Design (LLD)

## Module Breakdown

### data_preprocessing.py

Responsibilities:
- Load dataset
- Handle missing values
- Convert date format
- Save cleaned dataset

---

### feature_engineering.py

Responsibilities:
- Generate moving averages
- Compute volatility
- Calculate liquidity ratio
- Compute price range
- Save processed dataset

---

### model_training.py

Responsibilities:
- Load processed dataset
- Split dataset into train and test sets
- Train Random Forest model
- Save trained model

---

### evaluation.py

Responsibilities:
- Load trained model
- Evaluate model performance
- Compute evaluation metrics (RMSE, MAE, R²)

---

### streamlit_app.py

Responsibilities:
- Provide user interface
- Collect input features
- Run trained model
- Display predicted volatility