# AgroMate: AI-Powered Farming Assistant 🌱

AgroMate is an AI-powered farming assistant designed to help farmers make data-driven decisions, detect crop diseases, and receive real-time agricultural advice. The project integrates **Computer Vision**, **Natural Language Processing (NLP)**, and **Data Analytics** to provide farmers with actionable insights for better crop management.

---

## Features ✨

1. **AI-Powered Disease Detection** 🖼️  
   - Detect **21 crop diseases** across **9 crops** using advanced **Convolutional Neural Networks (CNNs)**.  
   - Farmers can upload plant images for instant disease diagnosis and receive treatment suggestions.  

2. **Interactive Dashboard** 📊  
   - Real-time monitoring of weather data (temperature, humidity, wind speed, rainfall) and air quality indicators (PM2.5, PM10, CO, NO2, SO2, O3).  
   - Visual graphs, bar charts, and map integration for data-driven decision-making.  

3. **Multilingual AI Chatbot** 💬  
   - AI-powered chatbot built using **OpenAI’s GPT-3.5 Turbo** for prompt engineering and context-aware responses.  
   - Supports multiple languages, enabling farmers to ask questions about crop diseases, treatments, and best farming practices in their preferred language.  

4. **Image Predictor & Chat** 🤖  
   - Farmers can upload plant images for disease detection and chat with the AI for further guidance.  
   - Provides detailed explanations of diseases, treatment tips, and follow-up recommendations.  

---

## Technologies Used 🛠️

- **Deep Learning**:  
  - Built **Convolutional Neural Networks (CNNs)** using **TensorFlow/Keras** for disease detection.  
  - Applied **Batch Normalization**, **Max Pooling**, and **Dropout** for model optimization.  

- **Feature Engineering**:  
  - Extracted high-level image features from the second-to-last layer of the CNN model.  
  - Used **Decision Trees** for improved interpretability and efficiency.  

- **NLP & Chatbot Integration**:  
  - Integrated **OpenAI’s GPT-3.5 Turbo** for multilingual, context-aware chatbot responses.  
  - Applied **Prompt Engineering** to generate accurate and relevant answers for farmers.  

- **Data Visualization**:  
  - Used **Matplotlib** and **Plotly** for creating interactive graphs and charts.  
  - Integrated live weather and pollution data into the dashboard.  

---

## How It Works 🚀

1. **Disease Detection**:  
   - Farmers upload plant images to the system.  
   - The AI analyzes the image using trained CNN models and detects diseases with high accuracy.  
   - Provides treatment suggestions and precautions.  

2. **Interactive Dashboard**:  
   - Farmers can monitor real-time weather and pollution data.  
   - Visual graphs and maps help farmers make informed decisions to protect their crops.  

3. **AI Chatbot**:  
   - Farmers can ask questions about crop diseases, treatments, and farming practices.  
   - The chatbot provides instant, expert-backed responses in multiple languages.  

---

## Installation & Setup ⚙️

1. **Clone the Repository**:  
   ```bash
   git clone https://github.com/HareKrishna4747/AgroMate.git
   cd AgroMate
   ```

2. **Install Dependencies**:  
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:  
   ```bash
   python app.py
   ```

4. **Access the Dashboard**:  
   - Open your browser and navigate to `http://localhost:5000`.  

---

## Contributors 👥

- [HareKrishna4747](https://github.com/HareKrishna4747)  

---

## License 📜

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Contact 📧

For any queries or feedback, feel free to reach out:  
- **Email**: jayadityaarora2007@gmail.com 
- **GitHub**: [HareKrishna4747](https://github.com/HareKrishna4747)  

---
