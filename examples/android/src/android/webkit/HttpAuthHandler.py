from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HttpAuthHandler"]

class HttpAuthHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/HttpAuthHandler"
    useHttpAuthUsernamePassword = JavaMethod("()Z")
    cancel = JavaMethod("()V")
    proceed = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")