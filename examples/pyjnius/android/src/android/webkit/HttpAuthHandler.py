from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["HttpAuthHandler"]

class HttpAuthHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/webkit/HttpAuthHandler"
    cancel = JavaMethod("()V")
    useHttpAuthUsernamePassword = JavaMethod("()Z")
    proceed = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")