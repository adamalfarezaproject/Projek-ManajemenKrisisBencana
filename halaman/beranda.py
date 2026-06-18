import streamlit as st


def tampilkan_beranda():

    # =====================================
    # HERO
    # =====================================

    kiri, kanan = st.columns([1, 1])

    with kiri:

        st.markdown("""
        <div class="dma-badge">
        DISASTER MANAGEMENT ASSISTANT
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <h1 class="dma-title">
        SIAP SIAGA.<br>
        BANTU CEPAT.<br>
        <span>SELAMAT</span> BERSAMA.
        </h1>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="dma-desc">

        Sistem informasi bencana berbasis
        Finite State Machine (FSM)
        untuk edukasi, bantuan darurat,
        pelaporan kejadian,
        dan pemantauan laporan secara real-time.

        </div>
        """, unsafe_allow_html=True)

        tombol1, tombol2, kosong = st.columns([1,1,2])

        with tombol1:

            st.button(
                "Mulai Sekarang",
                use_container_width=True
            )

        with tombol2:

            st.button(
                "Pelajari Sistem",
                use_container_width=True
            )

        st.markdown("<br>", unsafe_allow_html=True)

        s1, s2, s3, s4 = st.columns(4)

        with s1:
            st.markdown("""
            <div class="stat-box">
            <h3>24/7</h3>
            <p>Siaga</p>
            </div>
            """, unsafe_allow_html=True)

        with s2:
            st.markdown("""
            <div class="stat-box">
            <h3>12K+</h3>
            <p>Pengguna</p>
            </div>
            """, unsafe_allow_html=True)

        with s3:
            st.markdown("""
            <div class="stat-box">
            <h3>8.7K+</h3>
            <p>Laporan</p>
            </div>
            """, unsafe_allow_html=True)

        with s4:
            st.markdown("""
            <div class="stat-box">
            <h3>98%</h3>
            <p>Respon</p>
            </div>
            """, unsafe_allow_html=True)

    with kanan:

        st.image(
            "aset/hero.png",
            use_container_width=True
        )

    st.markdown("<br><br>", unsafe_allow_html=True)

    # =====================================
    # FEATURE CARD
    # =====================================

    c1, c2, c3, c4 = st.columns(4)

    data = [

        (
            "Informasi Lengkap",
            "Dapatkan informasi lengkap berbagai jenis bencana."
        ),

        (
            "Bantuan Darurat",
            "Panduan cepat menghadapi situasi darurat."
        ),

        (
            "Laporan Kejadian",
            "Laporkan kejadian bencana secara langsung."
        ),

        (
            "Pantau Statistik",
            "Pantau laporan dan perkembangan bencana."
        )

    ]

    for col, item in zip(
        [c1, c2, c3, c4],
        data
    ):

        with col:

            st.markdown(f"""
            <div class="feature-dark">

            <div class="feature-dark-title">
            {item[0]}
            </div>

            <div class="feature-dark-desc">
            {item[1]}
            </div>

            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="dma-footer">

    DMA Assistant |
    Sistem Manajemen Krisis dan Bencana Berbasis FSM

    </div>
    """, unsafe_allow_html=True)