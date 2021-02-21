# Conan-VTK - Nightly Build Recipe

To create the VTK build using the new auto clone from git:

```
conan create .

OR

conan create . -pr vs2019 -o vtk:group_qt=True
```

_Note_: This will create vtk/9.0.[nightly build number]@mpb27/testing package.

This recipe clones the latest nightly from the VTK repository.

This recipe was originally based on https://github.com/Chrismarsh/conan-vtk but was 
was subsequently heavily modified and is now primarily based on https://github.com/atrelinski/conan-center-index/blob/master/recipes/vtk/all/conanfile.py and the comments in the conan-center-index PR for this recipe (https://github.com/conan-io/conan-center-index/pull/3280).
