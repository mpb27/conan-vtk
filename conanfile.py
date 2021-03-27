import os
import re

from fnmatch import fnmatch
from conans import ConanFile, CMake, tools

# This recipe clones the latest nightly from the VTK repository.
# This recipe was originally based on https://github.com/Chrismarsh/conan-vtk
# This recipe was heavily modified and is now primarily based on https://github.com/atrelinski/conan-center-index/blob/master/recipes/vtk/all/conanfile.py
# and the comments in the conan-center-index PR for this recipe (https://github.com/conan-io/conan-center-index/pull/3280).

class VTKConan(ConanFile):
    name = "vtk"
    user = "mpb27"
    channel = "testing"
    description = "Visualization Toolkit by Kitware"
    url = "https://github.com/mpb27/conan-vtk"
    license = "BSD-3-Clause"
    generators = "cmake"
    settings = "os", "compiler", "build_type", "arch"
    exports = ["LICENSE.md"]
    exports_sources = ["FindVTK.cmake", "CMakeLists.txt", "patches/**"]
    source_subfolder = "source_subfolder"
    _groups = ["StandAlone", "Rendering", "MPI", "Qt", "Imaging", "Views", "Web"]
     # _modules are taken from CMake GUI
    _modules = [
        "AcceleratorsVTKm"
        "ChartsCore",
        "CommonArchive"
        "CommonColor"
        "CommonComputationalGeometry",
        "CommonCore",
        "CommonDataModel",
        "CommonExecutionModel",
        "CommonMath"
        "CommonMisc",
        "CommonSystem",
        "CommonTransforms",
        "DICOMParser",
        "DomainsChemistry",
        "DomainsChemistryOpenGL2",
        "DomainsMicroscopy",
        "DomainsParallelChemistry",
        "FiltersAMR",
        "FiltersCore",
        "FiltersExtraction",
        "FiltersFlowPaths",
        "FiltersGeneral",
        "FiltersGeneric",
        "FiltersGeometry",
        "FiltersHybrid",
        "FiltersHyperTree",
        "FiltersImaging",
        "FiltersModeling",
        "FiltersOpenTURNS",
        "FiltersParallel",
        "FiltersParallelDIY2",
        "FiltersParallelFlowPaths",
        "FiltersParallelGeometry",
        "FiltersParallelImaging",
        "FiltersParallelMPI",
        "FiltersParallelStatistics",
        "FiltersParallelVerdict",
        "FiltersPoints",
        "FiltersProgrammable",
        "FiltersReebGraph",
        "FiltersSMP",
        "FiltersSelection",
        "FiltersSources",
        "FiltersStatistics",
        "FiltersTexture",
        "FiltersTopology",
        "FiltersVerdict",
        "GeovisCore",
        "GeovisGDAL",
        "GUISupportMFC",
        "GUISupportQt",
        "GUISupportQtSQL",
        "ImagingColor",
        "ImagingCore",
        "ImagingFourier",
        "ImagingGeneral",
        "ImagingHybrid",
        "ImagingMath",
        "ImagingMorphological",
        "ImagingOpenGL2",
        "ImagingSources",
        "ImagingStatistics",
        "ImagingStencil",
        "InfovisBoost",
        "InfovisBoostGraphAlgorithms",
        "InfovisCore",
        "InfovisLayout",
        "InteractionImage",
        "InteractionStyle",
        "InteractionWidgets",
        "IOADIOS2",
        "IOAMR",
        "IOAsynchronous",
        "IOCityGML",
        "IOCore",
        "IOEnSight",
        "IOExodus",
        "IOExport",
        "IOExportGL2PS",
        "IOExportPDF",
        "IOFFMPEG",
        "IOGDAL",
        "IOGeoJSON",
        "IOGeometry",
        "IOH5part",
        "IOImage",
        "IOImport",
        "IOInfovis",
        "IOLAS",
        "IOLSDyna",
        "IOLegacy",
        "IOMINC",
        "IOMPIImage",
        "IOMotionFX",
        "IOMovie",
        "IOMySQL",
        "IONetCDF",
        "IOODBC",
        "IOOggTheora",
        "IOPDAL",
        "IOPIO",
        "IOPLY",
        "IOParallel",
        "IOParallelExodus",
        "IOParallelLSDyna",
        "IOParallelNetCDF",
        "IOParallelXML",
        "IOParallelXdmf3",
        "IOPostgreSQL",
        "IOSQL",
        "IOSegY",
        "IOTRUCHAS",
        "IOTecplotTable",
        "IOVPIC",
        "IOVeraOut",
        "IOVideo",
        "IOXML",
        "IOXMLParser",
        "IOXdmf2",
        "IOXdmf3",
        "MomentInvariants",
        "ParallelCore",
        "ParallelDIY",
        "ParallelMPI",
        "PoissonReconstruction",
        "Powercrust",
        "PythonInterpreter",
        "RenderingAnnotation",
        "RenderingContext2D",
        "RenderingContextOpenGL2",
        "RenderingCore",
        "RenderingExternal",
        "RenderingFreeType",
        "RenderingFreeTypeFontConfig",
        "RenderingGL2PSOpenGL2",
        "RenderingImage",
        "RenderingLabel",
        "RenderingLICOpenGL2",
        "RenderingLOD",
        "RenderingMatplotlib",
        "RenderingOpenGL2",
        "RenderingOpenVR",
        "RenderingParallel",
        "RenderingParallelLIC",
        "RenderingQt",
        "RenderingRayTracing",
        "RenderingSceneGraph",
        "RenderingUI",
        "RenderingVolume",
        "RenderingVolumeAMR",
        "RenderingVolumeOpenGL2",
        "RenderingVtkJS",
        "SignedTensor",
        "SplineDrivenImageSlicer",
        "TestingCore",
        "TestingGenericBridge",
        "TestingIOSQL",
        "TestingRendering",
        "UtilitiesBenchmarks",
        "ViewsContext2D",
        "ViewsCore",
        "ViewsInfovis",
        "ViewsQt",
        "WebCore",
        "WebGLExporter",
        "WrappingPythonCore",
        "WrappingTools",

        "diy2",
        "doubleconversion",
        "eigen",
        "exodusII",
        "expat",
        "freetype",
        "gl2ps",
        "glew",
        "h5part",
        "hdf5",
        "jpeg",
        "jsoncpp",
        "kissfft",
        "kwiml",
        "libharu",
        "libproj",
        "libxml2",
        "loguru",
        "lz4",
        "lzma",
        "metaio",
        "netcdf",
        "octree",
        "ogg",
        "opengl",
        "pegtl",
        "png",
        "pugixml",
        "sqlite",
        "theora",
        "tiff",
        "utf8",
        "verdict",
        "vpic",
        "vtkDICOM",
        "vtkm",
        "vtksys",
        "xdmf2",
        "xdmf3",
        "zfp",
        "zlib",
    ]
    options = dict({"shared": [True, False], "fPIC": [True, False],
    }, **{"group_{}".format(group.lower()): [True, False] for group in _groups},
    **{"module_{}".format(module.lower()): [True, False] for module in _modules}
    )
    # default_options are set to the same values as clean VTK 9.0.1 cmake installation has, except "shared" which Conan require to be "False" by default.
    default_options = dict({
        "shared": True,
        "fPIC": False,
        }, **{"group_{}".format(group.lower()): True for group in _groups if (group in ["StandAlone", "Rendering"])},
        **{"group_{}".format(group.lower()): False for group in _groups if (group not in ["StandAlone", "Rendering"])},
        **{"module_{}".format(module.lower()): False for module in _modules})
    _cmake = None
    short_paths = True
    vtk_commit = ""  # SHA-1 hash of commit


    def set_version(self):
       if self.vtk_commit:
          tools.download("https://gitlab.kitware.com/vtk/vtk/-/raw/" + self.vtk_commit + "/CMake/vtkVersion.cmake", "temp/vtkVersion.cmake")
       else:
          tools.download("https://gitlab.kitware.com/vtk/vtk/-/raw/nightly-master/CMake/vtkVersion.cmake", "temp/vtkVersion.cmake")
       content = tools.load("temp/vtkVersion.cmake")
       tools.rmdir("temp")
       vtk_version_major = re.search("set\(VTK_MAJOR_VERSION (.*)\)", content).group(1)
       vtk_version_minor = re.search("set\(VTK_MINOR_VERSION (.*)\)", content).group(1)
       vtk_version_build = re.search("set\(VTK_BUILD_VERSION (.*)\)", content).group(1)
       self.version = "%s.%s.%s" %(vtk_version_major, vtk_version_minor, vtk_version_build)
       self.output.info("VTK version available from nightly is %s" % self.version)


    def source(self):
       git = tools.Git(folder="VTK")
       git.clone("https://gitlab.kitware.com/vtk/vtk.git", "nightly-master")
       if self.vtk_commit:
          git.checkout(self.vtk_commit)
       os.rename("VTK", self.source_subfolder)


    def requirements(self):
        if self.options.group_qt:
            self.requires("qt/6.0.1@bincrafters/stable")
            self.requires("bzip2/1.0.8@conan/stable")      # Override for pcre library conflict
            self.options["qt"].shared = True


    def config_options(self):
        if self.settings.compiler == "Visual Studio":
            del self.options.fPIC


    def _configure_cmake(self):
        if self._cmake:
            return self._cmake
        self._cmake = CMake(self)
        self._cmake.definitions["BUILD_TESTING"] = "OFF"
        self._cmake.definitions["BUILD_EXAMPLES"] = "OFF"
        self._cmake.definitions["BUILD_SHARED_LIBS"] = self.options.shared

        # VTK available options for cmake defines are `YES`, `WANT`, `DONT_WANT`, `NO`, or `DEFAULT`. Other values results as cmake configure step failure.
        for group in self._groups:
            self._cmake.definitions["VTK_GROUP_ENABLE_{}".format(group)] = "WANT" if self.options.get_safe("group_{}".format(group.lower()), default=False) else "DEFAULT"
        for module in self._modules:
            # Defines shouldn't be left uninitalized, however VTK has so many _modules, that
            # it ends up as "The command line is too long." error on Windows.
            if self.options.get_safe("module_{}".format(module.lower()), default=False):
                self._cmake.definitions["VTK_MODULE_ENABLE_VTK_{}".format(module)] = "WANT" if self.options.get_safe("module_{}".format(module.lower()), default=False) else "DEFAULT"

        if self.options.group_qt:
            vtk_qt = self.requires["qt"].ref.version.split(".")[0]
            self._cmake.definitions["VTK_QT_VERSION"] = vtk_qt
            self.output.info("VTK_QT_VERSION is " + vtk_qt)

        if self.settings.build_type == "Debug" and self.settings.compiler == "Visual Studio":
            self._cmake.definitions["CMAKE_DEBUG_POSTFIX"] = "_d"

        self._cmake.configure(source_folder=self.source_folder+'/'+self.source_subfolder,build_folder='build')
        return self._cmake


    def build(self):
        cmake = self._configure_cmake()

        if self.options.group_qt:
            cmake.definitions["VTK_QT_VERSION"] = self.requires["qt"].ref.version.split(".")[0]

        if self.settings.build_type == "Debug" and self.settings.compiler == "Visual Studio":
            cmake.definitions["CMAKE_DEBUG_POSTFIX"] = "_d"
        
        #for patch in self.conan_data.get("patches", {}).get(self.version, []):
        #    tools.patch(**patch)

        cmake.build()
    
    
    def validate(self):
        if self.options.group_qt:
            if self.options["qt"].shared == False:
                raise ConanInvalidConfiguration("VTK option 'group_qt' requires 'qt:shared=True'")


    def package(self):
        self.copy("FindVTK.cmake", ".", ".")
        cmake = self._configure_cmake()
        cmake.install()

        # "$\package\lib\vtk" contains "hierarchy\conanvtk\" and a lot of *.txt files in it. I believe they are not needed. Remove them.
        #tools.rmdir(os.path.join(self.package_folder, 'lib', 'vtk'))
        # "$\package\lib\cmake" contains a lot of *.cmake files. conan-center HOOK disallow *.cmake files in package. Remove them.
        #tools.rmdir(os.path.join(self.package_folder, 'lib', 'cmake'))
        # Licenses are created in "$\package\share\licenses\conanvtk\" while their must be in "$\package\licenses\". Move them from former to latter.
        #os.rename(os.path.join(self.package_folder, 'share', 'licenses', 'conanvtk'), os.path.join(self.package_folder, 'licenses'))
        #tools.rmdir(os.path.join(self.package_folder, 'share'))


    def package_info(self):
        self.cpp_info.names["cmake_find_package"] = "VTK"
        self.cpp_info.names["cmake_find_package_multi"] = "VTK"
        self.cpp_info.libs = tools.collect_libs(self)

        version_split = self.version.split('.')
        short_version = "%s.%s" % (version_split[0], version_split[1])

        self.cpp_info.includedirs = [
            "include/vtk-%s" % short_version,
            "include/vtk-%s/vtknetcdf/include" % short_version,
            "include/vtk-%s/vtknetcdfcpp" % short_version
        ]

        if self.settings.os == 'Linux':
            self.cpp_info.libs.append('pthread')
