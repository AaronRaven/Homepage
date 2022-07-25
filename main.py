# ---- THE LIBRARIES----
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import requests
from PIL import Image

# ---- PAGE CONFIGURATIONS----
st.set_page_config(page_title="Nordic stuff", page_icon=":euro:", layout="wide")


# ---- FUNCTION TO LOAD A LOTTIE ----
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")
# ---- ADDITIONAL ASSET ----
black_knight = Image.open("images/knight.png")
lottie = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_buopyjyz.json")

# ---- LIBRARIES FOR FUN AND META ----
import pandas as pd
import numpy as np
import altair as alt

# ---- SIDEBAR ----
selected = option_menu(
    menu_title="Epic Navigation bar",  # required
    options=["Home", "Our Python Calculator", "The Crypto tool"],  # required
    icons=["house", "calculator", "currency-bitcoin"],  # optional
    menu_icon="controller",  # optional
    default_index=1,  # optional
    orientation="horizontal",
)

if selected == "Home":
    st.title("'Tis the HOME")
if selected == "Our Python Calculator":
    st.title("placeholder")
if selected == "The Crypto tool":
    st.title("pages/project.py")

# ---- BASSICALLY THE BODY----
# ---- Specifically the intro about the start up----
with st.container():
    st.subheader("NordCrytoStuff :wave:")
    st.title("A totaly Nordic platform for all things crypto")
    st.write(
        "A totaly nordic i.e. not Baltic (LAMEEEE)company for all your crypto needs."
    )

# ---- Moar about the company----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What we offer")
        st.write("**")
        st.write("""While we are produly NORDIC company
        we use sadly Dutch programming Language Python in giving you all 
        the necessery tools to succed in crypto and stock trade
        bellow is a list of our main tools to help you succed in crypto/stock world
        """)
    with right_column:
        st.image(black_knight, caption=' \'Tiss but a scratch!')

# ---- What the start up offers----
with st.container():
    st.write("---")
    lottie_column, data_column = st.columns((1, 2))
    with lottie_column:
        st_lottie(lottie, height=300, key="Python!")
    with data_column:
        st.write(pd.DataFrame({

            'first column': [1, 2, 3, 4, 5, 6],
            'second column': ["Tkinter Calculator", "Kivy TicTacToe", "Small Flask Login", "Small Streamlit website",
                              "Small Tkinter Opener", "Small f Guesser"],
        }))

# ---- CONTACT FORM----
with st.container():
    st.write("---")
    st.header("Contact us for gifts")
    st.write("**")

contact_form = """
<form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Thine name" required>
    <input type="email" name="email" placeholder="Thine email" required>
    <textarea name="message" placeholder="Thine message here" required></textarea>
    <button type="submit">Send</button>
</form>
"""
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()
# ---- FOOTER----
st.caption(" All rights reserved... Siaip nervuoja kai LT komapnijos vadinasi NORDIC :(")
