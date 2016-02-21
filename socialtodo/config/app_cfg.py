# -*- coding: utf-8 -*-
"""
Global configuration file for TG2-specific settings in socialtodo2.

This file complements development/deployment.ini.

Please note that **all the argument values are strings**. If you want to
convert them into boolean, for example, you should use the
:func:`paste.deploy.converters.asbool` function, as in::
    
    from paste.deploy.converters import asbool
    setting = asbool(global_conf.get('the_setting'))
 
"""

from tg.configuration import AppConfig

import socialtodo
from socialtodo import model
from socialtodo.lib import app_globals, helpers 

base_config = AppConfig()
base_config.renderers = []
base_config.prefer_toscawidgets2 = True

base_config.package = socialtodo

#Enable json in expose
base_config.renderers.append('json')

#Enable genshi in expose to have a lingua franca for extensions and pluggable apps
#you can remove this if you don't plan to use it.
base_config.renderers.append('genshi')

#Set the default renderer
base_config.default_renderer = 'jinja'
base_config.renderers.append('jinja')
base_config.jinja_extensions = ['jinja2.ext.with_']
#Configure the base Ming Setup
base_config.use_ming = True
base_config.use_sqlalchemy=False
base_config.use_transaction_manager=False
#base_config.serve_static = True
#base_config.paths['static_files'] = 'public'