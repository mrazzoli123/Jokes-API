#!/usr/bin/env python3
"""
jokes api logic

@author:
@version: 2025.11
"""

import pathlib
import random
import tomllib
import random
from functools import cache

import pyjokes
from pyjokes.exc import CategoryNotFoundError, LanguageNotFoundError

from .models import Joke
from flask import current_app

CATEGORIES=["neutral", "chuck"]
FULLJOKELIST = []


class Joker:

    @classmethod
    def init_dataset(cls):
        
        languages = current_app.config.get("LANGUAGES")
        lang_list=list(languages.keys())
        sorted_lang=sorted(lang_list)

        for lang in sorted_lang:
            try:
                temp_neutral = pyjokes.get_jokes(language=lang, category="neutral")
                for joke in temp_neutral:
                    FULLJOKELIST.append(
                        Joke(
                            language=lang,
                            category="neutral",
                            text=joke,
                        )
                    )
            except (Exception):
                pass
            try:
                temp_chuck = pyjokes.get_jokes(language=lang, category="chuck")
                for joke in temp_chuck:
                    FULLJOKELIST.append(
                        Joke(
                            language=lang,
                            category="chuck",
                            text=joke,
                        )
                    )
            except (Exception):
                pass
        
        if not FULLJOKELIST:
            raise ValueError("Dataset could not be initialized")
        



    @classmethod
    def get_jokes(cls, language: str = "any", category: str = "any", number: int = 0) -> list[Joke]:
        
        if not FULLJOKELIST:
            cls.init_dataset()

        if language != "any":
            languages = current_app.config.get("LANGUAGES")
            if language not in languages:
                raise ValueError("Invalid language")
        
        if category != "any":
            if category not in CATEGORIES:
                raise ValueError("Invalid category")
            
        if number < 0:
            raise ValueError("Number of jokes requested cannot be below 0")
        
        if language != "any" and category != "any":
            filtered_jokes = []
            for joke in FULLJOKELIST:
                if joke.language == language and joke.category == category:
                    filtered_jokes.append(joke)

            random.shuffle(filtered_jokes)

            if number > 0:
                return filtered_jokes[:number]
            else:
                return filtered_jokes

        elif language != "any" and category == "any":
            filtered_jokes = []
            for joke in FULLJOKELIST:
                if joke.language == language:
                    filtered_jokes.append(joke)

            random.shuffle(filtered_jokes)
            
            if number > 0:
                return filtered_jokes[:number]
            else:
                return filtered_jokes

        elif language == "any" and category != "any":
            filtered_jokes = []
            for joke in FULLJOKELIST:
                if joke.category == category:
                    filtered_jokes.append(joke)
            
            random.shuffle(filtered_jokes)

            if number > 0:
                return filtered_jokes[:number]
            else:
                return filtered_jokes

        elif language == "any" and category == "any":
            random.shuffle(FULLJOKELIST)
            if number > 0:
                return FULLJOKELIST[:number]
            else:
                return FULLJOKELIST

        

    @classmethod
    def get_the_joke(cls, joke_id: int) -> Joke:
    
        if not FULLJOKELIST:
            cls.init_dataset()

        if joke_id < 0 or joke_id >= len(FULLJOKELIST):
            raise ValueError(f"404 Not Found: Joke {joke_id} not found, try an id between 0 and 952")
        
        return FULLJOKELIST[joke_id-1]
