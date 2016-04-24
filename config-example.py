DEBUG = True # REMOVE BEFORE PRODUCTION

# Database login String
SQLALCHEMY_DATABASE_URI = "mysql://username:password@localhost/database"

# Other DB Settings
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Form Stuff
WTF_CSRF_ENABLED = True
SECRET_KEY = 'make-me-special'

# Session Management Stuff
REMEMBER_COOKIE_NAME = "make-a-token-name"