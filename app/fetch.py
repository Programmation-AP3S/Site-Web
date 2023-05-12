#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MSP AP3S

Script de génération de la liste des médecins
"""
import csv
import re
import unicodedata
from typing import TYPE_CHECKING, TypeAlias

import tomli_w

if TYPE_CHECKING:
    from _csv import _reader

Medecin: TypeAlias = tuple[str, str, str, str, str]
"""Nom, Profession, Téléphone, Doctolib, Biographie"""


def strip_accents(s):
    return "".join(
        c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn"
    )


class ListeMedecins:
    """Charge la liste des médecins."""

    def __init__(self):
        """
        Initialise l'objet.

        Charge les fichiers.
        """
        self.medecins: list[Medecin] = self._liste_medecins()
        self.export()

    def _liste_medecins(self) -> list[Medecin]:
        with open("conf/liste_medecins.csv") as file:
            reader: _reader = csv.reader(file)
            data: list[list[str]] = [row for row in reader]
        liste_medecins: list[Medecin] = []
        for row in data:
            liste_medecins.append((" ".join(row[:3]), row[3], row[7], "", ""))
        return liste_medecins

    def export(self) -> None:
        """
        Export the data.

        Saved in conf/medecins.toml.
        """
        dictionnaire: dict[str, dict[str, str]] = {}
        for medecin in self.medecins:
            dictionnaire[strip_accents(medecin[0].replace(" ", "_").lower())] = {
                "name": medecin[0],
                "profession": medecin[1],
                "telephone": medecin[2],
                "doctolib": "",
                "bio": "",
            }
        with open("conf/medecins.toml", "wb") as file:
            tomli_w.dump(dictionnaire, file)


if __name__ == "__main__":
    liste_medecins: ListeMedecins = ListeMedecins()
