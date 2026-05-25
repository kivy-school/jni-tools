from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ToggleTemplate"]

class ToggleTemplate(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/controls/templates/ToggleTemplate"
    __javaconstructor__ = [("(Ljava/lang/String;Landroid/service/controls/templates/ControlButton;)V", False)]
    isChecked = JavaMethod("()Z")
    getContentDescription = JavaMethod("()Ljava/lang/CharSequence;")
    getTemplateType = JavaMethod("()I")