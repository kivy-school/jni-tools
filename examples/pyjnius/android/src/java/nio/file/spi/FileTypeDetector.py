from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FileTypeDetector"]

class FileTypeDetector(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/nio/file/spi/FileTypeDetector"
    __javaconstructor__ = [("()V", False)]
    probeContentType = JavaMethod("(Ljava/nio/file/Path;)Ljava/lang/String;")