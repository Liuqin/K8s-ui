from cryptography.fernet import Fernet
import base64, os, logging, traceback
from django.conf import settings
from uuid import uuid4
import datetime


# encrypt text
def encrypt(txt):
    try:
        txt = str(txt)
        cipher_suite = Fernet(settings.ENCRYPTION_KEY)
        encrypted_text = cipher_suite.encrypt(txt.encode('ascii'))
        encrypted_text = base64.urlsafe_b64encode(encrypted_text).decode("ascii")
        return encrypted_text
    except Exception as e:
        logging.getLogger("error_logger").error(traceback.format_exc())
        return None


# decrypt text
def decrypt(txt):
    try:
        txt = base64.urlsafe_b64decode(txt)
        cipher_suite = Fernet(settings.ENCRYPTION_KEY)
        decoded_text = cipher_suite.decrypt(txt).decode("ascii")
        return decoded_text
    except Exception as e:
        logging.getLogger("error_logger").error(traceback.format_exc())
        return None


# change file name when uploaded
def file_handler(instance, filename):
    upload_to = settings.UPLOADS['CONFIG_FILES']
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid4().hex, ext)
    return os.path.join(upload_to, filename)


def json_serializer(value):
    if isinstance(value, datetime.date):
        return dict(year=value.year, month=value.month, day=value.day)
    else:
        return value.__dict__
