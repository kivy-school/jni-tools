from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ObjectStreamException"]

class ObjectStreamException(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/ObjectStreamException"