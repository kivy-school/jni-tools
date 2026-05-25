from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Deprecated"]

class Deprecated(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/Deprecated"
    since = JavaMethod("()Ljava/lang/String;")
    forRemoval = JavaMethod("()Z")