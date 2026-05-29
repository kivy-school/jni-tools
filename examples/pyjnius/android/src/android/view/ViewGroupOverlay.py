from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ViewGroupOverlay"]

class ViewGroupOverlay(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/ViewGroupOverlay"
    remove = JavaMethod("(Landroid/view/View;)V")
    add = JavaMethod("(Landroid/view/View;)V")