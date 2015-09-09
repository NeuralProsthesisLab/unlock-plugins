__author__ = 'Graham Voysey'
# ref https://web.archive.org/web/20130731202108/http://lateral.netmanagers.com.ar/weblog/posts/BB923.html for plugin stuff.
import logging
from yapsy.PluginManager import PluginManager
from plugins.drivers.daqplugin import DAQPlugin
from plugins.apps.appplugin import AppPlugin
from plugins.plugin_one.testplugin import TestPlugin
from plugins.decoders.decoderplugin import DecoderPlugin

##turn on to see yapsy plugin registration messages
#logging.basicConfig(level=logging.DEBUG)


def main():
    # Load the plugins from the plugin directory.
    manager = ConfigurePluginManager()

    # Load the Test Plugin
    manager = ActivatePlugins(manager,["Test", "App"])

    # load at least one app, one decoder, and one driver.
    # defaults: app - hello-world or dashboard (todo: when written)
    #           decoder - keyboard
    #           driver -  none
    # todo: non-default values should come from where the plugin directory root comes from -- some command line input or config file.

    # if(AreAppsConfigured() is False):
    #    manager.activatePluginByName("HelloWorld","App")
    # if(AreDecodersConfigured() is False):
    #    manager.activatePluginByName("keyboard", "Decoder")
    logging.log(logging.INFO,"unlock exiting ...")


def ConfigurePluginManager(categories=None, pluginLocation=None):
    if categories is None:
        categories = dict(Test=TestPlugin, DAQ=DAQPlugin, App=AppPlugin, Decoder=DecoderPlugin)
    if pluginLocation is None:
        pluginLocation = ["plugins"]
    manager = PluginManager()
    # todo: plugin directory and categories should be set some other way (command line arg parsing?)
    manager.setPluginPlaces(pluginLocation)
    manager.setCategoriesFilter(categories)
    manager.collectPlugins()
    return manager


def ActivatePlugins(manager, categories=[]):
    """
    This is the pattern for locating all plugins of a specific type, iterating over them, and (normally) activating them.

    :param manager: manager is the plugin manager object
    :return: null.
    """

    for category in categories:
        if category == "Test":
            for plugin in manager.getPluginsOfCategory(category):
                manager.activatePluginByName(plugin.name)
                plugin.plugin_object.test()
        if category == "App":
            # todo this logic will change substantially once Dashboard exists.  (and become "load dashboard", and cache other names)
            for plugin in manager.getPluginsOfCategory(category):
                manager.activatePluginByName(plugin.name)
                plugin.plugin_object.configure()
                plugin.plugin_object.start()

    return manager

def AreAppsConfigured():
    """
    Here we check to see if there are any apps that were specifically requested
    to be activated from some as-yet-undetermined argument/config parsing
    :return: a boolean
    """
    return False


def AreDecodersConfigured():
    """
    Here we check to see which decoders we need.
    :return: a boolean
    """
    return False


if __name__ == "__main__":
    main()
