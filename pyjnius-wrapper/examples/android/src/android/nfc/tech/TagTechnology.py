from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TagTechnology"]

class TagTechnology(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/nfc/tech/TagTechnology"
    getTag = JavaMethod("()Landroid/nfc/Tag;")
    connect = JavaMethod("()V")
    close = JavaMethod("()V")
    isConnected = JavaMethod("()Z")