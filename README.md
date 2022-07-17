# Wicky
[![Ko-Fi](https://img.shields.io/badge/donate-kofi-blue?style=for-the-badge&logo=ko-fi&color=E35B57&logoColor=FFFFFF&labelColor=232323)](https://ko-fi.com/molasses)
[![Patreon](https://img.shields.io/badge/donate-patreon-blue?style=for-the-badge&logo=patreon&color=E35B57&logoColor=FFFFFF&labelColor=232323)](https://www.patreon.com/molasseslover)
[![PyPI](https://img.shields.io/badge/module-pip-blue?style=for-the-badge&logo=python&color=E35B57&logoColor=FFFFFF&labelColor=232323)](https://pypi.org/project/Wicky/)

Wicky is a free and open-source command-line tool for generating 
Wicked Engine projects.

### Usage

```sh
➜ cd 'Source/'
➜ python3 Wicky.py
```

In order to compile the generated project, you will have to 
clone the Wicked Engine project into a directory named
`Library/`

```sh
➜ mkdir Library
➜ cd Library
➜ git clone https://github.com/MolassesLover/WickedEngine.git --recursive
➜ cd WickedEngine
➜ git checkout library
➜ cd ../..
```

## Dependencies
[![Colorama](https://img.shields.io/badge/colorama-pip-blue?style=for-the-badge&logo=python&color=E35B57&logoColor=FFFFFF&labelColor=232323)](https://pypi.org/project/colorama/)
[![PyYAML](https://img.shields.io/badge/yaml-pip-blue?style=for-the-badge&logo=python&color=E35B57&logoColor=FFFFFF&labelColor=232323)](https://pypi.org/project/PyYAML/)

In order to build the generated project you will need a few pieces of software on 
your system. Depending on your operating system and its distribution, some of these 
dependencies might already be met. In any case, dependencies are fairly minimal.

Here is a full list of dependencies:

- [Wicked Engine](https://github.com/turanszkij/WickedEngine)
- [CMake](https://cmake.org/)
- [Colorama](https://pypi.org/project/colorama/)
- [Vulkan](https://www.vulkan.org/)
- [SDL2](https://www.libsdl.org/download-2.0.php)
- [DXC](https://github.com/Microsoft/DirectXShaderCompiler)


### Building

The generated project uses CMake for building, making it a dependency.

Here are example build commands:

```sh
➜ cd Library/WickedEngine
➜ cmake -B Build
➜ cmake --build Build -j$(nproc)
➜ cd ../..
➜ cmake -B Build -DWickedEngine_DIR=/Library/WickedEngine/Build .
➜ cmake --build Build -j$(nproc)
```
