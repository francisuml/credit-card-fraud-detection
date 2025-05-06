# Credit Card Fraud Detection 🕵️‍♂️💳

This project detects anomalies in credit card transactions using supervised learning. Built using the `creditcard.csv` dataset.

## Dataset
The original `creditcard.csv` dataset is not included due to GitHub file size restrictions.  
You can download it from [Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud).
Place it in the `data/` directory to run the notebook.

## 📁 Project Structure
.
├── src/ # Python scripts
├── notebooks/ # Jupyter notebooks
├── outputs/ # Plots, HTML exports, reports
├── README.md
├── .gitignore
├── requirements.txt
├── LICENSE

## 🛠️ Features

- Data preprocessing & scaling
- Exploratory Data Analysis
- Model training & evaluation
- ROC & Precision-Recall curve visualizations
- Threshold tuning for better recall
- Hyperparameter tuning (RandomizedSearchCV)

## ⚙️ Setup

```bash
pip install -r requirements.txt

🚀 Run
Jupyter Notebook or:

python src/main.py

📊 Results
Precision: 95.40%

Recall: 84.69%

F1 Score: 89.73%

AUC-ROC: 0.99+

## Author

Francis Carl Sumile 
Machine Learning Practitioner | Data Scientist
GitHub: github.com/francisuml