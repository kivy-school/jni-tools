from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ViewOverlay"]

class ViewOverlay(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/ViewOverlay"
    remove = JavaMethod("(Landroid/graphics/drawable/Drawable;)V")
    clear = JavaMethod("()V")
    add = JavaMethod("(Landroid/graphics/drawable/Drawable;)V")