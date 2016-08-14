# -*- coding: utf-8 -*- #
"""
NoJekyll
=============

This plugin add a *.nojekyll* file to the output root.
"""

__version__ = '1.0.0'

import os
from pelican import signals

def add_nojekyll(p):
    """ 
    :param p: pelican instance
    :return: None
    """

    nojekyll_path = os.path.join(p.output_path, '.nojekyll')
    content = ' '
    with open(nojekyll_path, 'w') as f:
        f.write(content)    

def register():
    signals.finalized.connect(add_nojekyll)
