from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps, cmake_layout

class ZerocodeConan(ConanFile):
    name = "zerocode"
    version = "1.0.0"
    license = "MIT"
    author = "Bret Brown"
    url = "https://github.com/bretbrownjr/zerocode"
    description = "A C++ project with no code"
    topics = ("cmake", "library", "packaging")
    
    settings = "os", "arch", "compiler", "build_type"
    options = {
        "shared": [True, False]
    }
    default_options = {
        "shared": False
    }

    exports_sources = "*"
    package_type = "library"
    
    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()
        deps = CMakeDeps(self)
        deps.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.set_property("cmake_file_name", "zerocode")
        self.cpp_info.set_property("cmake_target_name", "zerocode::zerocode")

        # Manually tell Conan the expected library name
        config = str(self.settings.build_type).lower()
        self.cpp_info.libs = [f"zerocode.{config}"]

