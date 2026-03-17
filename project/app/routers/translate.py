"""
Module: translate.py

`/translate` POST route handler

Author: @ZouariOmar (zouariomar20@gmail.com)
Date: 2026-03-17
License: GPL3.0
Version: 0.1
"""

from fastapi import APIRouter, status
from app.models.translation import Translation
from app.services.text_translator import TextTranlator

router = APIRouter()


@router.post("/translate")
async def create_translation(translation: Translation):
    """
    Translate a given text from a source language to a target language.

    Args:
        translation (Translation): The translation request containing the text,
            source language, and target language.

    Returns:
        Translation: The json translation result
    """
    if (
        not translation.text
        or not translation.source_lang
        or not translation.target_lang
    ):  # Missing field(s)
        return {
            "status": status.HTTP_400_BAD_REQUEST,
            "detail": "Missing required field(s)",
        }

    return {
        "status": status.HTTP_200_OK,
        "translated_text": TextTranlator.translate(translation),
    }
