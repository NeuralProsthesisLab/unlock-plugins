__author__ = 'Graham Voysey'

from jinja2 import Environment, FileSystemLoader
from os import path
import yaml, sys, os, argparse, base

rootDir = base.rootPath
generatorPath = path.join(base.rootPath,"plugin_generator")
templatePath = path.join(generatorPath,"templates")
yamlPath = path.join(generatorPath,"AppConfig.yaml")

# parse input arguments: a path to the yaml config file and an output dir
parser = argparse.ArgumentParser()
parser.add_argument("config", nargs='?', help="YAML file with app configuration values", action='store',
                    default=yamlPath)
parser.add_argument("output", nargs='?', help='directory to use', action='store',
                    default=path.expanduser("~"))
args = parser.parse_args()

# make sure the output path makes sense
assert (path.isdir(args.output))
# read in the YAML, if present.
with open(yamlPath) as _:
    configDict = yaml.load(_)

# Make a folder whose name is the app.
appBasePath = path.join(args.output, configDict['appname'])
os.mkdir(appBasePath)

# render the templated app files
env = Environment(loader=FileSystemLoader(templatePath))
for file in os.listdir(templatePath):
    #render it
    template = env.get_template(file)
    retval = template.render(yaml=configDict)

    if file.endswith(".pytemplate"):
        if file == "app.pytemplate":
            # if the template is the base app, name the new file the name of the new app
            outfile = configDict['appname'] + ".py"
        else:
            #otherwise name it the same as its template with the right extension
            outfile = path.splitext(file)[0] + ".py"
        with open(path.join(appBasePath,outfile),"w") as _:
            _.write(retval)

    if file.endswith(".yptemplate"):
        outfile = configDict['appname'] + ".yapsy-plugin"
        with open(path.join(appBasePath,outfile),"w") as _:
            _.write(retval)





# use jinja to configure an  app.py to the app root directory from a template.

# jinja a base view, model, controller, deocder, daq in the right places.

# exit.
if False:
    ENV = Environment(loader=FileSystemLoader('./'))

    with open("AppConfig.yaml") as _:
        dict = yaml.load(_)

    # Print dictionary generated from yaml
    print(dict)

    # Render template and print generated config to console
    template = ENV.get_template("app.pytemplate")
    print(template.render(config=dict))

    print("script: sys.argv[0] is", repr(sys.argv[0]))
    print("script: __file__ is", repr(__file__))
