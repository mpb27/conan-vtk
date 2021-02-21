set(VTK_DIR ${CONAN_VTK_ROOT})
include(${CONAN_VTK_ROOT}/lib/cmake/vtk-9.0/vtk-config.cmake)

mark_as_advanced(
	VTK_DIR
)
