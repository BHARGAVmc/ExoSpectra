import streamlit as st
import pandas as pd
import joblib


model = joblib.load('./models/exo_model.pkl')
scaler = joblib.load('./models/scaler.pkl')
feature_columns = joblib.load('./models/feature_columns.pkl')


st.set_page_config(
    page_title="ExoSpectra",
    page_icon="🌌",
    layout="wide"
)


st.title("🌌 ExoSpectra")
st.caption("AI Powered Exoplanet Detection System")


col1, col2, col3, col4 = st.columns(4)

with col1:
    distance = st.number_input("Distance", value=304.0)

with col2:
    mass_multiplier = st.number_input("Mass", value=19.4)

with col3:
    orbital_radius = st.number_input("Orbit Radius", value=1.29)

with col4:
    eccentricity = st.number_input("Eccentricity", value=0.23)


col5, col6, col7 = st.columns(3)

with col5:
    mass_wrt = st.selectbox(
        "Mass WRT",
        ["Jupiter", "Earth", "Neptune"]
    )

with col6:
    radius_wrt = st.selectbox(
        "Radius WRT",
        ["Jupiter", "Earth", "Neptune"]
    )

with col7:
    detection_method = st.selectbox(
        "Detection",
        ["Radial Velocity", "Transit"]
    )


if st.button("Predict"):

    input_data = pd.DataFrame({
        'distance': [distance],
        'stellar_magnitude': [4.72],
        'discovery_year': [2007],
        'mass_multiplier': [mass_multiplier],
        'mass_wrt': [mass_wrt],
        'radius_multiplier': [1.08],
        'radius_wrt': [radius_wrt],
        'orbital_radius': [orbital_radius],
        'orbital_period': [0.89],
        'eccentricity': [eccentricity],
        'detection_method': [detection_method]
    })

  
    input_data = pd.get_dummies(input_data)

    
    input_data = input_data.reindex(
        columns=feature_columns,
        fill_value=0
    )

 
    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)


    planet_types = {
        0: "Gas Giant",
        1: "Neptune-like",
        2: "Super Earth",
        3: "Terrestrial"
    }

    
    if mass_multiplier > 1:

        result = planet_types[prediction[0]]

        st.success(
            f"Exoplanet Detected\n\n Exoplanet Type: {result}"
        )

    else:
        st.error("Not an Exoplanet")


st.caption(
    "Built using Random Forest and NASA Exoplanet Dataset"
)
