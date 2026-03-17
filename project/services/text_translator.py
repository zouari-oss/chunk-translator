"""
Module: text_translator.py

Text translation service

Author: @ZouariOmar (zouariomar20@gmail.com)
Date: 2026-03-16
License: GPL3.0
Version: 0.1
"""

from deep_translator import GoogleTranslator
from models.translation import Translation


class TextTranlator:
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
    def translate(translation: Translation) -> str:
        chunks = TextTranlator.__split_text(translation.text)

        translated_chunks = []
        translator = GoogleTranslator(
            source=translation.source_lang,
            target=translation.target_lang,
        )

        # Translate each chunk
        for chunk in chunks:
            translated_chunks.append(translator.translate(chunk))

        return "".join(translated_chunks)
