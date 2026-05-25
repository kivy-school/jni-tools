from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MbmsGroupCallSession"]

class MbmsGroupCallSession(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/MbmsGroupCallSession"
    create = JavaMultipleMethod([("(Landroid/content/Context;ILjava/util/concurrent/Executor;Landroid/telephony/mbms/MbmsGroupCallSessionCallback;)Landroid/telephony/MbmsGroupCallSession;", True, False), ("(Landroid/content/Context;Ljava/util/concurrent/Executor;Landroid/telephony/mbms/MbmsGroupCallSessionCallback;)Landroid/telephony/MbmsGroupCallSession;", True, False)])
    close = JavaMethod("()V")
    startGroupCall = JavaMethod("(JLjava/util/List;Ljava/util/List;Ljava/util/concurrent/Executor;Landroid/telephony/mbms/GroupCallCallback;)Landroid/telephony/mbms/GroupCall;")