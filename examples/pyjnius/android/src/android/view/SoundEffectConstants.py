from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SoundEffectConstants"]

class SoundEffectConstants(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/SoundEffectConstants"
    CLICK = JavaStaticField("I")
    NAVIGATION_DOWN = JavaStaticField("I")
    NAVIGATION_LEFT = JavaStaticField("I")
    NAVIGATION_REPEAT_DOWN = JavaStaticField("I")
    NAVIGATION_REPEAT_LEFT = JavaStaticField("I")
    NAVIGATION_REPEAT_RIGHT = JavaStaticField("I")
    NAVIGATION_REPEAT_UP = JavaStaticField("I")
    NAVIGATION_RIGHT = JavaStaticField("I")
    NAVIGATION_UP = JavaStaticField("I")
    getConstantForFocusDirection = JavaStaticMethod("(IZ)I")
    getContantForFocusDirection = JavaStaticMethod("(I)I")