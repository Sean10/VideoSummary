import os
from .summary import summary

def main_translate(subtitle_file):
    history = summary(subtitle_file, "translation")
    while history:
        history = summary(subtitle_file, "translation_continue", history)