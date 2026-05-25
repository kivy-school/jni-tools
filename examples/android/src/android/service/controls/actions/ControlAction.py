from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ControlAction"]

class ControlAction(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/controls/actions/ControlAction"
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
    isValidResponse = JavaStaticMethod("(I)Z")
    getActionType = JavaMethod("()I")
    getTemplateId = JavaMethod("()Ljava/lang/String;")
    getChallengeValue = JavaMethod("()Ljava/lang/String;")
    getErrorAction = JavaStaticMethod("()Landroid/service/controls/actions/ControlAction;")