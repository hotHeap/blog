import os
from app import create_app

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
application = create_app('config.cfg')

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8089)
