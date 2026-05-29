from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CommandAction"]

class CommandAction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/controls/actions/CommandAction"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;)V", False), ("(Ljava/lang/String;)V", False)]
    getActionType = JavaMethod("()I")