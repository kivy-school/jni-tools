from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Formatter"]

class Formatter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/format/Formatter"
    __javaconstructor__ = [("()V", False)]
    formatFileSize = JavaStaticMethod("(Landroid/content/Context;J)Ljava/lang/String;")
    formatShortFileSize = JavaStaticMethod("(Landroid/content/Context;J)Ljava/lang/String;")
    formatIpAddress = JavaStaticMethod("(I)Ljava/lang/String;")