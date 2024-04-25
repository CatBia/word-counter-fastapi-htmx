import re

async def word_count(text:str):
    return len(re.findall(r"[\w-]+", text))