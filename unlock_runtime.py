__author__ = 'Graham Voysey'
# ref https://web.archive.org/web/20130731202108/http://lateral.netmanagers.com.ar/weblog/posts/BB923.html
import logging
from yapsy.PluginManager import PluginManager
from plugins.drivers.idaqplugin import IDAQPlugin
from plugins.apps.iappplugin import IAppPlugin
from plugins.plugin_one.itestplugin import ITestPlugin

logging.basicConfig(level=logging.DEBUG)


def main():
    # Load the plugins from the plugin directory.
    manager = PluginManager()
    manager.setPluginPlaces(["plugins"]) #todo: plugin directory set some other way (command line arg parsing)
    manager.setCategoriesFilter({
        "Test": ITestPlugin,
        "DAQ": IDAQPlugin,
        "App": IAppPlugin,
    })
    manager.collectPlugins()

    #load the test plugin
    for pluginInfo in manager.getPluginsOfCategory("Test"):
        manager.activatePluginByName(pluginInfo.name)
        pluginInfo.plugin_object.print_name()
        pluginInfo.plugin_object.print_status()

    #load the

if __name__ == "__main__":
    main()
