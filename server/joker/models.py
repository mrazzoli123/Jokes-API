#!/usr/bin/env python3
"""
jokes api models

@author:
@version: 2025.11
"""

from dataclasses import dataclass

@dataclass
class Joke:
    
    language:str
    category:str
    text:str

    def __init__(self, language: str, category: str, text: str) -> None:
        self.language = language
        self.category = category
        self.text = text

    
