from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ZipError"]

class ZipError(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/zip/ZipError"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]