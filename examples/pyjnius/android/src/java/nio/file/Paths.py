from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Paths"]

class Paths(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/Paths"
    get = JavaMultipleMethod([("(Ljava/lang/String;[Ljava/lang/String;)Ljava/nio/file/Path;", True, True), ("(Ljava/net/URI;)Ljava/nio/file/Path;", True, False)])