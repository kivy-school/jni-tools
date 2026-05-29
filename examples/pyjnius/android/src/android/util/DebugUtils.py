from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DebugUtils"]

class DebugUtils(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/util/DebugUtils"
    isObjectSelected = JavaStaticMethod("(Ljava/lang/Object;)Z")