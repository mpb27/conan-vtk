# vtk

This is a minimal Conan build of the vtk library for use with [CHM](https://github.com/Chrismarsh/CHM). 

Build artifacts are uploaded to [Bintray](https://bintray.com/chrismarsh/CHM)


```
conan install vtk/8.2.0@CHM/stable
```

To create the VTK build:

```
conan create . vtk/9.0.1@mpb27/stable
conan create . vtk/9.0.1@mpb27/stable -o vtk:VTK_Group_Qt=True -pr vs2019
conan install vtk/9.0.1@mpb27/stable -o vtk:VTK_Group_Qt=True -pr vs2019
```

To create the VTK build using the new auto clone from git:

```
conan create .
```

_Note_: This will create vtk/9.0.<nightly build number>@mpb27/testing package.
