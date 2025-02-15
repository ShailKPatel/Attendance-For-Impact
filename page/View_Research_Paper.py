import streamlit as st
from streamlit_pdf_viewer import pdf_viewer 

# Logo
st.logo("resources\\logo.png", icon_image="resources\\logo.png",size='large')

pdf_viewer('resources\\Research Paper.pdf', width='133%')