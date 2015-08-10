__author__ = 'Graham Voysey'
# ref https://web.archive.org/web/20130731202108/http://lateral.netmanagers.com.ar/weblog/posts/BB923.html for plugin stuff.
import logging
from yapsy.PluginManager import PluginManager
from plugins.drivers.idaqplugin import IDAQPlugin
from plugins.apps.iappplugin import IAppPlugin
from plugins.plugin_one.itestplugin import ITestPlugin
from plugins.decoders.idecoderplugin import IDecoderPlugin


logging.basicConfig(level=logging.DEBUG)


def main():
    # Load the plugins from the plugin directory.
    manager = ConfigurePluginManager()

    # Load the Test Plugin
    manager = ActivatePluginsOfCategory(manager)

    # load at least one app, one decoder, and one driver.
    # defaults: app - hello-world or dashboard (todo: when written)
    #           decoder - keyboard
    #           driver -  none
    # todo: non-default values should come from where the plugin directory root comes from -- some command line input or config file.

    # if(AreAppsConfigured() is False):
    #    manager.activatePluginByName("HelloWorld","App")
    # if(AreDecodersConfigured() is False):
    #    manager.activatePluginByName("keyboard", "Decoder")





def ConfigurePluginManager(categories=None, pluginLocation=None):
    if categories is None:
        categories = dict(Test=ITestPlugin, DAQ=IDAQPlugin, App=IAppPlugin, Decoder=IDecoderPlugin)
    if pluginLocation is None:
        pluginLocation = ["plugins"]
    manager = PluginManager()
    # todo: plugin directory and categories should be set some other way (command line arg parsing?)
    manager.setPluginPlaces(pluginLocation)
    manager.setCategoriesFilter(categories)
    manager.collectPlugins()
    return manager


def ActivatePluginsOfCategory(manager, pluginCategory=None):
    """
    This is the pattern for locating all plugins of a specific type, iterating over them, and (normally) activating them.

    :param manager: manager is the plugin manager object
    :return: null.
    """
    # todo: if we're just running the test plugin, we know what its methods are, so we can just call them directly.
    if pluginCategory is None:
        pluginCategory = "Test"

        for plugin in manager.getPluginsOfCategory(pluginCategory):
            manager.activatePluginByName(plugin.name)
            plugin.plugin_object.print_status()
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
