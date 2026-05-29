from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Callback"]

class Callback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/security/auth/callback/Callback"