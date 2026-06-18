import streamlit as st

from utils.kelola_kuis import (
    load_soal,
    hitung_skor,
    kategori_nilai
)


def tampilkan_kuis():

    soal_list = load_soal()

    # ==================================
    # SESSION
    # ==================================

    if "nomor_soal" not in st.session_state:

        st.session_state.nomor_soal = 0

    if "jawaban_user" not in st.session_state:

        st.session_state.jawaban_user = []

    if "selesai_kuis" not in st.session_state:

        st.session_state.selesai_kuis = False

    # ==================================
    # HEADER
    # ==================================

    st.markdown(
        """
        <div class="quiz-header">
            <h1>Kuis Kesiapsiagaan Bencana</h1>
            <p>
            Uji pengetahuan Anda mengenai kesiapsiagaan,
            mitigasi, dan penanganan bencana alam.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # ==================================
    # HASIL
    # ==================================

    if st.session_state.selesai_kuis:

        skor, benar, salah = hitung_skor(
            st.session_state.jawaban_user,
            soal_list
        )

        kategori, warna = kategori_nilai(
            skor
        )

        st.markdown(
            f"""
            <div class="quiz-result">
                <h2>Hasil Kuis</h2>
                <h1>{skor}</h1>
                <p>{kategori}</p>
                <p>Jawaban Benar : {benar}</p>
                <p>Jawaban Salah : {salah}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button(
            "Ulangi Kuis",
            use_container_width=True
        ):

            st.session_state.nomor_soal = 0

            st.session_state.jawaban_user = []

            st.session_state.selesai_kuis = False

            st.rerun()

        return

    # ==================================
    # PROGRESS
    # ==================================

    nomor = st.session_state.nomor_soal

    total = len(soal_list)

    progress = nomor / total

    st.progress(progress)

    st.markdown(
        f"""
        <p style="
        color:#94A3B8;
        font-size:14px;">
        Soal {nomor + 1} dari {total}
        </p>
        """,
        unsafe_allow_html=True
    )

    # ==================================
    # SOAL
    # ==================================

    soal = soal_list[nomor]

    st.markdown(
        f"""
        <div class="quiz-card">

        <h3>
        {soal["pertanyaan"]}
        </h3>

        </div>
        """,
        unsafe_allow_html=True
    )

    jawaban = st.radio(

        "Pilih Jawaban",

        soal["opsi"],

        label_visibility="collapsed"
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # ==================================
    # NEXT
    # ==================================

    st.markdown(
        '<div class="quiz-btn">',
        unsafe_allow_html=True
    )

    next_btn = st.button(
        "Selanjutnya",
        use_container_width=True
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

    if next_btn:

        st.session_state.jawaban_user.append(
            jawaban
        )

        st.session_state.nomor_soal += 1

        if (
            st.session_state.nomor_soal
            >=
            total
        ):

            st.session_state.selesai_kuis = True

        st.rerun()