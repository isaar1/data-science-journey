# Netflix Movies & TV Shows - Exploratory Data Analysis (EDA)

## 📌 Project Overview
This project is part of my **Data Science Learning Journey**. The goal is to analyze the **Netflix Movies & TV Shows Dataset** using **Pandas, NumPy, and Data Visualization Libraries** to extract insights.

## 📂 Dataset Information
- **Source:** [Kaggle - Netflix Movies & TV Shows](https://www.kaggle.com/datasets/shivamb/netflix-shows)
- **Rows:** 8,807
- **Columns:** 12 (Title, Type, Country, Release Year, Rating, etc.)
- **Objective:** Clean, analyze, and visualize data trends.

## 🔍 Key Steps in Analysis
### 1️⃣ Data Preprocessing
- Checked for missing values
- Filled missing `country` with "Unknown"
- Replaced missing `rating` with the most common rating
- Dropped unnecessary columns (`director`, `cast`)

### 2️⃣ Exploratory Data Analysis (EDA)
- **Movie vs. TV Show count** 📊
- **Top 10 countries producing Netflix content** 🌍
- **Most common movie ratings** 🎭
- **Number of releases over the years** 📈
- **WordCloud analysis of Netflix titles** 🔤

## 📊 Insights Discovered
- Netflix has **more movies than TV shows**.
- **USA dominates** Netflix content production.
- **Most common rating is TV-MA** (Mature Audience).
- Netflix **releases more content each year**, indicating platform growth.

## 🚀 How to Run the Project
1. Download the dataset from Kaggle.
2. Run `netflix-eda.ipynb` in Jupyter Notebook.
3. Install required libraries if needed:
   ```bash
   pip install pandas numpy matplotlib seaborn wordcloud
   ```
4. Explore the results in Jupyter Notebook.

## 📌 Next Steps
- Apply similar EDA techniques to other datasets.
- Extend analysis by using **SQL** for querying the dataset.
- Experiment with **machine learning models** on Netflix data.

## 🔗 Links
- **GitHub Repository:** [https://github.com/isaar1/data-science-journey/tree/main]
- **LinkedIn Post:** [https://www.linkedin.com/in/isaar/recent-activity/all/]

---
📢 _If you found this useful, feel free to connect with me on LinkedIn!_ 🚀

