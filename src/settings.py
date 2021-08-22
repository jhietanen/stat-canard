"""
Settings for Stat Canard project src

Content:
1. Paths
2. API Query Settings

"""
import os
from pathlib import Path

### PATHS ###
# Configure Project Dir
PROJECT_DIR = Path(__file__).resolve().parents[1]

# Configure subdirectories
SUB_DIRS = {
    'DATA': PROJECT_DIR / 'data',
    'DOCS': PROJECT_DIR / 'docs',
    'MODELS': PROJECT_DIR / 'models',
    'NOTEBOOKS': PROJECT_DIR / 'notebooks',
    'REFERENCES': PROJECT_DIR / 'references',
    'REPORTS': PROJECT_DIR / 'reports',
    'TESTS': PROJECT_DIR / 'tests',
}

# Configure DATA subdirectories
DATA_PATHS = {
    'EXTERNAL': SUB_DIRS['DATA'] / 'external',
    'INTERIM': SUB_DIRS['DATA'] / 'interim',
    'PROCESSED': SUB_DIRS['DATA'] / 'processed',
    'RAW': SUB_DIRS['DATA'] / 'raw',
}

# Configure REFERENCES subdirectories
REFERENCES_PATHS = {
    'DATABASES': SUB_DIRS['REFERENCES'] / 'databases',
    'IMG': SUB_DIRS['REFERENCES'] / 'img',
}

# Configure REPORTS subdirectories
REPORT_PATHS = {
    'FIGURES': SUB_DIRS['REPORTS'] / 'figures'
}

### API QUERY SETTINGS ###
DATA_QUERIES = {
    'statfin_ksyyt_pxt_11bs.px': {
        'URL': 'http://pxnet2.stat.fi/PXWeb/api/v1/en/StatFin/ter/ksyyt/statfin_ksyyt_pxt_11bs.px',
        'JSON_QUERY': REFERENCES_PATHS['DATABASES'] / 'StatFin' / 'statfin_ksyyt_pxt_11bs.px' / 'json_query.json'
    },
    'statfin_khki_pxt_111k.px': {
        'URL': 'http://pxnet2.stat.fi/PXWeb/api/v1/en/StatFin/ymp/khki/statfin_khki_pxt_111k.px',
        'JSON_QUERY': REFERENCES_PATHS['DATABASES'] / 'StatFin' / 'statfin_khki_pxt_111k.px' / 'json_query.json'
    },
    'statfin_vaerak_pxt_11rd.px': {
        'URL': 'https://pxnet2.stat.fi:443/PXWeb/api/v1/en/StatFin/vrm/vaerak/statfin_vaerak_pxt_11rd.px',
        'JSON_QUERY': REFERENCES_PATHS['DATABASES'] / 'StatFin' / 'statfin_vaerak_pxt_11rd.px' / 'json_query.json'
    },
    'statfin_kihi_pxt_11j9.px': {
        'URL': 'https://pxnet2.stat.fi:443/PXWeb/api/v1/en/StatFin/asu/kihi/nj/statfin_kihi_pxt_11j9.px',
        'JSON_QUERY': REFERENCES_PATHS['DATABASES'] / 'StatFin' / 'statfin_kihi_pxt_11j9.px' / 'json_query.json'
    }
}
