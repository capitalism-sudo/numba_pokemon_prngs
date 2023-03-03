"""Module for data usage and access"""

import importlib.resources as pkg_resources
from ..resources import txt

SPECIES_EN = tuple(
    pkg_resources.read_text(txt, "species_en.txt", encoding="utf-8-sig").splitlines()
)
CONSTANT_CASE_SPECIES_EN = tuple(
    "SPECIES_NIDORAN_M"
    if name == "Nidoran♂"
    else "SPECIES_NIDORAN_F"
    if name == "Nidoran♀"
    else f"SPECIES_{name.upper()}"
    for name in SPECIES_EN
)
