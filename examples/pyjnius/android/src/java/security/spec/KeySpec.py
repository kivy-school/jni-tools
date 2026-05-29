from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeySpec"]

class KeySpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/KeySpec"