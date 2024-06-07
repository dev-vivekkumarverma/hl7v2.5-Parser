from typing import TypedDict

# component separator, repetition separator, escape character, and subcomponent separator.

v2EncodingChars=TypedDict(
    "v2EncodingChars",
    {
        "dataFieldSep":str,
        "escapeSeq":str,
        "componentSep":str,
        "sub-componentSep":str,
        "repetitionSep":str
    }
)