from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Session"]

class Session(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/se/omapi/Session"
    getReader = JavaMethod("()Landroid/se/omapi/Reader;")
    closeChannels = JavaMethod("()V")
    getATR = JavaMethod("()[B")
    openBasicChannel = JavaMultipleMethod([("([BB)Landroid/se/omapi/Channel;", False, False), ("([B)Landroid/se/omapi/Channel;", False, False)])
    openLogicalChannel = JavaMultipleMethod([("([B)Landroid/se/omapi/Channel;", False, False), ("([BB)Landroid/se/omapi/Channel;", False, False)])
    close = JavaMethod("()V")
    isClosed = JavaMethod("()Z")