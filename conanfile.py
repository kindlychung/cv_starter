
from conans import ConanFile, CMake, tools
from conans.tools import os_info, SystemPackageTool
from pathlib import Path
import os
import shutil

homedir = Path.home()
conan_dir = os.path.join(homedir, ".conan")
conan_bin_dir = os.path.join(conan_dir, "bin")
if not os.path.exists(conan_bin_dir):
    os.mkdir(conan_bin_dir)


class cv_starterConan(ConanFile):
    name = "cv_starter"
    version = "0.0.1"
    license = "LGPL"
    author = "kaiyin keenzhong@qq.com"
    url = "https://github.com/kindlychung/cv_starter"
    description = "change_your_description"
    topics = ("cpp", )
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {
        "shared": "False",
        "opencv:shared": "False",
        "opencv:contrib": "True",
        "opencv:gtk": 3
    }
    requires = ("docopt/0.6.2@conan/stable", "opencv/4.0.0@conan/stable")
    generators = "cmake"
    exports_sources = "src/%s/*" % name, "src/CMakeLists.txt", "src/*.cmake"

    def system_requirements(self):
        pack_name = None
        if os_info.linux_distro == "ubuntu":
            # put the system libs that you require here, e.g. ["libpulse-dev"]
            pack_name = None
        if pack_name:
            installer = SystemPackageTool()
            installer.install(pack_name)

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="src")
        cmake.build()

    def package(self):
        self.copy("*", dst="bin", src="bin")

    def imports(self):
        self.copy("*", dst="include", src="include")
        self.copy("*", dst="bin", src="lib")

    def system_requirements(self):
        pack_list = None
        if os_info.linux_distro == "ubuntu":
            pack_list = ["qtbase5-dev"]
        if pack_list:
            for p in pack_list:
                installer = SystemPackageTool()
                installer.install(p)

    def deploy(self):
        self.copy("*", src="bin", dst=conan_bin_dir)
