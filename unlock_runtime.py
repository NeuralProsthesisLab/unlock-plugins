__author__ = 'Graham Voysey'
# ref https://web.archive.org/web/20130731202108/http://lateral.netmanagers.com.ar/weblog/posts/BB923.html
from yapsy.PluginManager import PluginManager
from plugins.drivers.idaqplugin import IDAQPlugin
from plugins.apps.iappplugin import IAppPlugin
from plugins.plugin_one.itestplugin import ITestPlugin
from plugins.plugin_one import plugin_one
import core
import logging

logging.basicConfig(level=logging.DEBUG)


def main():
    # Load the plugins from the plugin directory.
    manager = PluginManager() #categories_filter={"testers": PluginOne}
    manager.setPluginPlaces(["plugins"])
    manager.setCategoriesFilter({
        "Test": ITestPlugin,
        "DAQ": IDAQPlugin,
        "App": IAppPlugin,
    })
    manager.collectPlugins()

    #Loop round the plugins and print their names.
    #for plugin in manager.getAllPlugins():
    #    manager.activatePluginByName(plugin.name)
    #    logging.debug("UNLOCK found plugin: " + plugin.name + ", with description: " +plugin.description);

    #load the test plugin
    for pluginInfo in manager.getPluginsOfCategory("Test"):
        manager.activatePluginByName(pluginInfo.name)
        pluginInfo.plugin_object.print_name()

if __name__ == "__main__":
    main()
