import streamlit as st
import os
import google.generativeai as genai
from config import google_gemini_api

genai.configure(api_key=google_gemini_api)

# Create the model
generation_config = {
  "temperature": 1.2,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

# set app to wide mode
st.set_page_config(layout='wide')

# title of app
st.title('AI writing companion')

# create a subheader
st.subheader("Now we can craft perfect blogs with the help of this AI Blog Companion")

# create a sidebar for user input
with st.sidebar:
    st.title('Input your blog details')
    st.subheader('Enter details of the blog you want to generate')

    # Blog titile
    blog_title = st.text_input('Blog title')

    # keywords input
    keywords = st.text_area('Keywords (comma-seperated)')

    # number of words in blog
    num_words = st.slider('Number of words in blog', min_value=250, max_value=1500, step=250)

    # number of images in blog
    # num_images = st.slider('Number of images in blog', min_value=1, max_value=5, step=1)

    # prompt given to model
    prompt = f"generate a comprehensive, engaging blog post relevant to the given title {blog_title} and focus on keywords like {keywords}. the blog should be around {num_words} words long, suitable for general audience. ensure the content is informative and maintain a consistent tone throughout."

    # submit button
    submit_button = st.button('Generate blog')

if submit_button:

    st.title('Your blog\'s context is here')

    response = model.generate_content(prompt)
    st.write(response.text)