# -*- coding: utf-8 -*-
"""
Site web AP3S

Liste des professions
"""
from typing import Any

import tomllib

__all__: list[str] = [
    "professions",
    "profession_of",
]

with open("conf/professions.toml", "rb") as f:
    professions: dict[str, dict[str, Any]] = tomllib.load(f)

profession_of: dict[str, str] = {}
"""Dictionnaire entre un code et un identifiant de profession."""

for identifiant, profession in professions.items():
    for code in profession["codes"]:
        profession_of[code] = identifiant
