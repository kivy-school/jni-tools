from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MbmsStreamingSession"]

class MbmsStreamingSession(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/telephony/MbmsStreamingSession"
    startStreaming = JavaMethod("(Landroid/telephony/mbms/StreamingServiceInfo;Ljava/util/concurrent/Executor;Landroid/telephony/mbms/StreamingServiceCallback;)Landroid/telephony/mbms/StreamingService;")
    requestUpdateStreamingServices = JavaMethod("(Ljava/util/List;)V")
    close = JavaMethod("()V")
    create = JavaMultipleMethod([("(Landroid/content/Context;Ljava/util/concurrent/Executor;Landroid/telephony/mbms/MbmsStreamingSessionCallback;)Landroid/telephony/MbmsStreamingSession;", True, False), ("(Landroid/content/Context;Ljava/util/concurrent/Executor;ILandroid/telephony/mbms/MbmsStreamingSessionCallback;)Landroid/telephony/MbmsStreamingSession;", True, False)])