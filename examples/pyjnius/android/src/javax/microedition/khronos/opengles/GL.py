from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GL"]

class GL(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "javax/microedition/khronos/opengles/GL"