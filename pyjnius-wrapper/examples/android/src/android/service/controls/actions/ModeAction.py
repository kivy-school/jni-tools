from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ModeAction"]

class ModeAction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/controls/actions/ModeAction"
    __javaconstructor__ = [("(Ljava/lang/String;ILjava/lang/String;)V", False), ("(Ljava/lang/String;I)V", False)]
    getActionType = JavaMethod("()I")
    getNewMode = JavaMethod("()I")