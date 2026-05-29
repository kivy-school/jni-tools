from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TranslateAnimation"]

class TranslateAnimation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/animation/TranslateAnimation"
    __javaconstructor__ = [("(IFIFIFIF)V", False), ("(FFFF)V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False)]
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
    initialize = JavaMethod("(IIII)V")