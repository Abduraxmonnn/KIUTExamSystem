from django.test import TestCase

# Create your tests here.

data = [
    {
        "id": 111,
        "rate": 1,
        "question": [
            {
                "type": "text",
                "content": " NLPda \"TF-IDF\""
            },
            {
                "type": "image",
                "content": [
                    "media/image1.png"
                ]
            },
            {
                "type": "text",
                "content": " nima?\n"
            }
        ],
        "option1": [
            {
                "type": "text",
                "content": " Matndagi so`zning ahamiyatini uning hujjat korpusida tez-tezligi va paydo bo`lishiga qarab baholash usuli.\n"
            },
            {
                "correct": True
            }
        ],
        "option2": [
            {
                "type": "text",
                "content": " Matnlarni tasniflash algoritmi."
            },
            {
                "type": "image",
                "content": [
                    "media/image1.png"
                ]
            },
            {
                "correct": False
            }
        ],
        "option3": [
            {
                "type": "text",
                "content": " Matndagi sinonim va antonimlarni aniqlash texnologiyasi.\n"
            },
            {
                "correct": False
            }
        ],
        "option4": [
            {
                "type": "text",
                "content": " Gaplar ohangini aniqlash usuli.\n"
            },
            {
                "correct": False
            }
        ]
    },
    {
        "id": 112,
        "rate": 1,
        "question": [
            {
                "type": "text",
                "content": " NLPda \"So' z ma' nosini ajratish\" nima?\n"
            }
        ],
        "option1": [
            {
                "type": "text",
                "content": " Kontekstda so`z ma'nosini ajratib ko`rsatish texnikasi.\n"
            },
            {
                "correct": True
            }
        ],
        "option2": [
            {
                "type": "text",
                "content": " Gapning semantik tuzilishini aniqlash usuli.\n"
            },
            {
                "correct": False
            }
        ],
        "option3": [
            {
                "type": "text",
                "content": " Matndagi tayanch iboralarni ajratib olish algoritmi.\n"
            },
            {
                "correct": False
            }
        ],
        "option4": [
            {
                "type": "text",
                "content": " Matnni vektor "
            },
            {
                "type": "image",
                "content": [
                    "media/image1.png"
                ]
            },
            {
                "type": "text",
                "content": "sifatida ifodalash modeli.\n"
            },
            {
                "correct": False
            }
        ]
    },
    {
        "id": 113,
        "rate": 1,
        "question": [
            {
                "type": "text",
                "content": " NLPda "
            },
            {
                "type": "image",
                "content": [
                    "media/image2.png"
                ]
            },
            {
                "type": "text",
                "content": "\"Sintaksis daraxti\" nima?\n"
            }
        ],
        "option1": [
            {
                "type": "text",
                "content": " Gapning sintaktik tuzilishini ifodalovchi daraxt.\n"
            },
            {
                "correct": True
            }
        ],
        "option2": [
            {
                "type": "text",
                "content": " Matndagi so`zlar orasidagi semantik munosabatlarni aks ettiruvchi tuzilma.\n"
            },
            {
                "correct": False
            }
        ],
        "option3": [
            {
                "type": "text",
                "content": " Matnni grafik shaklida tasvirlash modeli.\n"
            },
            {
                "correct": False
            }
        ],
        "option4": [
            {
                "type": "text",
                "content": " Matndagi kalit so`zlarni ajratib ko`rsatish usuli.\n"
            },
            {
                "correct": False
            }
        ]
    },
    {
        "id": 114,
        "rate": 1,
        "question": [
            {
                "type": "text",
                "content": " NLPda \"Sentiment Analysis\" nima?"
            },
            {
                "type": "image",
                "content": [
                    "media/image2.png"
                ]
            }
        ],
        "option1": [
            {
                "type": "text",
                "content": " Matn hissiyotini tahlil qilish va aniqlash vazifasi.\n"
            },
            {
                "correct": True
            }
        ],
        "option2": [
            {
                "type": "text",
                "content": " Matndagi gap qismlarini aniqlash usuli.\n"
            },
            {
                "correct": False
            }
        ],
        "option3": [
            {
                "type": "text",
                "content": " So`zlar orasidagi sintaktik munosabatlarni ajratib ko`rsatish algoritmi.\n"
            },
            {
                "correct": False
            }
        ],
        "option4": [
            {
                "type": "text",
                "content": " Gapdagi tayanch iboralarni ajratib ko`rsatish usuli.\n"
            },
            {
                "correct": False
            }
        ]
    },
    {
        "id": 115,
        "rate": 1,
        "question": [
            {
                "type": "text",
                "content": " Tabiiy tilni "
            },
            {
                "type": "image",
                "content": [
                    "media/image2.png"
                ]
            },
            {
                "type": "text",
                "content": "qayta ishlash kontekstida \"Transfer Learning\" nima?\n"
            }
        ],
        "option1": [
            {
                "type": "text",
                "content": " Bilim va tajribani bir muammoni hal qilishdan boshqasiga o' tkazish usuli.\n"
            },
            {
                "correct": True
            }
        ],
        "option2": [
            {
                "type": "text",
                "content": " Har bir yangi vazifaga noldan modellarni tayyorlash usuli.\n"
            },
            {
                "correct": False
            }
        ],
        "option3": [
            {
                "type": "text",
                "content": " Matnli ma'lumotlarni tasvirlash uchun grafiklardan foydalanadigan texnika."
            },
            {
                "type": "image",
                "content": [
                    "media/image2.png"
                ]
            },
            {
                "correct": False
            }
        ],
        "option4": [
            {
                "type": "text",
                "content": " Matnlarni tasniflash algoritmi.\n"
            },
            {
                "correct": False
            }
        ]
    },
    {
        "id": 116,
        "rate": 1,
        "question": [
            {
                "type": "text",
                "content": " NLPdagi ``Sequence-to-Sequence'' (Seq2Seq) modeli nima?\n"
            }
        ],
        "option1": [
            {
                "type": "text",
                "content": " Kirishlar ketma-ketligida "
            },
            {
                "type": "image",
                "content": [
                    "media/image2.png"
                ]
            },
            {
                "type": "text",
                "content": "ishlaydigan va chiqishlar ketma-ketligini hosil qiluvchi "
            },
            {
                "type": "image",
                "content": [
                    "media/image2.png"
                ]
            },
            {
                "type": "text",
                "content": "model.\n"
            },
            {
                "correct": True
            }
        ],
        "option2": [
            {
                "type": "text",
                "content": " Kirish sifatida ma'lumotlar ketma-ketligini oladigan va bitta chiqishni qaytaruvchi model.\n"
            },
            {
                "correct": False
            }
        ],
        "option3": [
            {
                "type": "text",
                "content": " Gaplarning sintaktik tuzilishini ajratib olish texnikasi.\n"
            },
            {
                "correct": False
            }
        ],
        "option4": [
            {
                "type": "text",
                "content": " Matndagi tayanch iboralarni ajratib ko`rsatish algoritmi.\n"
            },
            {
                "correct": False
            }
        ]
    }
]