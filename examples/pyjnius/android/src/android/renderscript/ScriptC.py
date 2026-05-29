from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ScriptC"]

class ScriptC(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/ScriptC"