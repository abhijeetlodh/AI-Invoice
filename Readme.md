# AI Invoice Project

Welcome to the **AI Invoice Project**! This project extracts data from PDF files and leverages Google Generative AI for analysis.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)

## Installation

To set up the project, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/abhijeetlodh/AI-Invoice.git
   cd AI-Invoice

2. **Install the required packages:**:
    ```bash
    pip install -r requirements.txt

3. **Create a Conda environment:**:
    ```bash
    conda create --name venv python=3.12

4. **Activate the Conda environment:**:
    ```bash
     conda activate venv/

5. **Set up environment variables: Create a .env file in the root directory and add your environment variables, for example:**:
    ```bash
    GOOGLE_API_KEY=your_api_key_here
    
6. **Usage:**:
    ```bash
    python streamlit run solve.py