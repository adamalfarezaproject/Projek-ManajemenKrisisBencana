from enum import Enum


class State(Enum):

    # ==========================
    # MENU UTAMA
    # ==========================

    IDLE = "IDLE"

    # ==========================
    # MENU BENCANA
    # ==========================

    BANJIR_MENU = "BANJIR_MENU"

    GEMPA_MENU = "GEMPA_MENU"

    LONGSOR_MENU = "LONGSOR_MENU"

    KEBAKARAN_MENU = "KEBAKARAN_MENU"

    TSUNAMI_MENU = "TSUNAMI_MENU"

    # ==========================
    # PELAPORAN
    # ==========================

    INPUT_NAMA = "INPUT_NAMA"

    INPUT_LOKASI = "INPUT_LOKASI"

    INPUT_KRONOLOGI = "INPUT_KRONOLOGI"

    KONFIRMASI_LAPORAN = "KONFIRMASI_LAPORAN"

    # ==========================
    # CEK STATUS
    # ==========================

    INPUT_ID = "INPUT_ID"