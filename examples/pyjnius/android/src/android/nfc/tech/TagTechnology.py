from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TagTechnology"]

class TagTechnology(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/nfc/tech/TagTechnology"
    connect = JavaMethod("()V")
    isConnected = JavaMethod("()Z")
    close = JavaMethod("()V")
    getTag = JavaMethod("()Landroid/nfc/Tag;")