from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WatchEvent"]

class WatchEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/WatchEvent"
    count = JavaMethod("()I")
    kind = JavaMethod("()Ljava/nio/file/WatchEvent$Kind;")
    context = JavaMethod("()Ljava/lang/Object;")

    class Modifier(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/nio/file/WatchEvent$Modifier"
        name = JavaMethod("()Ljava/lang/String;")

    class Kind(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "java/nio/file/WatchEvent$Kind"
        name = JavaMethod("()Ljava/lang/String;")
        type = JavaMethod("()Ljava/lang/Class;")