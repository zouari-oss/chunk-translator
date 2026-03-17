"""
Module: translation.py

This module defines data models for handling translations. It provides
a Pydantic `Translation` class for validating translation requests.

Author: @ZouariOmar (zouariomar20@gmail.com)
Date: 2026-03-17
License: GPL3.0
Version: 0.1
"""

from pydantic import BaseModel, Field


class Translation(BaseModel):
    """
    Data model representing a translation request.

    Attributes:
        text (str)       : The text to be translated.
        source_lang (str): The source language code (e.g., 'en').
        target_lang (str): The target language code (e.g., 'fr').

    Example:
        >>> Translation(
        ...     text="Hello World!",
        ...     source_lang="en",
        ...     target_lang="fr"
        ... )
    """

    text: str = Field(..., description="Text to be translated")
    source_lang: str = Field(..., description="Source language code (e.g., 'en')")
    target_lang: str = Field(..., description="Target language code (e.g., 'fr')")
