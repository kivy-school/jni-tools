from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LinkOption"]

class LinkOption(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/LinkOption"
    values = JavaStaticMethod("()[Ljava/nio/file/LinkOption;")
    valueOf = JavaStaticMethod("(Ljava/lang/String;)Ljava/nio/file/LinkOption;")
    NOFOLLOW_LINKS = JavaStaticField("Ljava/nio/file/LinkOption;")