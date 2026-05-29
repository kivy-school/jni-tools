from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CallControlCallback"]

class CallControlCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telecom/CallControlCallback"
    onSetActive = JavaMethod("(Ljava/util/function/Consumer;)V")
    onCallStreamingStarted = JavaMethod("(Ljava/util/function/Consumer;)V")
    onSetInactive = JavaMethod("(Ljava/util/function/Consumer;)V")
    onAnswer = JavaMethod("(ILjava/util/function/Consumer;)V")
    onDisconnect = JavaMethod("(Landroid/telecom/DisconnectCause;Ljava/util/function/Consumer;)V")