from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ToggleRangeTemplate"]

class ToggleRangeTemplate(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/controls/templates/ToggleRangeTemplate"
    __javaconstructor__ = [("(Ljava/lang/String;Landroid/service/controls/templates/ControlButton;Landroid/service/controls/templates/RangeTemplate;)V", False), ("(Ljava/lang/String;ZLjava/lang/CharSequence;Landroid/service/controls/templates/RangeTemplate;)V", False)]
    getRange = JavaMethod("()Landroid/service/controls/templates/RangeTemplate;")
    isChecked = JavaMethod("()Z")
    getActionDescription = JavaMethod("()Ljava/lang/CharSequence;")
    getTemplateType = JavaMethod("()I")