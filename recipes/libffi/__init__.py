from os.path import join
from multiprocessing import cpu_count

import sh

from pythonforandroid.recipe import Recipe
from pythonforandroid.logger import shprint
from pythonforandroid.util import current_directory


class LibffiRecipe(Recipe):
    """
    Android CI compatibility recipe.

    Uses libffi's official release tarball, which already includes the generated
    configure script. This avoids regenerating autotools files on newer Ubuntu
    runners, where libffi 3.4.2's LT_SYS_SYMBOL_USCORE macro can fail during
    autoreconf.
    """
    name = "libffi"
    version = "3.4.2"
    url = (
        "https://github.com/libffi/libffi/releases/download/"
        "v{version}/libffi-{version}.tar.gz"
    )

    patches = []
    built_libraries = {"libffi.so": ".libs"}

    def build_arch(self, arch):
        env = self.get_recipe_env(arch)
        with current_directory(self.get_build_dir(arch.arch)):
            shprint(
                sh.Command("./configure"),
                "--host=" + arch.command_prefix,
                "--prefix=" + self.get_build_dir(arch.arch),
                "--disable-builddir",
                "--enable-shared",
                _env=env,
            )
            shprint(
                sh.make,
                "-j",
                str(cpu_count()),
                "libffi.la",
                _env=env,
            )

    def get_include_dirs(self, arch):
        return [join(self.get_build_dir(arch), "include")]


recipe = LibffiRecipe()
