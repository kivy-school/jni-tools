from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ControlTemplate"]

class ControlTemplate(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/controls/templates/ControlTemplate"
    TYPE_ERROR = JavaStaticField("I")
    TYPE_NO_TEMPLATE = JavaStaticField("I")
    TYPE_RANGE = JavaStaticField("I")
    TYPE_STATELESS = JavaStaticField("I")
    TYPE_TEMPERATURE = JavaStaticField("I")
    TYPE_THUMBNAIL = JavaStaticField("I")
    TYPE_TOGGLE = JavaStaticField("I")
    TYPE_TOGGLE_RANGE = JavaStaticField("I")
    getTemplateId = JavaMethod("()Ljava/lang/String;")
    getTemplateType = JavaMethod("()I")
    getErrorTemplate = JavaStaticMethod("()Landroid/service/controls/templates/ControlTemplate;")
    getNoTemplateObject = JavaStaticMethod("()Landroid/service/controls/templates/ControlTemplate;")