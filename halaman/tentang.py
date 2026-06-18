import streamlit as st


def tampilkan_tentang():

    # ==================================
    # HERO
    # ==================================

    kiri, kanan = st.columns([1.2, 0.8])

    with kiri:

        st.markdown(
            """
            <div class="about-badge">
            TENTANG SISTEM
            </div>

            <h1 class="about-title">
            Mengenal Sistem
            <span>DMA Assistant</span>
            </h1>

            <p class="about-desc">
            DMA Assistant adalah sistem informasi
            bencana berbasis Finite State Machine (FSM)
            yang dirancang untuk memberikan informasi,
            bantuan darurat, pelaporan kejadian,
            dan pemantauan laporan secara real-time.
            </p>
            """,
            unsafe_allow_html=True
        )

    with kanan:

        st.markdown(
            '<div class="about-image">',
            unsafe_allow_html=True
        )

        st.image(
            "aset/tentang.png",
            use_container_width=True
        )

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)



    # ==================================
    # FITUR UTAMA
    # ==================================

    st.markdown(
        """
        <div class="section-title-about">
        FITUR UTAMA SISTEM
        </div>
        """,
        unsafe_allow_html=True
    )

    c1, c2, c3, c4 = st.columns(4)

    fitur = [

        (
            "Edukasi Informasi",
            "Menyediakan informasi lengkap seputar bencana, penyebab, dampak, dan langkah mitigasi."
        ),

        (
            "Bantuan Darurat",
            "Memberikan akses cepat ke layanan darurat dan kontak penting saat keadaan genting."
        ),

        (
            "Pelaporan Kejadian",
            "Memudahkan pengguna melaporkan kejadian bencana di sekitar dengan proses yang cepat."
        ),

        (
            "Pemantauan Laporan",
            "Memantau status laporan pengguna secara real-time hingga proses penanganan selesai."
        )

    ]

    for col, item in zip(
        [c1, c2, c3, c4],
        fitur
    ):

        with col:

            st.markdown(
                f'<div class="about-feature-card"><h3>{item[0]}</h3><p>{item[1]}</p></div>',
                unsafe_allow_html=True
            )

            st.markdown(
                "<div style='height:20px'></div>",
                unsafe_allow_html=True
            )

    # ==================================
    # TEKNOLOGI & MANFAAT
    # ==================================

    kiri, kanan = st.columns([1.2, 1])

    with kiri:

        st.markdown(
            """
            <div class="section-title-about">
            TEKNOLOGI YANG DIGUNAKAN
            </div>
            """,
            unsafe_allow_html=True
        )

        t1, t2 = st.columns(2)

        with t1:

            st.markdown(
                """
                <div class="tech-card">

                <h3>
                Finite State Machine (FSM)
                </h3>

                <p>
                Mengatur alur percakapan dan layanan sesuai state untuk respons yang akurat.
                </p>

                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                """
                <div class="tech-card">

                <h3>
                Real-time Processing
                </h3>

                <p>
                Memproses setiap permintaan pengguna secara real-time dan responsif.
                </p>

                </div>
                """,
                unsafe_allow_html=True
            )

        with t2:

            st.markdown(
                """
                <div class="tech-card">

                <h3>
                Database JSON
                </h3>

                <p>
                Menyimpan data pengguna, laporan, dan informasi bencana dengan aman.
                </p>

                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                """
                <div class="tech-card">

                <h3>
                Keamanan Data
                </h3>

                <p>
                Mendukung tata kelola data dengan sistem keamanan sederhana.
                </p>

                </div>
                """,
                unsafe_allow_html=True
            )

    with kanan:

        st.markdown(
            """
            <div class="section-title-about">
            MANFAAT SISTEM
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="benefit-card">

            <ul>

            <li>Informasi bencana yang akurat dan terpercaya</li>

            <li>Akses layanan darurat lebih cepat dan mudah</li>

            <li>Pelaporan kejadian lebih efisien</li>

            <li>Pemantauan laporan secara transparan</li>

            <li>Mendukung pengambilan keputusan yang lebih baik</li>

            </ul>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # ==================================
    # TIM
    # ==================================
    st.markdown("### Disaster Management Assistant")

    col1, col2 = st.columns([2, 1])

    with col1:

        st.write("Arvan")
        st.write("Adam")
        st.write("Kenang")

    with col2:

        st.write("Kelompok 3")
        st.write("Informatika")
        st.write("2026")