from PIL import Image
import requests
import streamlit as st 
from streamlit_lottie import st_lottie


# ----- Page layout -----
st.set_page_config(page_title="My Webpage", page_icon=":gear:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None 
    return r.json()

# ----- Loading Assets -----
lottie_coding = load_lottieurl("https://lottie.host/bf9430f2-2a05-4039-8dd5-802e21c12a3e/8vVzBaFz9e.json")
img_contact_form = Image.open("images/oval_profile.png")

# ----- Header Section -----
with st.container():
    intro_column, profile_column = st.columns(2)
    with intro_column:
        st.title("Hello! Welcome to my website")
        st.subheader("My name is Tony Weng :wave:")

# ----- What I Do -----
with st.container():
    st.write("---")
    left_column, right_column = st.columns([1, 3])
    with right_column:
        st.header("A little bit about me,")
        st.write(
            """
            I currently study mechanical engineering at Virginia Tech with
            the hope of pursuing automotive and robotics development in the 
            future. I am a part of the Hokie Electric Vehicle Team at 
            Virginia Tech where we compete in the EcoCarEV competition. 
            In my free time, I like to play basketball (GO CAVS!), 
            golf, and lift weights. During my free time this summer, I have 
            been teaching myself python for future projects. 
            """
        )
        st.write("##")
        st.write("##")
        st.write(
            """
            Feel free to follow me:
             [Instagram](https://www.instagram.com/tonyweng0/),
             [LinkedIn](https://www.linkedin.com/in/tonyweng24/)
            """
        )
    with left_column:
        st.image(img_contact_form)

# ----- Projects -----
with st.container():
    st.write("---")
    st.header("Here are some of my projects,")
    st.write("##")
    text_column, desc_column, image_column= st.columns((2, 3, 1))
    with text_column: 
            st.subheader("FEM analysis of engine cradle:")
            
    with desc_column:
        st.write(
                """**January 2023 - May 2023** | _Blacksburg, VA_
                 <br> 
                 \t- Utilized Siemens NX to conduct finite element 
                 analysis of engine subframe to increase factor of 
                 safety and ensure success.
                 <br>
                 \t- Collaborated with the CAD design team to optimize 
                subframe parameters like: factor of safety, cost, size, 
                weight, etc.
                """, unsafe_allow_html=True
                )
        
    

# ----- Contact -----

# ----- Theme -----

# UPDATE IDEAS
# - making tabs on the webpage 