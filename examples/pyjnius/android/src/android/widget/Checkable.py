from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Checkable"]

class Checkable(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/Checkable"
    toggle = JavaMethod("()V")
    isChecked = JavaMethod("()Z")
    setChecked = JavaMethod("(Z)V")