import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# -------------------------------
# Streamlit App Title
# -------------------------------
st.title("🩺 Heart Disease Data Visualization")
st.subheader("Histogram of Age vs Mortality")

# -------------------------------
# Upload Dataset
# -------------------------------
uploaded_file = st.file_uploader("Upload your CSV dataset", type=["csv"])

if uploaded_file is not None:
    # Load the dataset
    data = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")

    # Show data preview
    st.write("### 📋 Data Preview:")
    st.dataframe(data.head())

    # Check if required columns exist
    if 'Age' in data.columns and 'Mortality' in data.columns:
        st.write("### 📊 Histogram of Age by Mortality")

        # Create the histogram
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.histplot(
            data=data,
            x='Age',
            hue='Mortality',
            bins=20,
            kde=True,
            palette='Set2',
            edgecolor='black',
            ax=ax
        )

        ax.set_title('Age Distribution by Mortality Status', fontsize=14)
        ax.set_xlabel('Age', fontsize=12)
        ax.set_ylabel('Count', fontsize=12)
        ax.grid(alpha=0.3)
        st.pyplot(fig)

        # Optionally, add some insights
        avg_age = data['Age'].mean()
        st.info(f"ℹ️ Average age in dataset: *{avg_age:.1f} years*")
    else:
        st.error("❌ Columns 'Age' and 'Mortality' not found in the uploaded dataset.")
else:
    st.warning("👆 Please upload your dataset (CSV file) to view the histogram.")