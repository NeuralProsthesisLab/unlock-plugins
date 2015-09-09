__author__ = 'Graham Voysey'
from plugins.plugin_one.testplugin import TestPlugin
import logging


class PluginOne(TestPlugin):
    def test(self):
        logging.log(logging.INFO,"Plugin registration functional ...")
