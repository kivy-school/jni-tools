from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AutoTransition"]

class AutoTransition(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/transition/AutoTransition"
    __javaconstructor__ = [("()V", False), ("(Landroid/content/Context;Landroid/util/AttributeSet;)V", False)]