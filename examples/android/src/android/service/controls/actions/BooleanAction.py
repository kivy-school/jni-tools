from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BooleanAction"]

class BooleanAction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/controls/actions/BooleanAction"
    __javaconstructor__ = [("(Ljava/lang/String;Z)V", False), ("(Ljava/lang/String;ZLjava/lang/String;)V", False)]
    getNewState = JavaMethod("()Z")
    getActionType = JavaMethod("()I")