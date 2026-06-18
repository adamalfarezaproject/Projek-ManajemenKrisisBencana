import json


# ==================================
# LOAD SOAL
# ==================================

def load_soal():

    with open(
        "data/soal_kuis.json",
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


# ==================================
# HITUNG SKOR
# ==================================

def hitung_skor(jawaban_user, soal_list):

    benar = 0

    for i in range(len(jawaban_user)):

        if (
            jawaban_user[i]
            ==
            soal_list[i]["jawaban"]
        ):
            benar += 1

    total = len(soal_list)

    skor = round(
        (benar / total) * 100
    )

    salah = total - benar

    return skor, benar, salah


# ==================================
# KATEGORI NILAI
# ==================================

def kategori_nilai(skor):

    if skor >= 90:

        return (
            "Ahli Bencana",
            "#F59E0B"
        )

    elif skor >= 75:

        return (
            "Tanggap",
            "#10B981"
        )

    elif skor >= 60:

        return (
            "Siaga",
            "#3B82F6"
        )

    else:

        return (
            "Pemula",
            "#EF4444"
        )


# ==================================
# RESET KUIS
# ==================================

def reset_kuis():

    return {

        "nomor_soal": 0,

        "jawaban_user": [],

        "selesai": False
    }