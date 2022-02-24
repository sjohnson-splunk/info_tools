
import glob,os,re,sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from splunklib.searchcommands import \
    dispatch, GeneratingCommand, Configuration, Option, validators

@Configuration(type='reporting')

class LookupInfo(GeneratingCommand):
	
	def generate(self):

		userdir = os.sep.join([os.environ['SPLUNK_HOME'], "etc", "users", "**"])
		for name in glob.glob(userdir, recursive=True):
			if os.path.isfile(name):
				info=os.stat(name)
				size=info.st_size
				mtime=int(info.st_mtime)
				m=re.search(r"users[\/\\]([^\/\\]+)[\/\\]([^\/\\]+)[\/\\](.+)$",name)
				if m is not None:
					if m.lastindex==3:
						user=m.group(1)
						app=m.group(2)
						fileobject=m.group(3)
						yield {'user': user, 'app': app, 'fileobject': fileobject, 'size': info.st_size, 'mtime': mtime}
					else:
						continue

dispatch(LookupInfo, sys.argv, sys.stdin, sys.stdout, __name__)
