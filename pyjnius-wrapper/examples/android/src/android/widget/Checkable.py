from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Checkable"]

class Checkable(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/widget/Checkable"
    setChecked = JavaMethod("(Z)V")
    isChecked = JavaMethod("()Z")
    toggle = JavaMethod("()V")