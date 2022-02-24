
import glob,os,re,sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from splunklib.searchcommands import \
    dispatch, GeneratingCommand, Configuration, Option, validators

@Configuration(type='reporting')

class LookupInfo(GeneratingCommand):
	
	def generate(self):

		lookups = os.sep.join([os.environ['SPLUNK_HOME'], "etc", "apps", "*", "lookups", "*"])
		for name in glob.glob(lookups):
			info=os.stat(name)
			m=re.search(r"apps.([^/\\]+).lookups.(\S+)",name)
			app=m.group(1)
			lookup_name=m.group(2)
			mtime=int(info.st_mtime)
			yield {'app': app, 'name': lookup_name, 'size': info.st_size, 'mtime': mtime}

dispatch(LookupInfo, sys.argv, sys.stdin, sys.stdout, __name__)