from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["StatelessTemplate"]

class StatelessTemplate(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/controls/templates/StatelessTemplate"
    __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
    getTemplateType = JavaMethod("()I")