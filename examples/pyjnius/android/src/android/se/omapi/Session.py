from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Session"]

class Session(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/se/omapi/Session"
    getReader = JavaMethod("()Landroid/se/omapi/Reader;")
    getATR = JavaMethod("()[B")
    close = JavaMethod("()V")
    isClosed = JavaMethod("()Z")
    closeChannels = JavaMethod("()V")
    openBasicChannel = JavaMultipleMethod([("([BB)Landroid/se/omapi/Channel;", False, False), ("([B)Landroid/se/omapi/Channel;", False, False)])
    openLogicalChannel = JavaMultipleMethod([("([BB)Landroid/se/omapi/Channel;", False, False), ("([B)Landroid/se/omapi/Channel;", False, False)])