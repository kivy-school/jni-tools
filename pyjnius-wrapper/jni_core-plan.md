

ok now https://github.com/Py-Swift/CySwiftAst exist and is equal to PySwiftAST for generating cython ast tree / code

now we got the current pyjnius generator mode and it should remain as it is, and just have a flag or subcommand when pyjnius mode..


now we need this new library called jni_core
which just contains .pxi .pxd mostly, and only write core functions for things that reduce reapting too much code
because next is to make it write cython code for each module and write more direct jni calls through that and also avoid having to iterate over types too see what matches or anything.. 

jni_core should just cover base things java<->python types, and any helpers for casting between raw and jni types or whatever can help generator part..
and generator part writes custom cython code for classes / functions  / args / calls and as before writes a pythonic .pyi version.


soo ofc generator belongs in swift package and jni_core is a seperate cython pip module.. 