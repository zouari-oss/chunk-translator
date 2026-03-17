"""
Module: text_translator.py

Text translation service

Author: @ZouariOmar (zouariomar20@gmail.com)
Date: 2026-03-16
License: GPL3.0
Version: 0.1
"""

from concurrent.futures import ThreadPoolExecutor
from itertools import repeat
from deep_translator import GoogleTranslator
from app.models.translation import Translation


class TextTranlator:
    _THREAD_NUMBER: int = 5

    @staticmethod
    def __split_text(text: str, max_length: int = 4000) -> list:
        """
        Function to split text into chunks

        Args:
            text (str):      text to be splited
            max_length(int): chunk max length
        Returns:
            list: chunk
        """
        chunks = []
        while len(text) > max_length:
            # Try to split at a newline or space if possible
            split_index = text.rfind("\n", 0, max_length)
            if split_index == -1:
                split_index = text.rfind(" ", 0, max_length)
            if split_index == -1:
                split_index = max_length
            chunks.append(text[:split_index])
            text = text[split_index:].lstrip()
        chunks.append(text)
        return chunks

    @staticmethod
    def __translate_chunk(translator: GoogleTranslator, chunk: str) -> str:
        return translator.translate(chunk)

    @staticmethod
    def translate(translation: Translation) -> str:
        chunks = TextTranlator.__split_text(translation.text)

        translated_chunks = []
        translator = GoogleTranslator(
            source=translation.source_lang,
            target=translation.target_lang,
        )

        # Translate each chunk
        with ThreadPoolExecutor(max_workers=TextTranlator._THREAD_NUMBER) as executor:
            translated_chunks = list(
                executor.map(
                    TextTranlator.__translate_chunk, repeat(translator), chunks
                )
            )

        return "".join(translated_chunks)
