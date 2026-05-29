from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TrustManager"]

class TrustManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/net/ssl/TrustManager"