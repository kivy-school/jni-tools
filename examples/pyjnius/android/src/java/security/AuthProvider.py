from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AuthProvider"]

class AuthProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/AuthProvider"
    logout = JavaMethod("()V")
    setCallbackHandler = JavaMethod("(Ljavax/security/auth/callback/CallbackHandler;)V")
    login = JavaMethod("(Ljavax/security/auth/Subject;Ljavax/security/auth/callback/CallbackHandler;)V")