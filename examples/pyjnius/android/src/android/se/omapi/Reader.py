from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Reader"]

class Reader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/se/omapi/Reader"
    getName = JavaMethod("()Ljava/lang/String;")
    openSession = JavaMethod("()Landroid/se/omapi/Session;")
    isSecureElementPresent = JavaMethod("()Z")
    getSEService = JavaMethod("()Landroid/se/omapi/SEService;")
    closeSessions = JavaMethod("()V")