from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Reader"]

class Reader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/se/omapi/Reader"
    closeSessions = JavaMethod("()V")
    getSEService = JavaMethod("()Landroid/se/omapi/SEService;")
    isSecureElementPresent = JavaMethod("()Z")
    getName = JavaMethod("()Ljava/lang/String;")
    openSession = JavaMethod("()Landroid/se/omapi/Session;")