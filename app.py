import streamlit as st
from streamlit_option_menu import option_menu

from halaman.beranda import tampilkan_beranda
from halaman.chatbot import tampilkan_chatbot
from halaman.kuis import tampilkan_kuis
from halaman.tentang import tampilkan_tentang

from utils.style_loader import load_css


# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="DMA - Disaster Management Assistant",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==================================================
# LOAD CSS
# ==================================================

load_css()

# ==================================================
# SESSION MENU
# ==================================================

if "menu" not in st.session_state:

    st.session_state.menu = "Home"

# ==================================================
# NAVBAR
# ==================================================

selected = option_menu(

    menu_title=None,

    options=[
        "Home",
        "Chatbot",
        "Kuis",
        "Tentang Sistem"
    ],

    icons=[
        "house",
        "chat-dots",
        "clipboard-check",
        "info-circle"
    ],

    menu_icon="cast",


    default_index=[
        "Home",
        "Chatbot",
        "Kuis",
        "Tentang Sistem"
    ].index(st.session_state.menu),

    orientation="horizontal",

    styles={

        "container": {
            "padding": "0.5rem 1rem",
            "background-color": "#08111F",
            "border-radius": "18px",
            "border": "1px solid #132235"
        },

        "icon": {
            "color": "#10B981",
            "font-size": "18px"
        },

        "nav-link": {
            "font-size": "15px",
            "font-weight": "600",
            "text-align": "center",
            "color": "#94A3B8",
            "--hover-color": "#0F172A"
        },

        "nav-link-selected": {
            "background-color": "#10B981",
            "color": "#FFFFFF"
        }
    }
)

st.session_state.menu = selected

# ==================================================
# ROUTING
# ==================================================

if selected == "Home":

    tampilkan_beranda()

elif selected == "Chatbot":

    tampilkan_chatbot()

elif selected == "Kuis":

    tampilkan_kuis()

elif selected == "Tentang Sistem":

    tampilkan_tentang()