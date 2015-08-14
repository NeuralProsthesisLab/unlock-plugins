__author__ = 'Graham Voysey'
from plugins.plugin_one.itestplugin import ITestPlugin
import logging


class PluginOne(ITestPlugin):
    def test(self):
        logging.log(logging.INFO,"Plugin registration functional ...")
