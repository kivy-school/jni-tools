from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Channel"]

class Channel(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/se/omapi/Channel"
    isBasicChannel = JavaMethod("()Z")
    getSelectResponse = JavaMethod("()[B")
    selectNext = JavaMethod("()Z")
    getSession = JavaMethod("()Landroid/se/omapi/Session;")
    isOpen = JavaMethod("()Z")
    close = JavaMethod("()V")
    transmit = JavaMethod("([B)[B")