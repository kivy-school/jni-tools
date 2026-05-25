from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UnsupportedCallbackException"]

class UnsupportedCallbackException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/security/auth/callback/UnsupportedCallbackException"
    __javaconstructor__ = [("(Ljavax/security/auth/callback/Callback;)V", False), ("(Ljavax/security/auth/callback/Callback;Ljava/lang/String;)V", False)]
    getCallback = JavaMethod("()Ljavax/security/auth/callback/Callback;")