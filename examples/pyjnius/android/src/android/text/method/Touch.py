from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Touch"]

class Touch(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/text/method/Touch"
    getInitialScrollY = JavaStaticMethod("(Landroid/widget/TextView;Landroid/text/Spannable;)I")
    getInitialScrollX = JavaStaticMethod("(Landroid/widget/TextView;Landroid/text/Spannable;)I")
    scrollTo = JavaStaticMethod("(Landroid/widget/TextView;Landroid/text/Layout;II)V")
    onTouchEvent = JavaStaticMethod("(Landroid/widget/TextView;Landroid/text/Spannable;Landroid/view/MotionEvent;)Z")