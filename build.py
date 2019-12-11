from cpt.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.add_common_builds(shared_option_name="vtk:shared",
                                pure_c=False,
                                gcc_versions=["8.0"],
                                archs=["x86_64"],
                                build_types=["Release"])
    builder.run()
