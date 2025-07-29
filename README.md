# PDFCrafter Web Application

A modern web application for handling PDF operations including merging PDFs, splitting PDFs, converting images to PDF, and text to PDF conversion.

## Features

### 1. Merge PDFs
- Upload multiple PDF files
- Drag and drop to reorder files
- Preview file list before merging
- Download merged PDF

### 2. Split PDF
- Upload single PDF file
- Split into individual pages
- Download all pages as ZIP file
- Maintains original PDF quality

### 3. Images to PDF
- Upload multiple image files
- Supports common image formats (PNG, JPG, JPEG)
- Preview image list
- Convert to single PDF document

### 4. Text to PDF
- Input text directly
- Supports line breaks
- Convert to formatted PDF
- Automatic page breaks for long content

## Technical Stack

- **Backend**: FastAPI (Python)
- **Frontend**: HTML, CSS, JavaScript
- **PDF Processing**: PyPDF2, FPDF
- **Image Processing**: Pillow (PIL)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/pdfcrafter-webapp.git
    cd pdfcrafter-webapp
    ```

2. Create and activate virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Mac/Linux
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    uvicorn app.main:app --reload
    ```

## Project Structure

    ```
    pdfcrafter-webapp/
    ├── app/
    │   ├── static/
    │   │   ├── style.css    # Main stylesheet
    │   ├── templates/
    │   │   ├── index.html   # Main template
    │   ├── main.py          # FastAPI application
    │   └── pdf_utils.py     # PDF processing utilities
    ├── requirements.txt
    └── README.md
    ```

## API Endpoints

### 1. Merge PDFs
    ```
    POST /merge-pdfs/
    Content-Type: multipart/form-data
    Files: files[]
    ```

### 2. Split PDF
    ```
    POST /split-pdf/
    Content-Type: multipart/form-data
    File: file
    ```

### 3. Images to PDF
    ```
    POST /images-to-pdf/
    Content-Type: multipart/form-data
    Files: files[]
    ```

### 4. Text to PDF
    ```
    POST /text-to-pdf/
    Content-Type: multipart/form-data
    Data: text
    ```

## User Interface Features

### Navigation
- Sticky navigation bar
- Tool selection tabs
- Active state indicators
- Smooth transitions

### File Handling
- Drag and drop file uploads
- File list reordering
- Progress indicators
- Error handling

### Responsive Design
- Mobile-friendly layout
- Adaptive UI components
- Touch device support
- Flexible grid system

## Styling

### Theme Colors
- Primary: Linear gradient (#667eea to #764ba2)
- Background: #f8fafc
- Text: #2d3748, #4a5568
- Borders: #e2e8f0

### Components
- Cards with shadow effects
- Custom form elements
- Interactive buttons
- Custom file inputs

## Browser Support
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Development

### Running Tests
    ```bash
    pytest tests/
    ```

### Code Style
- Follow PEP 8 for Python code
- Use Black for code formatting
- ESLint for JavaScript

### Contributing
1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request

## License
MIT License

## Support
For issues and feature requests, please use the GitHub issue tracker.

## Roadmap
- [ ] Add PDF compression
- [ ] Implement PDF password protection
- [ ] Add PDF preview
- [ ] Support for more image formats
- [ ] Batch processing capabilities

## Acknowledgments
- FastAPI framework
- PyPDF2 library
- FPDF library
- Pillow library
