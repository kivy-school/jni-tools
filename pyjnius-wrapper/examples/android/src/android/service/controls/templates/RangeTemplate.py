from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RangeTemplate"]

class RangeTemplate(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/controls/templates/RangeTemplate"
    __javaconstructor__ = [("(Ljava/lang/String;FFFFLjava/lang/CharSequence;)V", False)]
    getMinValue = JavaMethod("()F")
    getMaxValue = JavaMethod("()F")
    getCurrentValue = JavaMethod("()F")
    getStepValue = JavaMethod("()F")
    getFormatString = JavaMethod("()Ljava/lang/CharSequence;")
    getTemplateType = JavaMethod("()I")