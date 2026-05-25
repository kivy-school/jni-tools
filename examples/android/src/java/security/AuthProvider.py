from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AuthProvider"]

class AuthProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/AuthProvider"
    __javaconstructor__ = [("(Ljava/lang/String;DLjava/lang/String;)V", False)]
    login = JavaMethod("(Ljavax/security/auth/Subject;Ljavax/security/auth/callback/CallbackHandler;)V")
    logout = JavaMethod("()V")
    setCallbackHandler = JavaMethod("(Ljavax/security/auth/callback/CallbackHandler;)V")