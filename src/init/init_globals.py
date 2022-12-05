import os

class PATHS:
	SEP = os.path.sep
	CWD = os.getcwd()
	ASSETS = 'assets'
	STORAGE = 'storage'
	WEBDRIVER_DIR = ASSETS + SEP + 'webdriver'
	PROXY_TEMPLATE_DIR = ASSETS + SEP + 'proxy_template'
	LOG_FILE = CWD + SEP + STORAGE + SEP + 'logs'
	CHROME_DRIVER = CWD + SEP + WEBDRIVER_DIR + SEP + 'chromedriver.exe'
	RESOURCES_FILE = CWD + SEP + ASSETS + SEP + 'resources.csv'
	MANIFEST_TEMPLATE_FILE = CWD + SEP + PROXY_TEMPLATE_DIR + SEP + 'manifests.json'
	SCRIPT_TEMPLATE_FILE = CWD + SEP + PROXY_TEMPLATE_DIR + SEP + 'background.js'

class ERRORS:
	UNKNOWN_ERROR = -1
	EMAIL_ERROR = 1
	PASS_ERROR = 2
	PROXY_ERROR = 3
	CAPTCHA_ERROR = 4
	BLOCKED_ACC_ERROR = 5
	VERIFICATION_ERROR = 6