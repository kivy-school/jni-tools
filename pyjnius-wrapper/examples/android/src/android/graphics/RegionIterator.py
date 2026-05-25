from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RegionIterator"]

class RegionIterator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/RegionIterator"
    __javaconstructor__ = [("(Landroid/graphics/Region;)V", False)]
    next = JavaMethod("(Landroid/graphics/Rect;)Z")
    finalize = JavaMethod("()V")