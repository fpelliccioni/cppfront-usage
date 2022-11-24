from conan import ConanFile
from conan.tools.cmake import CMakeDeps, CMakeToolchain, CMake, cmake_layout
from conan.tools.build import check_min_cppstd

class UsageConan(ConanFile):
    name = "usage"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"

    exports_sources = "CMakeLists.txt", "src/*", "include/*"

    def validate(self):
        if self.info.settings.compiler.cppstd:
            check_min_cppstd(self, "20")

    def requirements(self):
        self.requires("cppfront/cci.20221024")

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        # tc.variables["CMAKE_VERBOSE_MAKEFILE"] = True
        tc.generate()
        tc = CMakeDeps(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()
