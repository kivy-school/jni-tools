from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Presentation"]

class Presentation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/Presentation"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/view/Display;)V", False), ("(Landroid/content/Context;Landroid/view/Display;I)V", False)]
    getDisplay = JavaMethod("()Landroid/view/Display;")
    getResources = JavaMethod("()Landroid/content/res/Resources;")
    onStart = JavaMethod("()V")
    onStop = JavaMethod("()V")
    show = JavaMethod("()V")
    onDisplayRemoved = JavaMethod("()V")
    onDisplayChanged = JavaMethod("()V")