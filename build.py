from cpt.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager(gcc_versions=["8"],
                                archs=["x86_64"],
                                build_types=["Release"],
                                curpage="p1", total_pages=2)
    builder.add_common_builds(pure_c=False,shared_option_name="vtk:shared")

    builder.remove_build_if(lambda build: build.settings["compiler.libcxx"] == "libstdc++")


    i=0
    for settings, options, env_vars, build_requires, reference in builder.items:
        i += 1 
        named_builds["p%s" % i].append([settings, options, env_vars, build_requires, reference])

    builder.named_builds = named_builds

    builder.run()

