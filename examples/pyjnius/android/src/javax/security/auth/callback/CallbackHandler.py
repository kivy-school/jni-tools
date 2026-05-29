from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CallbackHandler"]

class CallbackHandler(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/security/auth/callback/CallbackHandler"
    handle = JavaMethod("([Ljavax/security/auth/callback/Callback;)V")