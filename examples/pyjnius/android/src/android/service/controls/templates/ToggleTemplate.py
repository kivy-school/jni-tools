from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ToggleTemplate"]

class ToggleTemplate(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/controls/templates/ToggleTemplate"
    __javaconstructor__ = [("(Ljava/lang/String;Landroid/service/controls/templates/ControlButton;)V", False)]
    TYPE_ERROR = JavaStaticField("I")
    TYPE_NO_TEMPLATE = JavaStaticField("I")
    TYPE_RANGE = JavaStaticField("I")
    TYPE_STATELESS = JavaStaticField("I")
    TYPE_TEMPERATURE = JavaStaticField("I")
    TYPE_THUMBNAIL = JavaStaticField("I")
    TYPE_TOGGLE = JavaStaticField("I")
    TYPE_TOGGLE_RANGE = JavaStaticField("I")
    getTemplateType = JavaMethod("()I")
    getContentDescription = JavaMethod("()Ljava/lang/CharSequence;")
    isChecked = JavaMethod("()Z")