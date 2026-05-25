from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BasicFileAttributeView"]

class BasicFileAttributeView(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/attribute/BasicFileAttributeView"
    name = JavaMethod("()Ljava/lang/String;")
    readAttributes = JavaMethod("()Ljava/nio/file/attribute/BasicFileAttributes;")
    setTimes = JavaMethod("(Ljava/nio/file/attribute/FileTime;Ljava/nio/file/attribute/FileTime;Ljava/nio/file/attribute/FileTime;)V")