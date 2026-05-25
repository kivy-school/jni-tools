from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ViewOverlay"]

class ViewOverlay(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/ViewOverlay"
    add = JavaMethod("(Landroid/graphics/drawable/Drawable;)V")
    remove = JavaMethod("(Landroid/graphics/drawable/Drawable;)V")
    clear = JavaMethod("()V")