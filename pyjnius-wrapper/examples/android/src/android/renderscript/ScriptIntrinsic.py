from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ScriptIntrinsic"]

class ScriptIntrinsic(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/renderscript/ScriptIntrinsic"