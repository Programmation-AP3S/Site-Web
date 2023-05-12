#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Outil de compilation

Compile le code Jinja 2
"""
import os
import shutil
from typing import Any

import jinja2
import tomllib

from app.context import context as ctx

jinja_env: jinja2.Environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader("src/"),
    autoescape=True,
)

with open("conf/context.toml", "rb") as f:
    context: dict[str, Any] = tomllib.load(f)

with open("conf/medecins.toml", "rb") as f:
    medecins: list[dict[str, Any]] = list(tomllib.load(f).values())

print(medecins)


def render(location: str, file: str) -> str:
    """
    Render a Jinja2 template.

    :param str location: File location.
    :param str file: File name.
    :return str: Generated code.
    """
    print(f"render::{location}/{file}")
    return jinja_env.get_template(file).render(
        **context, liste_medecins=medecins, **ctx
    )


def config() -> dict:
    """
    Charge la configuration des routes.

    :return dict: Les routes.
    """
    with open("conf/routes.toml", "rb") as file:
        return tomllib.load(file)


def routes(config: dict, base_path: str = "/") -> dict[str, str]:
    """
    Génère les routes dans un format standard.

    :param dict config: Configuration des routes.
    :param str base_path: Chemin de base.
    :return dict[str, str]: Route / Chemin du template.
    """
    routed_map: dict[str, str] = {}
    for url, element in config.items():
        if isinstance(element, dict):
            routed_map.update(routes(element, base_path + url + "/"))
        elif isinstance(element, str):
            routed_map[base_path + url] = element
    return routed_map


def empty_build() -> None:
    """
    Supprime le répertoire /build.

    Recrée le répertoire.
    """
    shutil.rmtree("build")
    os.mkdir("build")


def main() -> None:
    """
    Script principal.

    Compile le code Jinja.
    """
    configuration: dict = config()
    routed_map: dict[str, str] = routes(configuration)
    empty_build()
    for route, file in routed_map.items():
        directories: str = "/".join(("build/" + route).split("/")[:-1])
        os.makedirs(directories, exist_ok=True)
        print("route::", route)
        print("file::", file)
        with open("build/" + route + ".html", "w") as f:
            f.write(render("", "pages/" + file))


if __name__ == "__main__":
    main()
    main()
