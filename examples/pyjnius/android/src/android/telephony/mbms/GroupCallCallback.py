from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["GroupCallCallback"]

class GroupCallCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/mbms/GroupCallCallback"
    SIGNAL_STRENGTH_UNAVAILABLE = JavaStaticField("I")
    onBroadcastSignalStrengthUpdated = JavaMethod("(I)V")
    onGroupCallStateChanged = JavaMethod("(II)V")
    onError = JavaMethod("(ILjava/lang/String;)V")