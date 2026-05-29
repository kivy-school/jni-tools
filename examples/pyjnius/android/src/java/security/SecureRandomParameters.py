from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SecureRandomParameters"]

class SecureRandomParameters(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/SecureRandomParameters"