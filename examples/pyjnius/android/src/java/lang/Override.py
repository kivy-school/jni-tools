from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Override"]

class Override(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "java/lang/Override"