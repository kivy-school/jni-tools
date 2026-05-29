from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyManager"]

class KeyManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/KeyManager"