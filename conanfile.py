from conan import ConanFile
from conan.tools.cmake import CMakeDeps, CMakeToolchain, CMake, cmake_layout
from conan.tools.build import check_min_cppstd

class UsageConan(ConanFile):
    name = "usage"
    version = "0.1"

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*", "include/*"

    def validate(self):
        if self.info.settings.compiler.cppstd:
            check_min_cppstd(self, "20")

    # def build_requirements(self):
    #     self.tool_requires("cppfront/master")

    def requirements(self):
        self.requires("cppfront/master")

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
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
