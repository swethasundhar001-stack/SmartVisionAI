# 📄 Intelligent Document AI

An AI-powered document processing system that extracts important information from PDF and image documents using OCR and Natural Language Processing techniques.

## 🚀 Features

- 📤 Upload PDF, PNG, JPG and JPEG documents
- 🔍 OCR-based text extraction using Tesseract
- 🖼️ Image preprocessing using OpenCV
- 📝 Automatic field extraction
- 👤 Name extraction
- 📧 Email extraction
- 📱 Phone number extraction
- 📅 Date extraction
- 💰 Amount extraction
- 📍 Address extraction
- 📄 Display extracted OCR text
- 📥 Download extracted data as JSON
- 🌐 Simple and user-friendly Streamlit interface
- 🧪 Automated testing using Pytest

## 🛠️ Technologies Used

- Python
- Streamlit
- Tesseract OCR
- OpenCV
- NumPy
- Pillow
- pdf2image
- Regular Expressions
- JSON
- Pytest

## 🔄 Processing Pipeline

```text
Upload Document
       ↓
Document Loader
       ↓
Image Preprocessing
       ↓
Tesseract OCR
       ↓
Text Extraction
       ↓
Field Extraction
       ↓
Structured JSON Data
       ↓
Streamlit UI

## ⚙️ How It Works

### 1. Upload Document

The user uploads a PDF or image document through the Streamlit interface.

### 2. Document Loading

PDF documents are converted into images using `pdf2image`.

JPG, JPEG and PNG files are loaded using Pillow.

### 3. Image Preprocessing

OpenCV is used to:

- Convert the image to grayscale
- Resize the image
- Prepare the image for OCR

### 4. OCR Processing

Tesseract OCR extracts text from the preprocessed image.

### 5. Field Extraction

Regular expressions are used to extract:

- Name
- Email
- Phone
- Date
- Amount
- Address

### 6. Structured Output

The extracted information is displayed in the Streamlit application.

### 7. JSON Download

The extracted fields can be downloaded as a JSON file.

## 🧪 Running Tests

Run all automated tests using:

```bash
python -m pytest tests