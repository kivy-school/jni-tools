from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TemperatureControlTemplate"]

class TemperatureControlTemplate(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/controls/templates/TemperatureControlTemplate"
    __javaconstructor__ = [("(Ljava/lang/String;Landroid/service/controls/templates/ControlTemplate;III)V", False)]
    FLAG_MODE_COOL = JavaStaticField("I")
    FLAG_MODE_ECO = JavaStaticField("I")
    FLAG_MODE_HEAT = JavaStaticField("I")
    FLAG_MODE_HEAT_COOL = JavaStaticField("I")
    FLAG_MODE_OFF = JavaStaticField("I")
    MODE_COOL = JavaStaticField("I")
    MODE_ECO = JavaStaticField("I")
    MODE_HEAT = JavaStaticField("I")
    MODE_HEAT_COOL = JavaStaticField("I")
    MODE_OFF = JavaStaticField("I")
    MODE_UNKNOWN = JavaStaticField("I")
    TYPE_ERROR = JavaStaticField("I")
    TYPE_NO_TEMPLATE = JavaStaticField("I")
    TYPE_RANGE = JavaStaticField("I")
    TYPE_STATELESS = JavaStaticField("I")
    TYPE_TEMPERATURE = JavaStaticField("I")
    TYPE_THUMBNAIL = JavaStaticField("I")
    TYPE_TOGGLE = JavaStaticField("I")
    TYPE_TOGGLE_RANGE = JavaStaticField("I")
    getCurrentMode = JavaMethod("()I")
    getCurrentActiveMode = JavaMethod("()I")
    getModes = JavaMethod("()I")
    getTemplate = JavaMethod("()Landroid/service/controls/templates/ControlTemplate;")
    getTemplateType = JavaMethod("()I")