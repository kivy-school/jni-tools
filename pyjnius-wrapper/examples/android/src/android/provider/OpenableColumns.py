from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["OpenableColumns"]

class OpenableColumns(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/provider/OpenableColumns"
    DISPLAY_NAME = JavaStaticField("Ljava/lang/String;")
    SIZE = JavaStaticField("Ljava/lang/String;")