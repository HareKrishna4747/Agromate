import streamlit as st

def main():
    st.set_page_config(page_title="AgroMate", page_icon="🌱", layout="wide")
    
    # Landing Page Design
    st.markdown("""
        <style>
            .big-title {
                font-size: 40px;
                font-weight: bold;
                text-align: center;
                color: #2E8B57;
            }
            .sub-title {
                font-size: 20px;
                text-align: center;
                color: #555;
            }
            .centered {
                display: flex;
                justify-content: center;
                gap: 20px;
            }
            .button-container {
                text-align: center;
            }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<div class='big-title'>Welcome to AgroMate 🌱</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Empowering Farmers with AI and Insights</div>", unsafe_allow_html=True)
    
    st.write("""
    ### Choose an Option:
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📊 Dashboard"):
            st.switch_page("pages/dashboard.py")
    
    with col2:
        if st.button("📷 Predict Diseases with Pics"):
            st.switch_page("pages/predict.py")
    
    with col3:
        if st.button("💬 Chat with Farm Expert"):
            st.switch_page("pages/bot.py")
    
if __name__ == "__main__":
    main()