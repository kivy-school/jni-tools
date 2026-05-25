from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GL"]

class GL(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "javax/microedition/khronos/opengles/GL"