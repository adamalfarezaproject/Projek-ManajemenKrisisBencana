import streamlit as st

from chatbot.mesin_chatbot import MesinChatbot


def tambah_pesan(user_text, bot_text):

    st.session_state.chat_history.append(
        ("user", user_text)
    )

    st.session_state.chat_history.append(
        ("assistant", bot_text)
    )


def kirim_menu(pesan):

    jawaban = st.session_state.bot.proses_pesan(
        pesan
    )

    tambah_pesan(
        pesan,
        jawaban
    )

    st.rerun()


def tampilkan_chatbot():

    # ==================================
    # SESSION
    # ==================================

    if "bot" not in st.session_state:

        st.session_state.bot = MesinChatbot()

    if "chat_history" not in st.session_state:

        st.session_state.chat_history = []

    # ==================================
    # LAYOUT 3 KOLOM
    # ==================================

    menu_col, chat_col, guide_col = st.columns(
        [1.1, 4, 1.2]
    )

    # ==================================
    # MENU CEPAT
    # ==================================

    with menu_col:

        st.markdown(
            """
            <div class="chat-sidebar">
                <div class="sidebar-title">
                    Menu Cepat
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "Banjir",
            use_container_width=True
        ):
            kirim_menu("banjir")

        if st.button(
            "Gempa",
            use_container_width=True
        ):
            kirim_menu("gempa")

        if st.button(
            "Longsor",
            use_container_width=True
        ):
            kirim_menu("longsor")

        if st.button(
            "Kebakaran",
            use_container_width=True
        ):
            kirim_menu("kebakaran")

        if st.button(
            "Tsunami",
            use_container_width=True
        ):
            kirim_menu("tsunami")

        st.divider()

        if st.button(
            "Cek Status",
            use_container_width=True
        ):
            kirim_menu("status")

        if st.button(
            "Menu Utama",
            use_container_width=True
        ):
            kirim_menu("menu")

        if st.button(
            "Reset Chat",
            use_container_width=True
        ):


            st.session_state.bot.reset()

            st.session_state.chat_history = []

            st.rerun()

    # ==================================
    # PERCAKAPAN
    # ==================================

    with chat_col:

        st.markdown(
            """
            <div class="chat-main">
                <div class="chat-title">
                    Percakapan
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        # ==============================
        # WELCOME CARD
        # ==============================

        if not st.session_state.chat_history:

            st.markdown(
                """
                <div class="welcome-card">

                <h3>
                Selamat Datang di Disaster Management Assistant (DMA)
                </h3>

                <p>
                Layanan yang tersedia:
                </p>

                <ul>
                    <li>Banjir</li>
                    <li>Gempa</li>
                    <li>Longsor</li>
                    <li>Kebakaran</li>
                    <li>Tsunami</li>
                    <li>Cek Status Laporan</li>
                </ul>

                <p>
                Ketik nama bencana untuk memulai.
                </p>

                <p>
                Contoh:
                <br>
                banjir
                <br>
                gempa
                <br>
                status
                </p>

                </div>
                """,
                unsafe_allow_html=True
            )

        # ==============================
        # CHAT HISTORY
        # ==============================

        for role, pesan in st.session_state.chat_history:

            with st.chat_message(role):

                st.write(pesan)

        # ==============================
        # INPUT
        # ==============================

        user_input = st.chat_input(
            "Ketik pesan..."
        )

        if user_input:

            st.session_state.chat_history.append(
                ("user", user_input)
            )

            jawaban = (
                st.session_state.bot.proses_pesan(
                    user_input
                )
            )

            st.session_state.chat_history.append(
                ("assistant", jawaban)
            )

            st.rerun()

    # ==================================
    # PANDUAN
    # ==================================

    with guide_col:

        st.markdown("### Panduan")

        st.info("""
    1. Pilih bencana

    2. Pilih layanan

    3. Cek status laporan

    4. Kembali ke menu

    5. Reset chat
    """)
