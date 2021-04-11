# -*- coding: utf-8 -*-

"""Data fetching utility for USDA datasets.

This module provides the primary support functions for downloading datasets from
a text file.  Each line in the text file is expected to be a complete URL.  Lines
that begin with '#' are ignored.

Example:

    This module can be run directly with the following arguments:
    
    $ python -m project01.fetch path/to/uri.txt output/dir

    The URIs listed in the file path/to/uri.txt will be Files will be saved to output/dir.

    If no arguments are specified, they defaults (./uri.txt, and ./dataset)
"""

import os
import sys

import requests
import tempfile
import zipfile


class Fetcher():
    def __init__(self, uris: str="uri.txt", base: str="dataset", feedback: bool=True):
        """Creates a new fetcher method configured with the arguments specified.

        Args:
            uris (str): A path to a URI file for the class to parse and download the
                datasetsfrom
           base (str): A path to a directory to write the resulting files to.
           feedback (bool): Specifies if user feedback during the download process
               should occur.  When true, text is written to stdout.
        """
        self._uris = self.__parse_file(uris)
        self._base = base
        self._feedback = feedback

    def __parse_file(self, uri_file):
        """Establishs a link of URIs to download.
        
        Args:
            uri_file (str): the path to the file to parse.
        Returns:
            list(str): The effective listing of URIs from the uri_file.
        """
        ret = list()
        with open(uri_file, "r") as uris:
            for uri in uris:
                if not uri.startswith("#"):
                    ret.append(uri.rstrip())
        return ret

    def add_uri(self, uri: str):
        """Adds a URI to the list of download links after creation of the object.

        Args:
            uri (str): A fully qualified string to fetch to artifact from
        Returns:
            list(str): A listing of all URIs the instance is currently configured
                to support.
        """
        self._uris.append(uri)
        return self._uris

    def fetch(self, feedback: bool=None, out: str=None) -> None:
        """Downloads all URIs the the current object and extracts them to the class's directory.

        Args:
            feedback(bool): Overide the classes feedback state.  If True, the download
                progress will be echoed to screen.
            out(str): Overrides the classes output director.  If specified, the downloaded
                files will be written to the directory that has been specified.
        Returns:
            str: The output path of the extracted files.
        """
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
        return out


def cli():
    """Creates a CLI parser

    Returns:
        argparse.ArgumentParser: An Argument Parser configured to support the
            fetcher class.
    """
    import argparse
    parser = argparse.ArgumentParser("Fetch datasets")

    parser.add_argument("urifile", nargs="?",
                        default="uri.txt",
                        help="Path to file containing URIs to download.")
    parser.add_argument("outdir", nargs="?",
                        default="dataset",
                        help="Path to a directory to output the files.")
    return parser

def main(uri_file, out):
    collector = Fetcher(uris=uri_file, base=out)
    collector.fetch()


if __name__ == "__main__":
    config = cli().parse_args()
    main(uri_file=config.urifile, out=config.outdir)
