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
    manager = PluginManager()
    manager.setPluginPlaces(["plugins"])  # todo: plugin directory should be set some other way (command line arg parsing?)
    manager.setCategoriesFilter(dict(Test=ITestPlugin, DAQ=IDAQPlugin, App=IAppPlugin, Decoder=IDecoderPlugin))
    manager.collectPlugins()

    # load the test plugin(s).
    for plugin in manager.getPluginsOfCategory("Test"):
        manager.activatePluginByName(plugin.name)
        plugin.plugin_object.print_status()

    # load at least one app, one decoder, and one driver.
    # defaults: app - hello-world or dashboard (todo: when written)
    #           decoder - keyboard
    #           driver -  none
    # todo: non-default values should come from where the plugin directory root comes from -- some command line input or config file.

    #if(AreAppsConfigured() is False):
    #    manager.activatePluginByName("HelloWorld","App")
    #if(AreDecodersConfigured() is False):
    #    manager.activatePluginByName("keyboard", "Decoder")


def AreAppsConfigured():
    return False

def AreDecodersConfigured():
    return False


if __name__ == "__main__":
    main()
