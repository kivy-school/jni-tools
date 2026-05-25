from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyManager"]

class KeyManager(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/KeyManager"