from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Callback"]

class Callback(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "javax/security/auth/callback/Callback"