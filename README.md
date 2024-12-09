# AI Blog Writing Companion

## Overview
The **AI Blog Writing Companion** is a user-friendly Streamlit application designed to assist writers in crafting engaging, comprehensive, and informative blog posts. By leveraging the capabilities of Google's Gemini-1.5-Flash generative AI model, this app generates high-quality content tailored to the user's input, making blog writing efficient and enjoyable.

## Features
- Generate blog posts based on the provided title, keywords, and desired word count.
- Customize the length of the blog to suit your needs.
- Intuitive and interactive interface powered by Streamlit.
- AI-generated content that maintains consistency and engages the target audience.

---

- **Streamlit**: For creating a user-friendly and responsive interface.
- **Google Generative AI (Gemini-1.5-Flash)**: For generating blog content based on user input.
- **Python**: As the primary programming language.
- **Google Generative AI API**: For communicating with Google's AI model.

## Setup and Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/ai-blog-companion.git
   cd ai-blog-companion
   ```

2. **Set up API Keys**:
   To securely handle API keys:
   - Create a `.env` file in the project root directory.
   - Add your API key to the `.env` file:
     ```
     GOOGLE_GEMINI_API_KEY=your_google_gemini_api_key
     ```

4. **Run the application**:
   Launch the Streamlit app using:
   ```bash
   streamlit run app.py
   ```

## Usage
1. Open the application in your browser (default URL: `http://localhost:8501`).
2. Enter the blog title and keywords in the sidebar.
3. Adjust the slider to set the desired word count for the blog.
4. Click the "Generate Blog" button to create your blog post.
5. Review and copy the generated content displayed in the app.
