from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PorterDuffXfermode"]

class PorterDuffXfermode(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/PorterDuffXfermode"
    __javaconstructor__ = [("(Landroid/graphics/PorterDuff$Mode;)V", False)]