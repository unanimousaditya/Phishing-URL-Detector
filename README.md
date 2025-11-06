# 🔐 Phishing URL Detection

A machine learning-powered web application that detects phishing URLs using advanced feature extraction and gradient boosting classification. Built with Flask and featuring a modern, responsive dark-themed UI.

![Python](https://img.shields.io/badge/Python-3.13-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0.2-green.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.7.2-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- **Real-time URL Analysis**: Instantly analyze any URL for phishing indicators
- **Machine Learning Powered**: Uses Gradient Boosting Classifier trained on 11,000+ URLs
- **30+ Feature Extraction**: Analyzes URL structure, domain properties, page content, and more
- **Modern UI**: Dark-themed, responsive interface with smooth animations
- **High Accuracy**: Trained model with optimized hyperparameters for reliable detection
- **Visual Feedback**: Clear safety indicators with animated results

## 🎯 Demo

Enter any URL and get instant feedback:
- ✅ **Safe**: URL appears legitimate
- ⚠️ **Phishing**: URL shows suspicious characteristics

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/unanimousaditya/Phishing-URL-Detector.git
   cd Phishing-URL-Detector
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv .venv
   
   # Windows
   .venv\Scripts\activate
   
   # macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   ```
   http://127.0.0.1:5000
   ```

## 📊 How It Works

### Feature Extraction (30 Features)

The system analyzes multiple aspects of a URL:

#### 1. **URL-Based Features**
- URL length and complexity
- Number of special characters (@, -, _, etc.)
- Presence of IP address
- HTTPS usage
- Suspicious keywords

#### 2. **Domain-Based Features**
- Domain age and registration length
- DNS record analysis
- WHOIS information
- Domain rank (Google Page Rank)

#### 3. **Content-Based Features**
- Page title and meta information
- Number of external links
- Presence of forms (especially password/email fields)
- Iframe usage
- Redirect behavior

#### 4. **HTML/JavaScript Features**
- Right-click disabled
- Pop-up windows
- Hidden elements
- Suspicious scripts

### Machine Learning Model

- **Algorithm**: Gradient Boosting Classifier
- **Training Data**: 11,054 URLs (legitimate + phishing)
- **Features**: 30 extracted features per URL
- **Hyperparameters**:
  - max_depth: 4
  - learning_rate: 0.7
  - random_state: 42

The model is automatically trained on first run if not present, and saved as `pickle/model_new.pkl`.

## 🛠️ Technology Stack

- **Backend**: Flask 2.0.2
- **ML Library**: scikit-learn 1.7.2
- **Feature Extraction**: 
  - BeautifulSoup4 (HTML parsing)
  - python-whois (WHOIS lookups)
  - googlesearch-python (rank checking)
  - requests (HTTP requests)
- **Frontend**:
  - HTML5
  - CSS3 (Modern dark theme with animations)
  - JavaScript (Vanilla)
  - Font Awesome 6.0 (icons)
  - Google Fonts (Inter)

## 📁 Project Structure

```
Phishing-URL-Detector/
├── app.py                          # Flask application & ML model training
├── feature.py                      # Feature extraction logic
├── phishing.csv                    # Training dataset (11,054 URLs)
├── requirements.txt                # Python dependencies
├── Procfile                        # Deployment configuration
├── .gitignore                      # Git ignore rules
├── pickle/
│   └── model_new.pkl              # Trained ML model
├── static/
│   └── styles.css                 # Modern dark theme styling
├── templates/
│   └── index.html                 # Main webpage
└── Phishing URL Detection.ipynb   # Jupyter notebook (analysis)
```

## 🎨 UI Features

- **Modern Dark Theme**: Easy on the eyes with purple accent colors
- **Smooth Animations**: Fade-in effects and animated transitions
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Visual Feedback**: 
  - Animated shield icon
  - Color-coded results (green for safe, red for phishing)
  - Bounce/shake animations for results
- **Feature Showcase**: Highlights key capabilities
- **Clean Layout**: Card-based design with proper spacing

## 📈 Model Performance

The model is trained on a balanced dataset with:
- **Total Samples**: 11,054 URLs
- **Features**: 30 carefully engineered features
- **Model Type**: Gradient Boosting Classifier

To retrain the model, simply delete `pickle/model_new.pkl` and run the application. It will automatically retrain using `phishing.csv`.

## 🔧 Configuration

### Environment Variables

You can configure the Flask app using environment variables:

```bash
# Development mode (default)
export FLASK_ENV=development

# Production mode
export FLASK_ENV=production
```

### Model Retraining

To retrain with your own data:
1. Replace `phishing.csv` with your dataset (must have 30 features + class column)
2. Delete `pickle/model_new.pkl`
3. Run `python app.py`

## 🚢 Deployment

### Heroku Deployment

The project includes a `Procfile` for easy Heroku deployment:

```bash
# Login to Heroku
heroku login

# Create a new app
heroku create your-app-name

# Deploy
git push heroku main
```

### Docker Deployment

Create a `Dockerfile`:

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

Build and run:
```bash
docker build -t phishing-detector .
docker run -p 5000:5000 phishing-detector
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Aditya**
- GitHub: [@unanimousaditya](https://github.com/unanimousaditya)

## 🙏 Acknowledgments

- Dataset source: [Phishing URL Dataset](https://www.kaggle.com/datasets/taruntiwarihp/phishing-site-urls)
- Inspired by cybersecurity best practices
- Built with modern web technologies

## 📞 Support

If you have any questions or run into issues, please open an issue on GitHub.

---

⭐ **Star this repository** if you find it helpful!

🔗 **Live Demo**: [Add your deployment URL here]
