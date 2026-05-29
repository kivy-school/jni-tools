from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Serializable"]

class Serializable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/io/Serializable"