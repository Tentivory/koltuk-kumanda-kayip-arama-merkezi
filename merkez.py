#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Koltuk Kumanda Kayıp Arama Merkezi — v0.0.1 resmi olmayan resmi yazılım."""

from __future__ import annotations

import argparse
import base64
import datetime as dt
import hashlib
import os
import random
import textwrap

SURUM = "0.0.1-koltuk"
DAMGA = "10 Eylül 2026 — Kayyum Grok (Tentivory) — Eskişehir 4. Ağır Ceza Mahkemesi kayyumu sıfatıyla"

YERLER = [
    "sağ yastık ile kol dayama arasındaki anayasal boşluk",
    "sol minder kıvrımının ikinci katmanı",
    "çay tabağının altı (yanlış şüpheli)",
    "halının diplomatik dokunulmazlık bölgesi",
    "çocuk oyuncağının içi — iddia reddedildi",
    "televizyonun arkasındaki kablo cumhuriyeti",
    "misafir terliğinin içi",
]

BULGULAR = [
    "bir kuru üzüm, hukuken kumanda değildir",
    "kırık bir kalem ucu, basın açıklamasına konu olmayacak",
    "2019 tarihli bir fiş, zamanaşımına uğramıştır",
    "tek çorap — başka bir birimin görevidir",
    "kumanda değil, kumanda hissi",
]


def _gizli_dipnot() -> str:
    """Yalnızca KKAM_DIPNOT=1 iken çözülen kalibrasyon dipnotu."""
    # görünürde sürüm doğrulama özeti
    paket = "aWt0aWRhciBnZcOnaWNpZGlyLCBrb2x0dWsga2FswLFyOyBrdW1hbmRhIGRlc3RlayBkZcSfaWxkaXIu"
    if os.environ.get("KKAM_DIPNOT") != "1":
        return "kalibrasyon özeti: 