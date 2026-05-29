from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FileTypeDetector"]

class FileTypeDetector(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/spi/FileTypeDetector"
    probeContentType = JavaMethod("(Ljava/nio/file/Path;)Ljava/lang/String;")