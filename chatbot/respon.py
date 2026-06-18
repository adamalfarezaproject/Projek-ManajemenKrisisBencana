from chatbot.state import State


def generate_respon(state):

    responses = {

        # ==========================
        # MENU UTAMA
        # ==========================

        State.IDLE:
        """
Selamat Datang di Disaster Management Assistant (DMA)

Layanan yang tersedia:

1. Banjir
2. Gempa
3. Longsor
4. Kebakaran
5. Tsunami
6. Cek Status Laporan

Ketik nama bencana untuk memulai.

Contoh:
banjir
gempa
status
""",

        # ==========================
        # MENU BANJIR
        # ==========================

        State.BANJIR_MENU:
        """
Anda memilih layanan BANJIR.

Pilih layanan yang tersedia:

1. Informasi Bencana
2. Bantuan Darurat
3. Lapor Kejadian

Ketik angka atau nama layanan.
""",

        # ==========================
        # MENU GEMPA
        # ==========================

        State.GEMPA_MENU:
        """
Anda memilih layanan GEMPA.

Pilih layanan yang tersedia:

1. Informasi Bencana
2. Bantuan Darurat
3. Lapor Kejadian

Ketik angka atau nama layanan.
""",

        # ==========================
        # MENU LONGSOR
        # ==========================

        State.LONGSOR_MENU:
        """
Anda memilih layanan LONGSOR.

Pilih layanan yang tersedia:

1. Informasi Bencana
2. Bantuan Darurat
3. Lapor Kejadian

Ketik angka atau nama layanan.
""",

        # ==========================
        # MENU KEBAKARAN
        # ==========================

        State.KEBAKARAN_MENU:
        """
Anda memilih layanan KEBAKARAN.

Pilih layanan yang tersedia:

1. Informasi Bencana
2. Bantuan Darurat
3. Lapor Kejadian

Ketik angka atau nama layanan.
""",

        # ==========================
        # MENU TSUNAMI
        # ==========================

        State.TSUNAMI_MENU:
        """
Anda memilih layanan TSUNAMI.

Pilih layanan yang tersedia:

1. Informasi Bencana
2. Bantuan Darurat
3. Lapor Kejadian

Ketik angka atau nama layanan.
""",

        # ==========================
        # PELAPORAN
        # ==========================

        State.INPUT_NAMA:
        """
Pelaporan Kejadian Bencana

Silakan masukkan nama pelapor.
""",

        State.INPUT_LOKASI:
        """
Masukkan lokasi kejadian bencana.
""",

        State.INPUT_KRONOLOGI:
        """
Masukkan kronologi atau kondisi yang terjadi.
""",

        State.KONFIRMASI_LAPORAN:
        """
Periksa kembali data laporan Anda.

Ketik:

ya

atau

tidak
""",

        # ==========================
        # STATUS LAPORAN
        # ==========================

        State.INPUT_ID:
        """
Pemeriksaan Status Laporan

Silakan masukkan ID laporan.

Contoh:
DMA001
"""
    }

    return responses.get(
        state,
        """
Perintah tidak dikenali.

Ketik:
menu

untuk kembali ke menu utama.
"""
    )