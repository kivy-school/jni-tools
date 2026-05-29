from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FileVisitOption"]

class FileVisitOption(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/FileVisitOption"
    values = JavaStaticMethod("()[Ljava/nio/file/FileVisitOption;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/nio/file/FileVisitOption;")
    FOLLOW_LINKS = JavaStaticField("Ljava/nio/file/FileVisitOption;")