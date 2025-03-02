import streamlit as st

def main():
    st.set_page_config(page_title="AgroMate - AI Crop Disease Prediction", page_icon="🌱", layout="wide")
    if st.button("🏠 Go to Home"):
        st.switch_page("main.py")
    # Hide the sidebar by default
    st.markdown("""
        <style>
            [data-testid="stSidebar"] {
                display: none;
            }
            .big-title {
                font-size: 40px;
                font-weight: bold;
                text-align: center;
                color: #2E8B57;
                margin-bottom: 10px;
            }
            .sub-title {
                font-size: 20px;
                text-align: center;
                color: #555;
                margin-bottom: 30px;
            }
            .button-container {
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                gap: 15px;
            }
            .stButton>button {
                width: 220px;
                height: 50px;
                font-size: 16px;
                font-weight: bold;
                background-color: #2E8B57;
                color: white;
                border-radius: 10px;
                border: none;
            }
            .stButton>button:hover {
                background-color: #276749;
            }
        </style>
    """, unsafe_allow_html=True)

    # Display header
    st.markdown("<div class='big-title'>🌱 AI Crop Disease Prediction</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Select a crop to predict its diseases.</div>", unsafe_allow_html=True)

    # Create buttons in a responsive grid layout
    crop_pages = {
        "🍎 Apple": "pages/apple.py",
        "🍒 Cherry": "pages/cherry.py",
        "🌽 Corn": "pages/corn.py",
        "🍇 Grape": "pages/grape.py",
        "🍑 Peach": "pages/peach.py",
        "🌶️ Pepper": "pages/pepper.py",
        "🥔 Potato": "pages/potato.py",
        "🍓 Strawberry": "pages/strawberry.py",
        "🍅 Tomato": "pages/tomato.py"
    }

    # Display buttons in a neat grid
    st.markdown("<div class='button-container'>", unsafe_allow_html=True)
    cols = st.columns(5)

    for idx, (label, page) in enumerate(crop_pages.items()):
        with cols[idx % 5]:  # Distribute buttons across columns
            if st.button(label):
                st.switch_page(page)
    
    st.markdown("</div>", unsafe_allow_html=True)

    # Home button to refresh the app
    

if __name__ == "__main__":
    main()
