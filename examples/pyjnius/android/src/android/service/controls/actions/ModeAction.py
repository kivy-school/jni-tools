from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ModeAction"]

class ModeAction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/controls/actions/ModeAction"
    __javaconstructor__ = [("(Ljava/lang/String;ILjava/lang/String;)V", False), ("(Ljava/lang/String;I)V", False)]
    RESPONSE_CHALLENGE_ACK = JavaStaticField("I")
    RESPONSE_CHALLENGE_PASSPHRASE = JavaStaticField("I")
    RESPONSE_CHALLENGE_PIN = JavaStaticField("I")
    RESPONSE_FAIL = JavaStaticField("I")
    RESPONSE_OK = JavaStaticField("I")
    RESPONSE_UNKNOWN = JavaStaticField("I")
    TYPE_BOOLEAN = JavaStaticField("I")
    TYPE_COMMAND = JavaStaticField("I")
    TYPE_ERROR = JavaStaticField("I")
    TYPE_FLOAT = JavaStaticField("I")
    TYPE_MODE = JavaStaticField("I")
    getActionType = JavaMethod("()I")
    getNewMode = JavaMethod("()I")