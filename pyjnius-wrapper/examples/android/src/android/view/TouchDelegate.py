from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TouchDelegate"]

class TouchDelegate(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/TouchDelegate"
    __javaconstructor__ = [("(Landroid/graphics/Rect;Landroid/view/View;)V", False)]
    ABOVE = JavaStaticField("I")
    BELOW = JavaStaticField("I")
    TO_LEFT = JavaStaticField("I")
    TO_RIGHT = JavaStaticField("I")
    onTouchEvent = JavaMethod("(Landroid/view/MotionEvent;)Z")
    onTouchExplorationHoverEvent = JavaMethod("(Landroid/view/MotionEvent;)Z")
    getTouchDelegateInfo = JavaMethod("()Landroid/view/accessibility/AccessibilityNodeInfo$TouchDelegateInfo;")