from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Channel"]

class Channel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/se/omapi/Channel"
    close = JavaMethod("()V")
    isOpen = JavaMethod("()Z")
    isBasicChannel = JavaMethod("()Z")
    transmit = JavaMethod("([B)[B")
    getSession = JavaMethod("()Landroid/se/omapi/Session;")
    getSelectResponse = JavaMethod("()[B")
    selectNext = JavaMethod("()Z")