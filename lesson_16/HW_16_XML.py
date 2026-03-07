import logging
import xml.etree.ElementTree as ET

logging.basicConfig(
    level=logging.DEBUG,
    filename='xml_validation.log',
    format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


def find_incoming(filepath, group_number):
    root = ET.parse(filepath).getroot()

    for group in root.findall('group'):
        if int(group.find('number').text) == group_number:
            incoming = group.find('timingExbytes/incoming')
            logger.info("Group %d — incoming: %s", group_number, incoming.text)
            return incoming.text

find_incoming('groups.xml', 2)