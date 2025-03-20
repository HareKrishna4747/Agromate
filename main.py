import streamlit as st

def main():
    st.set_page_config(page_title="AgroMate", page_icon="🌱", layout="wide")
    
    # Custom CSS for styling
    st.markdown("""
        <style>
            .big-title {
                font-size: 50px;
                font-weight: bold;
                text-align: center;
                color: #2E8B57;
            }
            .sub-title {
                font-size: 22px;
                text-align: center;
                color: #555;
                margin-bottom: 30px;
            }
            .centered {
                display: flex;
                justify-content: center;
                gap: 20px;
            }
            .button-container {
                text-align: center;
                margin-top: 30px;
            }
            .footer {
                text-align: center;
                padding: 20px;
                background-color: #f1f1f1;
                margin-top: 40px;
                border-radius: 10px;
            }
            [data-testid="stSidebar"] {
                display: none;
            }
            .logo-container {
                display: flex;
                justify-content: center;
                margin-bottom: 20px;
            }
        </style>
    """, unsafe_allow_html=True)
    
    # Logo at the top

    
    st.markdown("<div class='big-title'>Welcome to AgroMate 🌱</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Empowering Farmers with AI and Insights</div>", unsafe_allow_html=True)
    
    st.write("### Choose an Option:")
    
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
    
    # Additional Content
    st.markdown("""
    ## About AgroMate
    AgroMate is an AI-powered platform designed to assist farmers in making informed decisions.
    With features like disease prediction, real-time analytics, and expert advice, AgroMate 
    aims to revolutionize the way farming is done.
    """)
    
    # Logo in the middle

    
    st.markdown("""
    ## Why Choose AgroMate?
    - **🌿 AI-Powered Insights**: Get accurate predictions and recommendations.
    - **📱 User-Friendly Interface**: Easy to use, even for non-tech-savvy users.
    - **🧑‍🌾 Expert Support**: Chat with farm experts for personalized advice.
    """)
    
    # Footer
    st.markdown("""
        <div style="text-align: center; padding: 10px; font-size: 14px; color: gray;">
            🌾 Grow Smarter with AgroMate | Powered by AI <br>
            Created by Jayaditya Harish Arora
        </div>
    """, unsafe_allow_html=True)
if __name__ == "__main__":
    main()