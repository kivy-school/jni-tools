from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["WatchEvent"]

class WatchEvent(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/WatchEvent"
    kind = JavaMethod("()Ljava/nio/file/WatchEvent$Kind;")
    count = JavaMethod("()I")
    context = JavaMethod("()Ljava/lang/Object;")

    class Kind(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "java/nio/file/WatchEvent/Kind"
        name = JavaMethod("()Ljava/lang/String;")
        type = JavaMethod("()Ljava/lang/Class;")

    class Modifier(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "java/nio/file/WatchEvent/Modifier"
        name = JavaMethod("()Ljava/lang/String;")