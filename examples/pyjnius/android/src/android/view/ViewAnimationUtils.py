from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ViewAnimationUtils"]

class ViewAnimationUtils(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/ViewAnimationUtils"
    createCircularReveal = JavaStaticMethod("(Landroid/view/View;IIFF)Landroid/animation/Animator;")