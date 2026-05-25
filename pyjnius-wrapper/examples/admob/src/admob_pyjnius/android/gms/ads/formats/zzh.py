from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzh"]

class zzh(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/formats/zzh"
    addView = JavaMethod("(Landroid/view/View;ILandroid/view/ViewGroup$LayoutParams;)V")
    removeView = JavaMethod("(Landroid/view/View;)V")
    removeAllViews = JavaMethod("()V")
    bringChildToFront = JavaMethod("(Landroid/view/View;)V")
    onVisibilityChanged = JavaMethod("(Landroid/view/View;I)V")
    dispatchTouchEvent = JavaMethod("(Landroid/view/MotionEvent;)Z")