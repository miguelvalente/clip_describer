import streamlit as st
from clip_describer.core.text_generator import generate_description

# region SetUp Page
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.set_page_config(
    page_title="Keywords Generator",
    page_icon="🔑",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


st.title('Text Keyword Generator')

uploaded_file = st.file_uploader("Upload an image...", type="jpg")

if uploaded_file is not None:
    # Create two columns
    col1, col2 = st.columns(2)

    # Left column: display uploaded image
    with col1:
        st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)

    # Right column: display spinner while classifying and then display results
    with col2:
        with st.spinner('Generating Keywords...'):
            # Call your function while the spinner is displayed
            generated_text = generate_description(uploaded_file)
        
        # After the function completes, the spinner will be removed
        # Now, display the results in a text area
        st.text_area("Generated Keywords", value=generated_text, height=200)
