#!/usr/bin/env python
import argparse
import sys
from lxml import etree
from requests import get
from StringIO import StringIO


def get_url(url, debug=False):
    print "starting to parse url:", url
    http_get = get(url)
    if http_get.status_code == 200:
        print "http get request ok\n"
        if debug:
            print http_get.text
    else:
        if debug:
            print http_get.text

        sys.exit("Ops failed to get url!")

    parser = etree.HTMLParser()
    tree = etree.parse(
        StringIO(http_get.text),
        parser
    )
    for element in tree.iter():
        epath = tree.getelementpath(element)
        edepth = epath.count('/')
        indent = ""
        count = 0
        while count < edepth:
            indent += "  "
            count += 1

        print "%s[%s]" % (indent, element.tag)

if __name__ == "__main__":
    description = """
    find all html elements and print out a tree showing the
    html element. in a 2-char indented hierarchical ASCII
    representation tree"""
    parser = argparse.ArgumentParser(description)
    parser.add_argument('-u', '--url', help='url', required=True)
    parser.add_argument('-d', '--debug', help='debug mode', action='store_true')
    args = parser.parse_args()
    get_url(args.url, debug=args.debug)
