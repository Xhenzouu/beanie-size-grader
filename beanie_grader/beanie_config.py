SIZES = ['XS', 'S', 'M', 'L', 'XL']

MEASUREMENTS = {
    'Crown Circumference (cm)': {
        'base': 56,
        'offsets': [-8, -4, 0, 4, 8],
    },
    'Height / Length (cm)': {
        'base': 22,
        'offsets': [-2, -1, 0, 1, 2],
    },
    'Brim Width (cm)': {
        'base': 8,
        'offsets': [0, 0, 0, 0.5, 1],
    },
    'Gauge (stitches per 10cm)': {
        'base': 22,
        'offsets': [0, 0, 0, 0, 0],
    },
}

PRODUCT_CONFIG = {
    "name": "beanie",
    "sizes": SIZES,
    "measurements": MEASUREMENTS,
}
