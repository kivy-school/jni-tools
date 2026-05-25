from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeySpec"]

class KeySpec(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "java/security/spec/KeySpec"