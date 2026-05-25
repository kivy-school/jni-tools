from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CallbackHandler"]

class CallbackHandler(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "javax/security/auth/callback/CallbackHandler"
    handle = JavaMethod("([Ljavax/security/auth/callback/Callback;)V")