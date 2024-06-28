# -*- coding: utf-8 -*-
"""
Site web AP3S

Outils de contexte
"""
from typing import Any

from app.context.posts import posts
from app.context.professions import profession_of, professions

__all__: list[str] = [
    "context"
]

context: dict[str, Any] = {
    "posts": posts,
    "professions": professions,
    "profession_of": profession_of,
}
