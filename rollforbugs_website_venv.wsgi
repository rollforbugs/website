import os, sys, site

# Add some stuff where we are
site_root = '/var/www/rollforbugs_website'
venv_root = site_root + '/env'
sys.path.append(site_root)
sys.path.append(venv_root)
site.addsitedir(venv_root + '/lib/python3.4/site-packages')

# Activate virtualenv
activate_env = venv_root + '/bin/activate_this.py'
with open(activate_env) as ae:
	exec(ae.read(), dict(__file__=activate_env))

from rollforbugs_website import app as application
