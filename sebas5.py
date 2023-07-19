# before 0.15.0
from ruamel.yaml import YAML

# after 0.15.0
from ruamel import yaml

import ruamel

from http.server import BaseHTTPRequestHandler
import urllib.parse

class GetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        tainted = urlparse.urlparse(self.path).query
   
        if ruamel.yaml.version_info < (0, 15):
            # ok: tainted-ruamel
            data = yaml.safe_load(istream)
            yaml.safe_dump(data, ostream)
        else:
            yml = ruamel.yaml.YAML()
            # ok: tainted-ruamel
	    	data = yml.load(istream)
            yml.dump(data, ostream)


        if ruamel.yaml.version_info < (0, 15):
            # ok: tainted-ruamel
            data = yaml.load(istream, Loader=yaml.CSafeLoader)
            yaml.round_trip_dump(data, ostream, width=1000, explicit_start=True)
        else:
            yml = ruamel.yaml.YAML(typ='safe')
            # ok: tainted-ruamel
            data = yml.load(istream)
            ymlo = ruamel.yaml.YAML()   # or yaml.YAML(typ='rt')
            ymlo.width = 1000
            ymlo.explicit_start = True
            ymlo.dump(data, ostream)

        
        # before 0.15.0

        # ruleid: tainted-ruamel
        ruamel.yaml.load(tainted)
        # ruleid: tainted-ruamel
        ruamel.yaml.load_all(tainted)
        # ruleid: tainted-ruamel
        ruamel.yaml.round_trip_load(tainted)

        # ok: tainted-ruamel
        ruamel.yaml.safe_load(tainted)

        # ok: tainted-ruamel
        ruamel.yaml.load(s)
        # ok: tainted-ruamel
        ruamel.yaml.load_all(s)
        # ok: tainted-ruamel
        ruamel.yaml.round_trip_load(s)

        # after 0.15.0

        yml = ruamel.yaml.YAML(typ='unsafe')
        # ruleid: tainted-ruamel
        data = yml.load(tainted)
        # ok: tainted-ruamel
        data = yml.load(s)

        yml = ruamel.yaml.YAML(typ='safe')
        # ok: tainted-ruamel 
        data = yml.load(tainted)

        # The default loader (typ='rt') is a direct derivative of the safe loader
        yml = ruamel.yaml.YAML(typ='rt')
        # ok: tainted-ruamel 
        data = yml.load(tainted)

        yml = ruamel.yaml.YAML()
        # ok: tainted-ruamel 
        data = yml.load(tainted)


