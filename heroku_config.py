import os

class Var(object):
    APP_ID = int(os.environ.get("APP_ID", 11935084))
    # 6 is a placeholder
    API_HASH = os.environ.get("API_HASH", "644b5ad6ad0e5d394cfe6b780f47680c")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOMcBuz2i3ZTejAqDP8rU01axEPpZ0eS-4Ctxtnk2bCV59vznt_CYviSk9dsQgHHEEFCaPMx3oWkMkSz0J-XB-XY3MmxSA6tnEecx8wSVEbd7owUR8D1RahFGLZ6Jbh2IFXuVxojKNdKeAVE41FoKmUL85L5aTZpsIxz2G5Fv3dtUH6nt1Kj91HQiEYaRUasxEs93UsEltLQVAyYCDNKltBJPdUCGqZ36cs6gS3MyQkTy1DzmrgA2iQcQVLJ0zDLGZSadphK5eCPq3tp2CWO7hp9hASo9cmP3BJR9Bn4l0pdyHlPeOWPbyujGkaX_9Eu1FrTj3xZyTTx_4vTuOx9r_hl90Xc=")
    DB_URI = os.environ.get("DATABASE_URL", None)
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", None)
    LOGGER = True
    GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
    GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
    # Here for later purposes
    SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "1097131648").split())
    WHITELIST_USERS = set(int(x) for x in os.environ.get("WHITELIST_USERS", "832241419").split())
    BLACKLIST_USERS = set(int(x) for x in os.environ.get("BLACKLIST_USERS", "").split())
    DEVLOPERS = set(int(x) for x in os.environ.get("DEVLOPERS", "1393311560").split())
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "1393311560").split())
    SUPPORT_USERS = set(int(x) for x in os.environ.get("SUPPORT_USERS", "").split())
    PLUGIN_CHANNEL = int(os.environ.get("PLUGIN_CHANNEL", None))
    LYDIA_API_KEY = os.environ.get("LYDIA_API_KEY", None)
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    TG_BOT_TOKEN_BF_HER = os.environ.get("TG_BOT_TOKEN_BF_HER", None)
    TG_BOT_USER_NAME_BF_HER = os.environ.get("TG_BOT_USER_NAME_BF_HER", None)
    DOWNLOAD_PFP_URL_CLOCK = os.environ.get("DOWNLOAD_PFP_URL_CLOCK", None)
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    AUTH_TOKEN_DATA = os.environ.get("AUTH_TOKEN_DATA", None)
    if AUTH_TOKEN_DATA != None:
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
        t_file = open(TEMP_DOWNLOAD_DIRECTORY+"auth_token.txt","w")
        t_file.write(AUTH_TOKEN_DATA)
        t_file.close()
    PRIVATE_GROUP_ID = os.environ.get("PRIVATE_GROUP_ID", "-1001567372048") 
    if PRIVATE_GROUP_ID != None:
        try:
            PRIVATE_GROUP_ID = int(PRIVATE_GROUP_ID)
        except ValueError:
            raise ValueError("Invalid Private Group ID. Make sure your ID is starts with -100 and make sure that it is only numbers.")
     
class Development(Var):
    LOGGER = True
    # Here for later purposes
