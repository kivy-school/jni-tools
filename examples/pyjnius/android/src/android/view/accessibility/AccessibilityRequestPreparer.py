from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AccessibilityRequestPreparer"]

class AccessibilityRequestPreparer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/accessibility/AccessibilityRequestPreparer"
    __javaconstructor__ = [("(Landroid/view/View;I)V", False)]
    REQUEST_TYPE_EXTRA_DATA = JavaStaticField("I")
    onPrepareExtraData = JavaMethod("(ILjava/lang/String;Landroid/os/Bundle;Landroid/os/Message;)V")
    getView = JavaMethod("()Landroid/view/View;")