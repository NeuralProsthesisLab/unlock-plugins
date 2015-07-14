__author__ = 'Graham Voysey'
# ref https://web.archive.org/web/20130731202108/http://lateral.netmanagers.com.ar/weblog/posts/BB923.html for plugin stuff.
import logging
from yapsy.PluginManager import PluginManager
from plugins.drivers.idaqplugin import IDAQPlugin
from plugins.apps.iappplugin import IAppPlugin
from plugins.plugin_one.itestplugin import ITestPlugin

logging.basicConfig(level=logging.DEBUG)


def main():
    # Load the plugins from the plugin directory.
    manager = PluginManager()
    manager.setPluginPlaces(["plugins"]) # todo: plugin directory should be set some other way (command line arg parsing?)
    manager.setCategoriesFilter({
        "Test": ITestPlugin,
        "DAQ": IDAQPlugin,
        "App": IAppPlugin,
    })
    manager.collectPlugins()

    # load the test plugin(s).
    for plugin in manager.getPluginsOfCategory("Test"):
        manager.activatePluginByName(plugin.name)
        plugin.plugin_object.print_status()

    # load at least one app, one decoder, and one driver.
    # defaults: app- hello-world or dashboard (todo: when written)
    #           decoder- keyboard
    #           driver-  none



if __name__ == "__main__":
    main()