from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ViewGroupOverlay"]

class ViewGroupOverlay(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/ViewGroupOverlay"
    add = JavaMethod("(Landroid/view/View;)V")
    remove = JavaMethod("(Landroid/view/View;)V")