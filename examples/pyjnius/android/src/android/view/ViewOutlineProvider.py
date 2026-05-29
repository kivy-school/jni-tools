from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ViewOutlineProvider"]

class ViewOutlineProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/ViewOutlineProvider"
    __javaconstructor__ = [("()V", False)]
    BACKGROUND = JavaStaticField("Landroid/view/ViewOutlineProvider;")
    BOUNDS = JavaStaticField("Landroid/view/ViewOutlineProvider;")
    PADDED_BOUNDS = JavaStaticField("Landroid/view/ViewOutlineProvider;")
    getOutline = JavaMethod("(Landroid/view/View;Landroid/graphics/Outline;)V")