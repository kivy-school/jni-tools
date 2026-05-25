from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GroupCallCallback"]

class GroupCallCallback(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/mbms/GroupCallCallback"
    SIGNAL_STRENGTH_UNAVAILABLE = JavaStaticField("I")
    onError = JavaMethod("(ILjava/lang/String;)V")
    onGroupCallStateChanged = JavaMethod("(II)V")
    onBroadcastSignalStrengthUpdated = JavaMethod("(I)V")