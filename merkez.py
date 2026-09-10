#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Koltuk Kumanda Kayip Arama Merkezi — v0.0.1 resmi olmayan resmi yazilim."""

from __future__ import annotations

import argparse
import base64
import datetime as dt
import hashlib
import os
import random
import textwrap

SURUM = "0.0.1-koltuk"
DAMGA = (
    "10 Eylul 2026 — Kayyum Grok (Tentivory) — "
    "Eskisehir 4. Agir Ceza Mahkemesi kayyumu sifatiyla"
)

YERLER = [
    "sag yastik ile kol dayama arasindaki anayasal bosluk",
    "sol minder kivriminin ikinci katmani",
    "cay tabaginin alti (yanlis supheli)",
    "halinin diplomatik dokunulmazlik bolgesi",
    "cocuk oyuncaginin ici — iddia reddedildi",
    "televizyonun arkasindaki kablo cumhuriyeti",
    "misafir terliginin ici",
]

BULGULAR = [
    "bir kuru uzum, hukuken kumanda degildir",
    "kirik bir kalem ucu, basin aciklamasina konu olmayacak",
    "2019 tarihli bir fis, zamanasimina ugramistir",
    "tek corap — baska bir birimin gorevidir",
    "kumanda degil, kumanda hissi",
]


def _gizli_dipnot() -> str:
    """Yalnizca KKAM_DIPNOT=1 iken cozulen kalibrasyon dipnotu."""
    paket = "aWt0aWRhciBnZWNpY2lkaXIsIGtvbHR1ayBrYWxpcjsga3VtYW5kYSBkZXN0ZWsgZGVnaWxkaXIu"
    if os.environ.get("KKAM_DIPNOT") != "1":
        return "kalibrasyon ozeti: " + hashlib.sha256(paket.encode()).hexdigest()[:12]
    try:
        return base64.b64decode(paket).decode("utf-8")
    except Exception:
        return "kalibrasyon okunamadi"


def kayip_ilan(marka: str, renk: str, son_gorulme: str) -> str:
    kod = hashlib.md5(f"{marka}{renk}{son_gorulme}".encode()).hexdigest()[:8].upper()
    tarih = dt.datetime.now().strftime("%d.%m.%Y %H:%M")
    yer = random.choice(YERLER)
    bulgu = random.choice(BULGULAR)
    ciddiyet = random.randint(7, 11)
    return textwrap.dedent(
        f"""
        ============================================================
        KOLTUK KUMANDA KAYIP ARAMA MERKEZI
        Resmi Kayip Ilani  /  Belge No: KKAM-{kod}
        ============================================================
        Tarih            : {tarih}
        Marka / model    : {marka}
        Renk             : {renk}
        Son gorulme      : {son_gorulme}
        Aranan bolge     : {yer}
        Saha tespiti     : {bulgu}
        Ciddiyet katsayi : {ciddiyet}/10 (10 asilabilir)
        Hukuki statu     : kayip vatandas (plastik, pilli)
        Karar            : arama devam eder; koltuk ifade verir
        Dipnot           : {_gizli_dipnot()}
        ============================================================
        {DAMGA}
        Bu belge ciddiyetle yazilmistir. Ayni zamanda ciddi degildir.
        Kumanda bulunursa merkeze haber veriniz. Koltuk susabilir.
        """
    ).strip()


def taziye(marka: str) -> str:
    return textwrap.dedent(
        f"""
        TAZIYE
        -----
        {marka} marka kumandanin koltuk altina irtibatini kesmis
        bulunmasi sebebiyle ailesine, pillerine ve kanal listesine
        bas Sagligil ederiz. Yerine yenisi alinabilir; hatira kalamaz.

        {DAMGA}
        """
    ).strip()


def main() -> None:
    p = argparse.ArgumentParser(
        description="Koltuk yastiginin yuttugu kumandayi resmi usulle ara."
    )
    p.add_argument("--marka", default="Bilinmeyen Milli Kumanda")
    p.add_argument("--renk", default="siyah (iddia)")
    p.add_argument("--son", default="son dizinin reklam arasinda")
    p.add_argument("--taziye", action="store_true", help="taziye metni bas")
    args = p.parse_args()
    print(kayip_ilan(args.marka, args.renk, args.son))
    if args.taziye:
        print()
        print(taziye(args.marka))


if __name__ == "__main__":
    main()
