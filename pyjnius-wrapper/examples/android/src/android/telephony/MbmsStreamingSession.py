from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MbmsStreamingSession"]

class MbmsStreamingSession(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/MbmsStreamingSession"
    create = JavaMultipleMethod([("(Landroid/content/Context;Ljava/util/concurrent/Executor;ILandroid/telephony/mbms/MbmsStreamingSessionCallback;)Landroid/telephony/MbmsStreamingSession;", True, False), ("(Landroid/content/Context;Ljava/util/concurrent/Executor;Landroid/telephony/mbms/MbmsStreamingSessionCallback;)Landroid/telephony/MbmsStreamingSession;", True, False)])
    close = JavaMethod("()V")
    requestUpdateStreamingServices = JavaMethod("(Ljava/util/List;)V")
    startStreaming = JavaMethod("(Landroid/telephony/mbms/StreamingServiceInfo;Ljava/util/concurrent/Executor;Landroid/telephony/mbms/StreamingServiceCallback;)Landroid/telephony/mbms/StreamingService;")