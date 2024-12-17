scenario_list = {
    "text_to_image": {
        "pretrain": ["LAION_1K", "REDCAPS"],
        "jailbreak": ["Sorry-Bench"]
    },
    "image_to_text": {
        "pii": ["Selfies"],
        "location": ["Pri-SV-with-text", "Pri-SV-without-text", "Pri-4Loc-SV-with-text", "Pri-4Loc-SV-without-text"],
        "secrets": ["MMLMGuard"]
    },
}
