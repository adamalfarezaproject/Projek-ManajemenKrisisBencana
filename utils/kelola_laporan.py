import json
import os
from datetime import datetime


FILE_LAPORAN = "data/laporan.json"


def baca_laporan():

    if not os.path.exists(FILE_LAPORAN):

        return {}

    try:

        with open(
            FILE_LAPORAN,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except Exception:

        return {}


def simpan_semua_laporan(data):

    with open(
        FILE_LAPORAN,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )


def generate_id_laporan():

    laporan = baca_laporan()

    nomor = len(laporan) + 1

    tanggal = datetime.now().strftime("%Y%m%d")

    return f"DMA-{tanggal}-{nomor:03d}"


def simpan_laporan(data_laporan):

    laporan = baca_laporan()

    id_laporan = generate_id_laporan()

    laporan[id_laporan] = data_laporan

    simpan_semua_laporan(laporan)

    return id_laporan


def cari_laporan(id_laporan):

    laporan = baca_laporan()

    return laporan.get(id_laporan)


def update_status(id_laporan, status_baru):

    laporan = baca_laporan()

    if id_laporan not in laporan:

        return False

    laporan[id_laporan]["status"] = status_baru

    simpan_semua_laporan(laporan)

    return True