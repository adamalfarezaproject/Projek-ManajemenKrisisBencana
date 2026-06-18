from chatbot.fsm import FSM
from chatbot.state import State
from chatbot.deteksi_intent import deteksi_intent
from chatbot.respon import generate_respon

from utils.kelola_laporan import (
    simpan_laporan,
    cari_laporan
)


class MesinChatbot:

    def __init__(self):

        self.fsm = FSM()

        self.data_laporan = {}

        self.jenis_bencana_aktif = None

    # ==========================
    # RESET
    # ==========================

    def reset(self):

        self.fsm.current_state = State.IDLE

        self.data_laporan = {}

        self.jenis_bencana_aktif = None

    # ==========================
    # PROSES PESAN
    # ==========================

    def proses_pesan(self, pesan):

        pesan = pesan.strip()

        intent = deteksi_intent(pesan)
        if intent in [
            "BANJIR",
            "GEMPA",
            "LONGSOR",
            "KEBAKARAN",
            "TSUNAMI"
        ]:

            self.fsm.current_state = State.IDLE
        state = self.fsm.current_state

        # ==========================
        # RESET
        # ==========================

        if intent == "RESET":

            self.reset()

            return generate_respon(State.IDLE)

        # ==========================
        # MENU
        # ==========================

        if intent == "MENU":

            self.reset()

            return generate_respon(State.IDLE)

        # ==========================
        # SIMPAN BENCANA AKTIF
        # ==========================

        if intent == "BANJIR":
            self.jenis_bencana_aktif = "Banjir"

        elif intent == "GEMPA":
            self.jenis_bencana_aktif = "Gempa"

        elif intent == "LONGSOR":
            self.jenis_bencana_aktif = "Longsor"

        elif intent == "KEBAKARAN":
            self.jenis_bencana_aktif = "Kebakaran"

        elif intent == "TSUNAMI":
            self.jenis_bencana_aktif = "Tsunami"

        # ==========================
        # MENU BANJIR
        # ==========================

        if state == State.BANJIR_MENU:

            if intent == "INFORMASI":

                return """
Informasi Banjir

Banjir merupakan peristiwa meluapnya air yang menggenangi wilayah daratan.

Penyebab:
- Curah hujan tinggi
- Sungai meluap
- Drainase buruk

Dampak:
- Kerusakan rumah
- Gangguan transportasi
- Penyebaran penyakit

Ketik:
menu
"""

            elif intent == "DARURAT":

                return """
Bantuan Darurat Banjir

- Segera menuju tempat lebih tinggi
- Hindari arus deras
- Matikan listrik
- Bawa dokumen penting
- Hubungi petugas setempat

Ketik:
lapor
"""

        # ==========================
        # MENU GEMPA
        # ==========================

        if state == State.GEMPA_MENU:

            if intent == "INFORMASI":

                return """
Informasi Gempa

Gempa bumi terjadi akibat pergerakan lempeng bumi.

Dampak:
- Kerusakan bangunan
- Korban jiwa
- Longsor
- Tsunami

Mitigasi:
- Kenali jalur evakuasi
- Siapkan tas darurat
- Ikuti simulasi bencana

Ketik:
menu
"""

            elif intent == "DARURAT":

                return """
Bantuan Darurat Gempa

- Lindungi kepala
- Berlindung di bawah meja
- Jauhi kaca
- Keluar menuju area terbuka

Ketik:
lapor
"""

        # ==========================
        # MENU LONGSOR
        # ==========================

        if state == State.LONGSOR_MENU:

            if intent == "INFORMASI":

                return """
Informasi Longsor

Longsor terjadi akibat pergerakan massa tanah atau batuan.

Penyebab:
- Curah hujan tinggi
- Lereng tidak stabil
- Penggundulan hutan

Dampak:
- Kerusakan rumah
- Akses jalan terputus
"""

            elif intent == "DARURAT":

                return """
Bantuan Darurat Longsor

- Menjauh dari lereng
- Cari area aman
- Ikuti jalur evakuasi

Ketik:
lapor
"""

        # ==========================
        # MENU KEBAKARAN
        # ==========================

        if state == State.KEBAKARAN_MENU:

            if intent == "INFORMASI":

                return """
Informasi Kebakaran

Penyebab:
- Korsleting listrik
- Kebocoran gas
- Kelalaian manusia

Dampak:
- Kerusakan bangunan
- Korban jiwa
"""

            elif intent == "DARURAT":

                return """
Bantuan Darurat Kebakaran

- Matikan sumber listrik
- Gunakan APAR jika aman
- Evakuasi bangunan
- Hubungi pemadam kebakaran

Ketik:
lapor
"""

        # ==========================
        # MENU TSUNAMI
        # ==========================

        if state == State.TSUNAMI_MENU:

            if intent == "INFORMASI":

                return """
Informasi Tsunami

Tsunami biasanya dipicu oleh gempa bawah laut.

Dampak:
- Banjir pesisir
- Kerusakan infrastruktur
- Korban jiwa
"""

            elif intent == "DARURAT":

                return """
Bantuan Darurat Tsunami

- Segera menuju tempat tinggi
- Jauhi pantai
- Ikuti arahan petugas

Ketik:
lapor
"""

        # ==========================
        # INPUT NAMA
        # ==========================

        if state == State.INPUT_NAMA:

            if not pesan:

                return "Nama pelapor tidak boleh kosong."

            self.data_laporan["nama"] = pesan

            self.fsm.current_state = State.INPUT_LOKASI

            return generate_respon(State.INPUT_LOKASI)

        # ==========================
        # INPUT LOKASI
        # ==========================

        if state == State.INPUT_LOKASI:

            if not pesan:

                return "Lokasi kejadian tidak boleh kosong."

            self.data_laporan["lokasi"] = pesan

            self.fsm.current_state = State.INPUT_KRONOLOGI

            return generate_respon(State.INPUT_KRONOLOGI)

        # ==========================
        # INPUT KRONOLOGI
        # ==========================

        if state == State.INPUT_KRONOLOGI:

            if not pesan:

                return "Kronologi tidak boleh kosong."

            self.data_laporan["kronologi"] = pesan

            self.fsm.current_state = State.KONFIRMASI_LAPORAN

            return f"""
Konfirmasi Laporan

Jenis      : {self.jenis_bencana_aktif}
Nama       : {self.data_laporan['nama']}
Lokasi     : {self.data_laporan['lokasi']}
Kronologi  : {self.data_laporan['kronologi']}

Ketik:
ya
atau
tidak
"""

        # ==========================
        # KONFIRMASI
        # ==========================
        if state == State.KONFIRMASI_LAPORAN:

            if intent == "YA":

                if not self.jenis_bencana_aktif:

                    self.reset()

                    return """
        Silakan pilih jenis bencana terlebih dahulu.

        Contoh:
        banjir
        gempa
        longsor
        kebakaran
        tsunami
        """

                data_laporan = {
                    "nama": self.data_laporan["nama"],
                    "jenis": self.jenis_bencana_aktif,
                    "lokasi": self.data_laporan["lokasi"],
                    "kronologi": self.data_laporan["kronologi"],
                    "status": "Menunggu Verifikasi"
                }

                id_laporan = simpan_laporan(
                    data_laporan
                )

                self.reset()


                return f"""
Laporan berhasil dibuat.

ID Laporan:
{id_laporan}

Status:
Menunggu Verifikasi

Gunakan ID tersebut untuk memeriksa status laporan.
"""

            elif intent == "TIDAK":

                self.reset()

                return """
Laporan dibatalkan.
"""

            return """
Silakan ketik:

ya
atau
tidak
"""

        # ==========================
        # CEK STATUS
        # ==========================

        if state == State.INPUT_ID:

            id_laporan = pesan.strip().upper()

            data = cari_laporan(id_laporan)

            self.fsm.current_state = State.IDLE

            if data:

                return f"""
Status Laporan

ID:
{id_laporan}

Jenis:
{data['jenis']}

Lokasi:
{data['lokasi']}

Status:
{data['status']}
"""

            return f"""
ID laporan {id_laporan} tidak ditemukan.

Pastikan ID yang dimasukkan benar.
"""

        # ==========================
        # FSM
        # ==========================

        state_baru = self.fsm.transition(intent)

        # jika masuk mode pelaporan
        if state_baru == State.INPUT_NAMA:

            return generate_respon(State.INPUT_NAMA)

        # jika masuk cek status
        if state_baru == State.INPUT_ID:

            return generate_respon(State.INPUT_ID)

        return generate_respon(state_baru)