from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SecureClassLoader"]

class SecureClassLoader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/SecureClassLoader"