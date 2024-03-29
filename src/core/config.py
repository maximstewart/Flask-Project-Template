# Python imports
import os
import secrets
import json
from datetime import timedelta

# Lib imports

# Apoplication imports



# This path is submitted as the redirect URI in certain code flows.
# Change localhost%3A6969 to different port accordingly or change to your domain.
REDIRECT_LINK = "http%3A%2F%2Flocalhost%3A6969%2F"


class FileGroups:
    videos = ('.mkv', '.avi', '.flv', '.mov', '.m4v', '.mpg', '.wmv', '.mpeg', '.mp4', '.webm')
    office = ('.doc', '.docx', '.xls', '.xlsx', '.xlt', '.xltx', '.xlm', '.ppt', 'pptx', '.pps', '.ppsx', '.odt', '.rtf')
    images = ('.png', '.jpg', '.jpeg', '.gif', '.ico', '.tga', '.webp')
    text   = ('.txt', '.text', '.sh', '.cfg', '.conf')
    music  = ('.psf', '.mp3', '.ogg', '.flac', '.m4a')
    pdf    = ('.pdf')


class Config(object):
    TITLE      = app_name
    DEBUG      = False
    TESTING    = False
    SECRET_KEY = secrets.token_hex(32)

    PERMANENT_SESSION_LIFETIME     = timedelta(days = 7).total_seconds()
    SQLALCHEMY_DATABASE_URI        = "sqlite:///static/db/database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    REGISTER_DISABLED              = False
    LOGIN_DISABLED                 = False
    LOGIN_PATH                     = "FLASK_LOGIN"  # Value can be OIDC or FLASK_LOGIN
    OIDC_TOKEN_TYPE_HINT           = 'access_token'
    APP_REDIRECT_URI               = REDIRECT_LINK
    OIDC_CLIENT_SECRETS            = f'{ROOT_FILE_PTH}/client_secrets.json'
    OIDC_ID_TOKEN_COOKIE_SECURE    = True
    OIDC_REQUIRE_VERIFIED_EMAIL    = True
    OIDC_USER_INFO_ENABLED         = True
    OIDC_VALID_ISSUERS   = [
                            'http://localhost:8080/auth/realms/apps',
                            'https://localhost:443/auth/realms/apps'
                        ]

    STATIC_FPTH    = f"{ROOT_FILE_PTH}/static"
    FILEGROUPS     = FileGroups
    VEXTENSION     = FileGroups.videos
    OEXTENSION     = FileGroups.office
    IEXTENSION     = FileGroups.images
    TEXTENSION     = FileGroups.text
    MEXTENSION     = FileGroups.music
    PEXTENSION     = FileGroups.pdf




class ProductionConfig(Config):
    pass



class DevelopmentConfig(Config):
    DEBUG = True
    OIDC_ID_TOKEN_COOKIE_SECURE = False
    OIDC_REQUIRE_VERIFIED_EMAIL = False


class TestingConfig(Config):
    TESTING = True
