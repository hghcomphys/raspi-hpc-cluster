help([[
This is the module file for the GCC compiler.
]])

local version = "8.3.0"

whatis("Name: GCC compiler (system default)")
whatis("Version: " .. version)
whatis("Keywords: System, Compiler")
whatis("URL: http://www.gnu.org/")
whatis("Description: GNU compiler family")

family("compiler")

local prefix = "/usr/bin"

setenv("CC",  pathJoin(prefix, "gcc-8"))
setenv("CXX", pathJoin(prefix, "g++-8"))
setenv("FC",  pathJoin(prefix, "fc"))
setenv("C77", pathJoin(prefix, "fc"))

local mroot = os.getenv("MODULEPATH_ROOT")
local mdir = pathJoin(mroot, "GCC", version)
prepend_path("MODULEPATH", mdir)
