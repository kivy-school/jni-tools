from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Presentation"]

class Presentation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/Presentation"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/view/Display;)V", False), ("(Landroid/content/Context;Landroid/view/Display;I)V", False)]
    BUTTON1 = JavaStaticField("I")
    BUTTON2 = JavaStaticField("I")
    BUTTON3 = JavaStaticField("I")
    BUTTON_NEGATIVE = JavaStaticField("I")
    BUTTON_NEUTRAL = JavaStaticField("I")
    BUTTON_POSITIVE = JavaStaticField("I")
    onDisplayChanged = JavaMethod("()V")
    onDisplayRemoved = JavaMethod("()V")
    getResources = JavaMethod("()Landroid/content/res/Resources;")
    show = JavaMethod("()V")
    getDisplay = JavaMethod("()Landroid/view/Display;")