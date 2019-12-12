from cpt.packager import ConanMultiPackager
from collections import defaultdict

if __name__ == "__main__":
    builder = ConanMultiPackager(gcc_versions=["8"],
                                apple_clang_versions=["11.0.0"],
                                archs=["x86_64"],
                                build_types=["Release"],
                                curpage="linux", total_pages=2)
    builder.add_common_builds(pure_c=False,shared_option_name="vtk:shared")

    builder.remove_build_if(lambda build: build.settings["compiler.libcxx"] == "libstdc++")


    named_builds = defaultdict(list)
    for settings, options, env_vars, build_requires, reference in builder.items:
        named_builds[settings['os']].append([settings, options, env_vars, build_requires, reference])

    builder.named_builds = named_builds

    builder.run()

