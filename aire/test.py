import yaml

# with open('settings.yaml','r') as file:
#     dict = yaml.load(file)
#     print(dict)

# Dynamic pakcage import test

def my_import(name):
    mod = __import__(name)
    components = name.split('.')
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod
module=my_import("aire.action_parser.ExpectParser.expectParser")
parser=getattr(module, "ExpectParser")
instance1=parser.get_instance({"session":"test","expect_name":"add_space"})
instance2=parser.get_instance({"session":"test","expect_name":"add_space"})
print("finished")
