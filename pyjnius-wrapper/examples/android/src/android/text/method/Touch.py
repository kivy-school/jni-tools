from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Touch"]

class Touch(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/method/Touch"
    scrollTo = JavaStaticMethod("(Landroid/widget/TextView;Landroid/text/Layout;II)V")
    onTouchEvent = JavaStaticMethod("(Landroid/widget/TextView;Landroid/text/Spannable;Landroid/view/MotionEvent;)Z")
    getInitialScrollX = JavaStaticMethod("(Landroid/widget/TextView;Landroid/text/Spannable;)I")
    getInitialScrollY = JavaStaticMethod("(Landroid/widget/TextView;Landroid/text/Spannable;)I")