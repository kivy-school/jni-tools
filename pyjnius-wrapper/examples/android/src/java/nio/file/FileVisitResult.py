from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FileVisitResult"]

class FileVisitResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/FileVisitResult"
    values = JavaStaticMethod("()[Ljava/nio/file/FileVisitResult;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/nio/file/FileVisitResult;")
    CONTINUE = JavaStaticField("Ljava/nio/file/FileVisitResult;")
    TERMINATE = JavaStaticField("Ljava/nio/file/FileVisitResult;")
    SKIP_SUBTREE = JavaStaticField("Ljava/nio/file/FileVisitResult;")
    SKIP_SIBLINGS = JavaStaticField("Ljava/nio/file/FileVisitResult;")