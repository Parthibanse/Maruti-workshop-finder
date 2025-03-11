import streamlit as st
import pandas as pd

# Load the dataset
df = pd.read_excel("Workshop_Dashboard.xlsx", sheet_name="Dashboard")

# Streamlit UI
def main():
    st.title("Sheet1")
    
    # Search by Pincode
    pincode = st.text_input("Enter Pincode:")
    
    # Filters
    channel = st.selectbox("Select Channel:", ["All", "Arena", "Nexa"])
    body shop = st.selectbox("body shop:", ["All"] + sorted(df["body shop"].unique()))
    state = st.selectbox("Select State:", ["All"] + sorted(df["State"].unique()))
    
    # Filter data based on inputs
    filtered_df = df.copy()
    if Pincode:
        filtered_df = filtered_df[filtered_df["PIN CODE"].astype(str).str.startswith(pincode[:3])]
    if channel != "All":
        filtered_df = filtered_df[filtered_df["Channel"] == channel]
    if body shop != "All":
        filtered_df = filtered_df[filtered_df["body shop"].str.strip() == body shop]
    if State != "All":
        filtered_df = filtered_df[filtered_df["State"] == State]
    
    # Display filtered data
    st.write("### Filtered Workshops", filtered_df)

if __name__ == "__main__":
    main()