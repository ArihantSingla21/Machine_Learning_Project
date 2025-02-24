# Student Performance Prediction

## Overview
This machine learning project analyzes and predicts student performance based on various demographic and academic factors. The model aims to predict math scores using features like gender, race/ethnicity, parental education, lunch type, and test preparation course completion status.

## Table of Contents
- [Installation](#installation)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Model Architecture](#model-architecture)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

# Installation
## 1. Clone the repository
bash
git clone https://github.com/ArihantSingla21/student-performance-prediction.git
cd student-performance-prediction
## 2. Create a virtual environment
python -m venv venv
## 3. Activate virtual environment
###     - For Linux/Mac:
source venv/bin/activate
### - For Windows:
venv\Scripts\activate
## 5. Install dependencies
pip install -r requirements.txt

## Dataset
The dataset contains student performance information:
- **Size**: 1000 students, 8 features
- **Features**:
  - Gender
  - Race/ethnicity
  - Parental level of education
  - Lunch type
  - Test preparation course
  - Reading score
  - Writing score
  - Math score (target variable)
- **Preprocessing**:
  - Categorical features encoded using OneHotEncoder
  - Numerical features scaled using StandardScaler
  - Data split into training (80%) and testing (20%) sets

## Project Structure
- `notebook/`
  - `EDA.ipynb`: Exploratory Data Analysis
  - `MODEL TRAINING.ipynb`: Model Training and Evaluation
- `data/`
  - `stud.csv`: Raw dataset
- `src/`
  - `components/`: Contains data ingestion, transformation, and model training modules
  - `utils.py`: Utility functions for saving models and evaluating performance
  - `exception.py`: Custom exception handling
  - `logger.py`: Logging configuration

## Model Architecture
Multiple regression models were implemented and compared:
- Linear Regression
- Lasso Regression
- Ridge Regression
- Decision Tree Regressor
- Random Forest Regressor

Key findings from EDA:
- Students who completed the test preparation course showed higher average scores
- Lunch type and gender showed correlations with performance
- Clear patterns in score distributions across different demographic groups

## Results
Model performance metrics include:
- Mean Absolute Error (MAE)
- Root Mean Square Error (RMSE)
- R-squared (R2) score

Detailed performance metrics for each model are available in the training notebook.

## Contributing
1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

## License
This project is licensed under the [MIT License](LICENSE).

---
Created by [ArihantSingla21](https://github.com/ArihantSingla21)

For questions or support, please open an issue or contact [arihantsingla21@gmail.com]