from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Xfermode"]

class Xfermode(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/Xfermode"
    __javaconstructor__ = [("()V", False)]