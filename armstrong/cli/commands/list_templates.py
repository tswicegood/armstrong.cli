from pkg_resources import iter_entry_points
import os

from .init import ENTRY_POINT


def command():
    # TODO: make this verify that there's a manifest.json present
    # TODO: make this display manifest.json's description along side template names
    print "The following templates are available:"
    for entry_point in iter_entry_points(ENTRY_POINT):
        print "    %s" % entry_point.name
