from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TrustManager"]

class TrustManager(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/TrustManager"