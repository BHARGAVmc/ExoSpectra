 Excited to share my Machine Learning project — **ExoSpectra: AI Powered Exoplanet Detection System** 🌍

An exoplanet is a planet that exists outside our solar system. Scientists discover these planets using huge amounts of telescope and space observation data collected from NASA missions. Since this data is very large and complex, manually analyzing and identifying exoplanets becomes difficult and time consuming.

To solve this problem, we started working on an AI-based solution during the **NASA Space Apps Challenge 2025**. The main goal of this project is to help in identifying exoplanets and classifying their types using Machine Learning techniques.

Initially, our model achieved around **95% accuracy**, but we noticed an important issue — the **precision and recall values were low**, which means the model could sometimes make incorrect predictions even with good accuracy.

Recently, I improved the project by:
 Better preprocessing and feature handling
 Improving feature matching during prediction
 Optimizing the Random Forest model
 Handling categorical data more effectively

After these improvements, the model achieved around **97% accuracy** with significantly better **precision and recall scores**, making the predictions much more reliable and stable.

✨ Current Features:
 Detects whether the given data represents an exoplanet or not
 Predicts the exoplanet type after detection
 Interactive Streamlit web interface for real-time prediction

 Technologies Used:

* Python
* Scikit-learn
* Streamlit
* Random Forest Algorithm

 Dataset:
NASA Exoplanet Dataset containing parameters like:

* Mass
* Orbital Radius
* Eccentricity
* Detection Method
* Stellar Properties

🌲 Why Random Forest?
Random Forest was chosen because it performs very well on structured datasets, reduces overfitting, and improves prediction accuracy by combining multiple decision trees.

This project helped me gain practical experience in:

* Machine Learning
* Data preprocessing
* Model evaluation
* Feature engineering
* Deployment using Streamlit
* End-to-end ML workflow

Really happy to see the complete workflow working successfully from training to deployment.
