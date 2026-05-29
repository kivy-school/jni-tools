from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ZipException"]

class ZipException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/util/zip/ZipException"
    __javaconstructor__ = [("()V", False), ("(Ljava/lang/String;)V", False)]