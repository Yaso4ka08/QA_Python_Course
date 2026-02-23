import json
import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename='validation_errors.log',
    encoding='utf-8'
)
logger = logging.getLogger(__name__)

json_files = ['localizations_en.json', 'localizations_ru.json', 'login.json', 'swagger.json']

def validate_json_files(files):
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            try:
                json.load(f)
            except json.JSONDecodeError as e:
                logger.error("Non-valid JSON: '%s' — %s", filepath, e)

validate_json_files(json_files)