# Chat Behavior Analysis

## Overview
Chat Behavior Analysis is a sentiment and threat detection system that analyzes chat messages in English, Gujarati, and Hindi. The system categorizes messages into **friendly, neutral, and non-friendly** types and triggers a **three-level notification threat system** based on detected behavior.

## Features
- **Multi-language Support:** Works with English, Gujarati, and Hindi.
- **Sentiment Analysis:** Detects and classifies messages as friendly, neutral, or non-friendly.
- **Threat Level Detection:** Implements a three-tier threat notification system:
  - **Low:** Minor negativity detected.
  - **Medium:** Potential harmful intent detected.
  - **High:** Strongly harmful or threatening content detected.
- **Real-time Notifications:** Alerts users based on threat levels.
- **Integration Ready:** Can be deployed as a Chrome extension and Flask-based web server.
- **Scalable:** Can be extended to social media platforms, messaging apps, and enterprise communication systems.

## Installation
### Prerequisites
- Python 3.8+
- Flask
- scikit-learn
- pandas
- nltk
- Google Translate API (for multilingual processing)

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/sonid617/Chat-Behaviour-Analysis.git
   cd chat-behavior-analysis
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Start the Flask server:
   ```sh
   python nlp_analyze.py
   ```
4. Deploy the Chrome extension (optional):
   - Load the extension in Developer mode from `chrome-extension` folder.

## Usage
- **Web Interface:**
  - Upload chat logs or input messages manually.
  - Get sentiment analysis and threat level classification.
- **API Endpoints:**
  - `POST /analyze` - Accepts chat text and returns sentiment classification.
  - `GET /threat_level` - Returns the latest detected threat level.
- **Chrome Extension:**
  - Scans and categorizes chat messages in real-time.
  - Displays threat level alerts within the browser.

## Model Details
- Uses **TF-IDF vectorization** for feature extraction.
- Employs **ML-based classifiers** like Random Forest and Isolation Forest.
- Implements **NLP techniques** for sentiment and behavior analysis.

## Future Enhancements
- **Deep Learning Integration** for improved accuracy.
- **Contextual Analysis** to detect evolving chat patterns.
- **Cross-Platform Support** for WhatsApp, Telegram, Discord, etc.
- **Better Threat Response Mechanisms** including automated reports to concerned authorities.

## Contributing
Contributions are welcome! Feel free to fork this repository and submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
- **Developer:** Dishank Soni
- **Email:** Dishanksoni627@gmail.com
