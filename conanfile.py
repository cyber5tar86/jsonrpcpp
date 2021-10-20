from conans import ConanFile, tools
import os


class JsonRpcppConan(ConanFile):
    name = "jsonrpcpp"
    version = "1.4.0"
    url = "https://github.com/cyber5tar86/jsonrpcpp"
    homepage = "https://github.com/badaix/jsonrpcpp"
    description = "C++ JSON-RPC 2.0 library"
    license = "MIT"
    topics = ("rpc", "json-rpc")
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {'shared': False, 'fPIC': True}
    generators = "cmake"
    exports = ["LICENSE.md", "README.md"]
    no_copy_source = True

    scm = {"revision": "1.4.0",
           "type": "git",
           "url": "https://github.com/cyber5tar86/jsonrpcpp"}

    def requirements(self):
        self.requires("nlohmann_json/3.9.1")

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src=self.source_folder)
        self.copy(pattern="README.md", dst="licenses", src=self.source_folder)
        self.copy("*.hpp", dst=src=os.path.join("include", "jsonrpcpp"), src=os.path.join(self.source_folder, include))

    def package_id(self):
        self.info.header_only()