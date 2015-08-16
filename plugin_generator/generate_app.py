__author__ = 'Graham Voysey'

from os import path, listdir, mkdir
import argparse
from jinja2 import Environment, FileSystemLoader
import yaml
import base

rootDir = base.rootPath
generatorPath = path.join(base.rootPath, "plugin_generator")
templatePath = path.join(generatorPath, "templates")
yamlPath = path.join(generatorPath, "AppConfig.yaml")

# parse input arguments: a path to the yaml config file and an output dir
parser = argparse.ArgumentParser()
parser.add_argument("config", nargs='?',
                    help="YAML file with app configuration values",
                    action='store',
                    default=yamlPath)
parser.add_argument("output", nargs='?',
                    help='directory to use',
                    action='store',
                    default=path.expanduser("~"))
args = parser.parse_args()

# make sure the output path makes sense
assert (path.isdir(args.output))
# read in the YAML, if present.
with open(yamlPath) as _:
    configDict = yaml.load(_)

# Make a folder whose name is the app.
appBasePath = path.join(args.output, configDict['appname'])
mkdir(appBasePath)

# render the templated app files
env = Environment(loader=FileSystemLoader(templatePath))
for file in listdir(templatePath):
    # render it
    template = env.get_template(file)
    retval = template.render(yaml=configDict)
    # generate all the python module stubs
    if file.endswith(".pytemplate"):
        out = path.splitext(file)[0] + ".py" if file != "app.pytemplate" else out = configDict['appname'] + ".py"
        with open(path.join(appBasePath, out), "w") as _:
            _.write(retval)
    # generate the plugin registration file
    if file.endswith(".yptemplate"):
        out = configDict['appname'] + ".yapsy-plugin"
        with open(path.join(appBasePath, out), "w") as _:
            _.write(retval)

print("A new app template has been generated in {0}", appBasePath)
