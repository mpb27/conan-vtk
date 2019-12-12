from cpt.packager import ConanMultiPackager
from collections import defaultdict

if __name__ == "__main__":
    builder = ConanMultiPackager(
                                archs=["x86_64"],
                                build_types=["Release"],
                                curpage="gcc_shared")
    builder.add_common_builds(pure_c=False,shared_option_name="vtk:shared")

    builder.remove_build_if(lambda build: build.settings["compiler.libcxx"] == "libstdc++")


    named_builds = defaultdict(list)
    for settings, options, env_vars, build_requires, reference in builder.items:
        print(settings)
        
        shared="shared"
        if not options['vtk:shared']:
            shared = "static" 

        named_builds[settings['compiler'] +"_"+shared].append([settings, options, env_vars, build_requires, reference])

    builder.named_builds = named_builds

    builder.curpage = list(named_builds.keys())[0] #start at first key

    builder.run()

