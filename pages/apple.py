import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
from langchain_openai import ChatOpenAI

# Set Streamlit Page Configuration
st.set_page_config("AgroMate - AI Plant Disease Predictor", page_icon=":seedling:")
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)

# Shortcut Button to Homepage
if st.button("🌿🔍 Predict Other"):
    st.switch_page("pages/predict.py")  
st.title("🌱 AgroMate - AI Plant Disease Chatbot")
st.write("Upload an image of an apple leaf to detect disease and chat about treatment suggestions.")

# Load AI Model
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("apple.h5")

model = load_model()

# Define Classes
classes = [
    "Apple Scab",
    "Black Rot",
    "Cedar Apple Rust",
    "Healthy"
]

# OpenAI Integration
llm = ChatOpenAI(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    model="gpt-3.5-turbo"
)

def query_chatgpt(label, user_input=None):
    if user_input:
        prompt = f"{user_input} (Context: Detected {label} in an apple plant)"
    else:
        prompt = f"I detected {label} in an apple plant. What are the treatments and precautions?"
    
    response = llm.invoke(prompt)  # ✅ Pass prompt as a string
    return response.content
# Image Upload
uploaded_file = st.file_uploader("Upload a leaf image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Preprocess Image
    image = image.resize((256, 256))
    image_array = np.array(image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)
    
    # Predict Disease
    predictions = model.predict(image_array)
    label_index = np.argmax(predictions)
    label = classes[label_index]
    
    st.success(f"Prediction: {label}")
    
    # Query ChatGPT for Initial Treatment Info
    with st.spinner("Fetching treatment suggestions..."):
        treatment_info = query_chatgpt(label)
    
    st.subheader("🩺 Treatment & Precautions")
    st.write(treatment_info)
    
    # Chatbot Interface
    st.subheader("💬 Chat about the Diagnosis")
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            {"role": "assistant", "content": treatment_info}
        ]
    
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
    
    user_input = st.chat_input("Ask about the diagnosis...")
    if user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        response = query_chatgpt(label, user_input)
        st.session_state.chat_history.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(response)
