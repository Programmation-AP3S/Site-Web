# -*- coding: utf-8 -*-
"""
Site web AP3S

Outils de contexte
"""
from typing import Any

from app.context.professions import profession_of, professions

context: dict[str, Any] = {
    "professions": professions,
    "profession_of": profession_of,
}
