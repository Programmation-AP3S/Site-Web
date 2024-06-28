# -*- coding: utf-8 -*-
"""
Site web AP3S

Liste des posts
"""
import tomllib

__all__: list[str] = [
    "posts"
]

with open("conf/posts.toml", "rb") as f:
    posts: dict = tomllib.load(f)
