from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FloatAction"]

class FloatAction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/controls/actions/FloatAction"
    __javaconstructor__ = [("(Ljava/lang/String;F)V", False), ("(Ljava/lang/String;FLjava/lang/String;)V", False)]
    getNewValue = JavaMethod("()F")
    getActionType = JavaMethod("()I")