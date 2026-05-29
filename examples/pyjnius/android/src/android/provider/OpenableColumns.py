from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OpenableColumns"]

class OpenableColumns(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/provider/OpenableColumns"
    DISPLAY_NAME = JavaStaticField("Ljava/lang/String;")
    SIZE = JavaStaticField("Ljava/lang/String;")