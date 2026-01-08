#!/usr/bin/env python3
"""
jokes api routes

@author:
@version: 2025.11
"""

import pyjokes
from typing import Literal
from .logic import Joker

from flask import Blueprint, abort, jsonify
from werkzeug import Response
from werkzeug.exceptions import NotFound

from flask import current_app

main = Blueprint("main", __name__, url_prefix="/api/v1/jokes")


@main.get("/zoli")
def hello_zoli():
    languages = current_app.config.get("LANGUAGES")
    lang_list=list(languages.keys())
    return lang_list



@main.route("/<string:language>/<string:category>/all")
def get_all_jokes_by_language_and_category(language: str, category: str) -> Response:
    
    try:
        jokes = Joker.get_jokes(language=language, category=category)
        jokes_json = {"jokes": [joke.text for joke in jokes]}
        return jsonify(jokes_json)
    except ValueError as e:
        return jsonify({"error": str(e)}), 500

    


@main.route("/<string:language>/<string:category>/<int:number>")
def get_n_jokes_by_language_and_category(language: str, category: str, number: int):
    
    try:
        jokes = Joker.get_jokes(language=language, category=category, number=number)
        jokes_json = {"jokes": [joke.text for joke in jokes]}
        return jsonify(jokes_json)
    except ValueError as e:
        return jsonify({"error": str(e)}), 500



@main.route("/<int:joke_id>")
def get_the_joke(joke_id: int):
    
    try:
        joke_result = Joker.get_the_joke(joke_id)
        jokes_json = {"joke": [joke_result.text]}

        return jsonify(jokes_json)
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

@main.errorhandler(404)
def not_found(error: NotFound) -> tuple[Response, Literal[404]]:
    return jsonify({"error": "not found"}), 404





