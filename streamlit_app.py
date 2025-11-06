import streamlit as st
import pickle
import pandas as pd
import os
from feature import FeatureExtraction

# Page configuration
st.set_page_config(
    page_title="Phishing URL Detector",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern dark theme
st.markdown("""
<style>
    /* Main background */
    .main {
        background: linear-gradient(135deg, #1e1e2e 0%, #2d2d44 100%);
    }
    
    /* Header styling */
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
    }
    
    .main-header h1 {
        color: white;
        font-size: 3rem;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .main-header p {
        color: rgba(255,255,255,0.9);
        font-size: 1.2rem;
        margin-top: 0.5rem;
    }
    
    /* Button styling */
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 0.75rem 2rem;
        border: none;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
    }
    
    /* Input field styling */
    .stTextInput>div>div>input {
        background-color: rgba(255, 255, 255, 0.05);
        color: white;
        border: 2px solid rgba(102, 126, 234, 0.3);
        border-radius: 10px;
        padding: 0.75rem;
        font-size: 1rem;
    }
    
    .stTextInput>div>div>input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 2px rgba(102, 126, 234, 0.2);
    }
    
    /* Result cards */
    .result-card {
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem 0;
        text-align: center;
        animation: fadeIn 0.5s ease-in;
    }
    
    .safe-card {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        box-shadow: 0 10px 30px rgba(56, 239, 125, 0.3);
    }
    
    .danger-card {
        background: linear-gradient(135deg, #eb3349 0%, #f45c43 100%);
        box-shadow: 0 10px 30px rgba(235, 51, 73, 0.3);
    }
    
    /* Feature cards */
    .feature-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 1.5rem;
        border-radius: 10px;
        border: 1px solid rgba(102, 126, 234, 0.2);
        margin: 1rem 0;
        transition: all 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        border-color: #667eea;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.2);
    }
    
    /* Metric styling */
    .stMetric {
        background: rgba(255, 255, 255, 0.05);
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid rgba(102, 126, 234, 0.2);
    }
    
    /* Animation */
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #1e1e2e 0%, #2d2d44 100%);
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background: rgba(102, 126, 234, 0.1);
        border-radius: 10px;
        color: white;
        font-weight: bold;
    }
    
    /* Success/Error message styling */
    .stSuccess, .stError {
        border-radius: 10px;
        padding: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Load or train model
@st.cache_resource
def load_model():
    """Load the trained model or train a new one if not found"""
    model_path = "pickle/model_new.pkl"
    
    if not os.path.exists(model_path):
        st.info("🔄 Training model for the first time... This may take a minute.")
        
        # Train the model
        from sklearn.ensemble import GradientBoostingClassifier
        import pandas as pd
        
        try:
            data = pd.read_csv("phishing.csv")
            X = data.drop(["Index", "class"], axis=1)
            y = data["class"]
            
            gbc = GradientBoostingClassifier(max_depth=4, learning_rate=0.7, random_state=42)
            gbc.fit(X, y)
            
            # Save the model
            os.makedirs("pickle", exist_ok=True)
            with open(model_path, "wb") as file:
                pickle.dump(gbc, file)
            
            st.success("✅ Model trained successfully!")
            return gbc
        except Exception as e:
            st.error(f"❌ Error training model: {str(e)}")
            return None
    else:
        try:
            with open(model_path, "rb") as file:
                return pickle.load(file)
        except Exception as e:
            st.error(f"❌ Error loading model: {str(e)}")
            return None

# Load the model
gbc = load_model()

# Header
st.markdown("""
<div class="main-header">
    <h1>🔐 Phishing URL Detector</h1>
    <p>Protect yourself from malicious websites using AI-powered detection</p>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("### 📊 About")
    st.markdown("""
    This application uses **Machine Learning** to detect phishing URLs in real-time.
    
    **Features:**
    - 🤖 AI-Powered Detection
    - ⚡ Real-time Analysis
    - 🎯 30+ Feature Extraction
    - 📈 High Accuracy Model
    
    **Model Details:**
    - Algorithm: Gradient Boosting
    - Training Data: 11,054 URLs
    - Features: 30 engineered features
    """)
    
    st.markdown("---")
    st.markdown("### 🛡️ How It Works")
    st.markdown("""
    1. **Enter URL**: Paste any website URL
    2. **Extract Features**: 30+ characteristics analyzed
    3. **AI Prediction**: ML model classifies the URL
    4. **Get Results**: Instant safety verdict
    """)
    
    st.markdown("---")
    st.markdown("### 👨‍💻 Developer")
    st.markdown("""
    **Aditya**
    
    [GitHub Repository](https://github.com/unanimousaditya/Phishing-URL-Detector)
    """)

# Main content
st.markdown("### 🔍 URL Analysis")

# Create two columns for input and button
col1, col2 = st.columns([4, 1])

with col1:
    url = st.text_input(
        "Enter URL to check:",
        placeholder="https://example.com",
        label_visibility="collapsed",
        help="Enter the complete URL including http:// or https://"
    )

with col2:
    analyze_button = st.button("🔍 Analyze", use_container_width=True)

# Analyze button logic
if analyze_button:
    if url:
        if not url.startswith(('http://', 'https://')):
            st.warning("⚠️ Please include http:// or https:// in the URL")
        else:
            with st.spinner("🔄 Analyzing URL... This may take a few seconds."):
                try:
                    # Extract features
                    obj = FeatureExtraction(url)
                    x = obj.getFeaturesList()
                    
                    # Predict
                    if gbc is not None:
                        y_pred = gbc.predict([x])[0]
                        y_pro_phishing = gbc.predict_proba([x])[0, 0]
                        y_pro_non_phishing = gbc.predict_proba([x])[0, 1]
                        
                        # Display results
                        st.markdown("---")
                        st.markdown("### 📋 Analysis Results")
                        
                        # Create result card
                        if y_pred == 1:
                            st.markdown("""
                            <div class="result-card safe-card">
                                <h2>✅ SAFE URL</h2>
                                <p style="font-size: 1.2rem; color: white;">This URL appears to be legitimate and safe to visit.</p>
                            </div>
                            """, unsafe_allow_html=True)
                            
                            # Metrics
                            col1, col2, col3 = st.columns(3)
                            with col1:
                                st.metric("Verdict", "SAFE", delta="✓ Legitimate")
                            with col2:
                                st.metric("Safety Score", f"{y_pro_non_phishing*100:.1f}%", delta=f"+{y_pro_non_phishing*100:.1f}%")
                            with col3:
                                st.metric("Risk Level", "LOW", delta="✓ Safe")
                        else:
                            st.markdown("""
                            <div class="result-card danger-card">
                                <h2>⚠️ PHISHING DETECTED</h2>
                                <p style="font-size: 1.2rem; color: white;">Warning! This URL shows suspicious characteristics.</p>
                            </div>
                            """, unsafe_allow_html=True)
                            
                            # Metrics
                            col1, col2, col3 = st.columns(3)
                            with col1:
                                st.metric("Verdict", "DANGER", delta="✗ Phishing", delta_color="inverse")
                            with col2:
                                st.metric("Risk Score", f"{y_pro_phishing*100:.1f}%", delta=f"-{y_pro_phishing*100:.1f}%", delta_color="inverse")
                            with col3:
                                st.metric("Risk Level", "HIGH", delta="✗ Unsafe", delta_color="inverse")
                            
                            st.error("🚨 **Do not proceed** - This URL may steal your personal information!")
                        
                        # Show confidence levels
                        st.markdown("### 📊 Confidence Levels")
                        col1, col2 = st.columns(2)
                        
                        with col1:
                            st.progress(y_pro_non_phishing, text=f"Legitimate: {y_pro_non_phishing*100:.2f}%")
                        with col2:
                            st.progress(y_pro_phishing, text=f"Phishing: {y_pro_phishing*100:.2f}%")
                        
                        # Show detailed features
                        with st.expander("📊 View Detailed Feature Analysis"):
                            st.markdown("#### Extracted Features")
                            st.info("These are the 30 features extracted from the URL and analyzed by the ML model.")
                            
                            # Create DataFrame with feature names
                            feature_names = [
                                "UsingIP", "LongURL", "ShortURL", "Symbol@", "Redirecting//",
                                "PrefixSuffix-", "SubDomains", "HTTPS", "DomainRegLen", "Favicon",
                                "NonStdPort", "HTTPSDomainURL", "RequestURL", "AnchorURL", "LinksInScriptTags",
                                "ServerFormHandler", "InfoEmail", "AbnormalURL", "WebsiteForwarding", "StatusBarCust",
                                "DisableRightClick", "UsingPopupWindow", "IframeRedirection", "AgeofDomain", "DNSRecording",
                                "WebsiteTraffic", "PageRank", "GoogleIndex", "LinksPointingToPage", "StatsReport"
                            ]
                            
                            features_df = pd.DataFrame([x], columns=feature_names)
                            
                            # Transpose for better view
                            features_display = features_df.T
                            features_display.columns = ['Value']
                            
                            # Color code the values
                            def color_code(val):
                                if val == 1:
                                    return 'background-color: #38ef7d; color: black'
                                elif val == -1:
                                    return 'background-color: #f45c43; color: white'
                                else:
                                    return 'background-color: #ffa500; color: black'
                            
                            styled_df = features_display.style.applymap(color_code)
                            st.dataframe(styled_df, use_container_width=True, height=400)
                            
                            st.markdown("""
                            **Legend:**
                            - 🟢 Green (1): Safe/Legitimate characteristic
                            - 🟠 Orange (0): Neutral/Suspicious characteristic
                            - 🔴 Red (-1): Dangerous/Phishing characteristic
                            """)
                    else:
                        st.error("❌ Model not loaded. Please refresh the page.")
                        
                except Exception as e:
                    st.error(f"❌ Error analyzing URL: {str(e)}")
                    st.error("This might happen if the URL is unreachable or invalid.")
    else:
        st.warning("⚠️ Please enter a URL to analyze")

# Features showcase
st.markdown("---")
st.markdown("### ✨ Key Features")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3>🤖 AI-Powered</h3>
        <p>Advanced machine learning algorithms detect phishing patterns with high accuracy</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3>⚡ Real-time</h3>
        <p>Instant analysis of any URL with immediate safety verdicts</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <h3>🎯 Accurate</h3>
        <p>Trained on 11,000+ URLs for reliable phishing detection</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="feature-card">
        <h3>🔍 Detailed</h3>
        <p>30+ features analyzed including URL structure, domain info, and content</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: rgba(255,255,255,0.6); padding: 2rem 0;">
    <p>Made with ❤️ by Aditya | Powered by Machine Learning</p>
    <p>⭐ <a href="https://github.com/unanimousaditya/Phishing-URL-Detector" target="_blank" style="color: #667eea; text-decoration: none;">Star on GitHub</a></p>
</div>
""", unsafe_allow_html=True)
