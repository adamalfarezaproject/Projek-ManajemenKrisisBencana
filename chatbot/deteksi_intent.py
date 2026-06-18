def deteksi_intent(pesan):

    pesan = pesan.lower().strip()

    # ==========================
    # MENU & RESET
    # ==========================

    if pesan in [
        "menu",
        "menu utama",
        "kembali",
        "home"
    ]:
        return "MENU"

    if pesan in [
        "reset",
        "ulang",
        "restart"
    ]:
        return "RESET"

    # ==========================
    # PILIH BENCANA
    # ==========================

    if pesan == "banjir":
        return "BANJIR"

    if pesan == "gempa":
        return "GEMPA"

    if pesan == "longsor":
        return "LONGSOR"

    if pesan == "kebakaran":
        return "KEBAKARAN"

    if pesan == "tsunami":
        return "TSUNAMI"

    # ==========================
    # MENU LAYANAN
    # ==========================

    if pesan == "1":
        return "INFORMASI"

    if pesan == "2":
        return "DARURAT"

    if pesan == "3":
        return "LAPOR"

    # ==========================
    # TEKS LAYANAN
    # ==========================

    if "informasi" in pesan:
        return "INFORMASI"

    if "darurat" in pesan:
        return "DARURAT"

    if "bantuan" in pesan:
        return "DARURAT"

    if pesan == "lapor":
        return "LAPOR"

    # ==========================
    # STATUS LAPORAN
    # ==========================

    if "status" in pesan:
        return "STATUS"

    # ==========================
    # KONFIRMASI YA
    # ==========================

    if pesan in [
        "ya",
        "iya",
        "y",
        "ok",
        "oke"
    ]:
        return "YA"

    # ==========================
    # KONFIRMASI TIDAK
    # ==========================

    if pesan in [
        "tidak",
        "ga",
        "gak",
        "nggak",
        "batal",
        "n"
    ]:
        return "TIDAK"

    # ==========================
    # TIDAK DIKENALI
    # ==========================

    return "TIDAK_DIKENALI"