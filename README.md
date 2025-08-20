# Offer Letter Generator 📝

A professional Python application that automates the generation and distribution of personalized offer letters via email using Gmail API integration.

## 🌟 Features

- **Automated Letter Generation**: Create personalized offer letters from templates
- **Email Integration**: Send offer letters directly via Gmail API
- **Excel Data Processing**: Import candidate data from Excel spreadsheets
- **Document Templates**: Use customizable Word document templates
- **Batch Processing**: Generate multiple offer letters efficiently
- **Web Interface**: Clean and intuitive web-based UI

## 🛠️ Tech Stack

- **Backend**: Python 3.x
- **Frontend**: HTML5, CSS3, JavaScript
- **APIs**: Gmail API, Google OAuth 2.0
- **Libraries**: 
  - `openpyxl` - Excel file processing
  - `python-docx` - Word document manipulation
  - `google-api-python-client` - Gmail integration

## 📋 Prerequisites

- Python 3.7 or higher
- Google Cloud Console account with Gmail API enabled
- OAuth 2.0 credentials (credentials.json)

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/Mantsha-Ansari/offer-letter-generator.git
cd offer-letter-generator
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up Google API Credentials
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing one
3. Enable Gmail API
4. Create OAuth 2.0 credentials
5. Download credentials.json and place in project root

### 4. Prepare Your Data
- Update `CandidateData.xlsx` with candidate information
- Customize `offerLetter.docx` template as needed

### 5. Run the Application
```bash
python index.py
```
Then open `http://localhost:8000` in your browser

## 📊 Project Structure

```
offer-letter-generator/
├── index.py                 # Main Flask application
├── generate_offer_letter.py # Letter generation logic
├── gmail_service.py         # Gmail API integration
├── send_email.py           # Email sending functionality
├── index.html              # Web interface
├── style.css               # Styling
├── script.js               # Frontend JavaScript
├── CandidateData.xlsx      # Sample candidate data
├── offerLetter.docx        # Letter template
├── credentials.json        # Google API credentials (not in repo)
├── .gitignore             # Git ignore rules
├── requirements.txt       # Python dependencies
└── Generated_Offer_Letters/ # Output directory
    ├── Offer_Letter_Ariba.docx
    ├── Offer_Letter_Peter.docx
    └── Offer_Letter_saba.docx
```

## 🎯 Usage Guide

### Web Interface
1. Open the web application
2. Upload candidate Excel file or use existing data
3. Select candidates for offer letter generation
4. Preview generated letters
5. Send via email with one click

### Command Line
```bash
# Generate offer letter for specific candidate
python generate_offer_letter.py --candidate "John Doe"

# Send email to candidate
python send_email.py --to "candidate@email.com" --file "Offer_Letter_John.docx"
```

## 🔧 Configuration

### Excel Data Format
Your `CandidateData.xlsx` should have these columns:
- Name
- Email
- Position
- Salary
- Start Date
- Department

### Template Customization
Edit `offerLetter.docx` to customize:
- Company letterhead
- Terms and conditions
- Signature block
- Formatting and styling

## 🔐 Security Best Practices

- Never commit `credentials.json` to version control
- Use environment variables for sensitive data
- Regularly rotate API credentials
- Implement proper access controls

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

For support, email mantsha.ansari@example.com or create an issue in the GitHub repository.

## 🙏 Acknowledgments

- Google for Gmail API
- Python community for excellent libraries
- Contributors and testers

---

Made with ❤️ by Mantsha Ansari
