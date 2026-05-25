from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AccessibilityNodeProvider"]

class AccessibilityNodeProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/accessibility/AccessibilityNodeProvider"
    __javaconstructor__ = [("()V", False)]
    HOST_VIEW_ID = JavaStaticField("I")
    createAccessibilityNodeInfo = JavaMethod("(I)Landroid/view/accessibility/AccessibilityNodeInfo;")
    addExtraDataToAccessibilityNodeInfo = JavaMethod("(ILandroid/view/accessibility/AccessibilityNodeInfo;Ljava/lang/String;Landroid/os/Bundle;)V")
    performAction = JavaMethod("(IILandroid/os/Bundle;)Z")
    findAccessibilityNodeInfosByText = JavaMethod("(Ljava/lang/String;I)Ljava/util/List;")
    findFocus = JavaMethod("(I)Landroid/view/accessibility/AccessibilityNodeInfo;")