from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AlphaAnimation"]

class AlphaAnimation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/animation/AlphaAnimation"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False), ("(FF)V", False)]
    ABSOLUTE = JavaStaticField("I")
    INFINITE = JavaStaticField("I")
    RELATIVE_TO_PARENT = JavaStaticField("I")
    RELATIVE_TO_SELF = JavaStaticField("I")
    RESTART = JavaStaticField("I")
    REVERSE = JavaStaticField("I")
    START_ON_FIRST_FRAME = JavaStaticField("I")
    ZORDER_BOTTOM = JavaStaticField("I")
    ZORDER_NORMAL = JavaStaticField("I")
    ZORDER_TOP = JavaStaticField("I")
    willChangeBounds = JavaMethod("()Z")
    willChangeTransformationMatrix = JavaMethod("()Z")