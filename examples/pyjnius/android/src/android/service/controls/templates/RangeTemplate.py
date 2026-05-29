from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RangeTemplate"]

class RangeTemplate(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/controls/templates/RangeTemplate"
    __javaconstructor__ = [("(Ljava/lang/String;FFFFLjava/lang/CharSequence;)V", False)]
    TYPE_ERROR = JavaStaticField("I")
    TYPE_NO_TEMPLATE = JavaStaticField("I")
    TYPE_RANGE = JavaStaticField("I")
    TYPE_STATELESS = JavaStaticField("I")
    TYPE_TEMPERATURE = JavaStaticField("I")
    TYPE_THUMBNAIL = JavaStaticField("I")
    TYPE_TOGGLE = JavaStaticField("I")
    TYPE_TOGGLE_RANGE = JavaStaticField("I")
    getTemplateType = JavaMethod("()I")
    getCurrentValue = JavaMethod("()F")
    getFormatString = JavaMethod("()Ljava/lang/CharSequence;")
    getStepValue = JavaMethod("()F")
    getMinValue = JavaMethod("()F")
    getMaxValue = JavaMethod("()F")