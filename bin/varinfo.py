
import glob,os,sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from splunklib.searchcommands import \
    dispatch, GeneratingCommand, Configuration, Option, validators

@Configuration(type='reporting')

class LookupInfo(GeneratingCommand):

	subdir = Option(require=False)

	def generate(self):
		if self.subdir:
			if ".." in self.subdir:
				sdir="zyxw"
			else:
				sdir=self.subdir
		else:
			sdir="*"
		vardir = os.sep.join([os.environ['SPLUNK_HOME'], "var", sdir, "**"])
		for name in glob.glob(vardir, recursive=True):
			if os.path.isfile(name):
				info=os.stat(name)
				size=info.st_size
				mtime=int(info.st_mtime)
				yield {'file': name, 'size': info.st_size, 'mtime': mtime}

dispatch(LookupInfo, sys.argv, sys.stdin, sys.stdout, __name__)
