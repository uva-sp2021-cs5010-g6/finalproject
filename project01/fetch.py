
import os
import sys

import requests
import tempfile
import zipfile


class Fetcher():
    def __init__(self, uris: str="uri.txt", base: str="dataset", feedback: bool=True):
        self._uris = self.__parse_file(uris)
        self._base = base
        self._feedback = feedback

    def __parse_file(self, uri_file):
        ret = list()
        with open(uri_file, "r") as uris:
            for uri in uris:
                if not uri.startswith("#"):
                    ret.append(uri.rstrip())
        return ret

    def add_uri(self, uri: str):
        self._uris.append(uri)
        return self._uris

    def fetch(self, feedback: bool=None, out: str=None) -> None:
        feedback = feedback if feedback is not None else self._feedback
        out = out if out is not None else self._base
        with tempfile.TemporaryDirectory() as temp_dir:
            for uri in self._uris:
                filename = os.path.basename(uri)
                # Use stream to download very large files
                resp = requests.get(uri, stream=True)
                resp.raise_for_status()
                uri_size = resp.headers.get('content-length') # Get the size of the download
                if feedback:
                    print("Downloading {}".format(uri))
                with open(os.path.join(temp_dir,filename), "wb") as zipf:
                    tracker = 0
                    for block in resp.iter_content(4096):
                        tracker += len(block)
                        zipf.write(block)
                        if feedback:
                            done = int( 50 * tracker / int(uri_size)) # Total Progress
                            # We need an unbuffered printer here...
                            sys.stdout.write("\r[%s%s] %s/100" % ('=' * done, ' ' * (50-done), done*2) )    
                            sys.stdout.flush()
                    print("")
            for root, dirs, files in os.walk(temp_dir):
                for zipf in files:
                    temp_zip = os.path.join(root,zipf)
                    with zipfile.ZipFile(temp_zip, "r") as zf:
                        if feedback:
                            print("Extracting {}".format(zipf))
                        stripped_name, ext = os.path.splitext(temp_zip)
                        basen = os.path.basename(stripped_name)
                        zf.extractall(os.path.join(out, basen))


if __name__ == "__main__":
    collector = Fetcher()
    collector.fetch()

