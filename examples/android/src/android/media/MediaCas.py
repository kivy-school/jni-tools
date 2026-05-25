from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaCas"]

class MediaCas(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/MediaCas"
    __javaconstructor__ = [("(I)V", False), ("(Landroid/content/Context;ILjava/lang/String;I)V", False), ("(Landroid/content/Context;ILjava/lang/String;ILandroid/os/Handler;Landroid/media/MediaCas$EventListener;)V", False)]
    PLUGIN_STATUS_PHYSICAL_MODULE_CHANGED = JavaStaticField("I")
    PLUGIN_STATUS_SESSION_NUMBER_CHANGED = JavaStaticField("I")
    SCRAMBLING_MODE_AES128 = JavaStaticField("I")
    SCRAMBLING_MODE_AES_CBC = JavaStaticField("I")
    SCRAMBLING_MODE_AES_ECB = JavaStaticField("I")
    SCRAMBLING_MODE_AES_SCTE52 = JavaStaticField("I")
    SCRAMBLING_MODE_DVB_CISSA_V1 = JavaStaticField("I")
    SCRAMBLING_MODE_DVB_CSA1 = JavaStaticField("I")
    SCRAMBLING_MODE_DVB_CSA2 = JavaStaticField("I")
    SCRAMBLING_MODE_DVB_CSA3_ENHANCE = JavaStaticField("I")
    SCRAMBLING_MODE_DVB_CSA3_MINIMAL = JavaStaticField("I")
    SCRAMBLING_MODE_DVB_CSA3_STANDARD = JavaStaticField("I")
    SCRAMBLING_MODE_DVB_IDSA = JavaStaticField("I")
    SCRAMBLING_MODE_MULTI2 = JavaStaticField("I")
    SCRAMBLING_MODE_RESERVED = JavaStaticField("I")
    SCRAMBLING_MODE_TDES_ECB = JavaStaticField("I")
    SCRAMBLING_MODE_TDES_SCTE52 = JavaStaticField("I")
    SESSION_USAGE_LIVE = JavaStaticField("I")
    SESSION_USAGE_PLAYBACK = JavaStaticField("I")
    SESSION_USAGE_RECORD = JavaStaticField("I")
    SESSION_USAGE_TIMESHIFT = JavaStaticField("I")
    isSystemIdSupported = JavaStaticMethod("(I)Z")
    enumeratePlugins = JavaStaticMethod("()[Landroid/media/MediaCas$PluginDescriptor;")
    setEventListener = JavaMethod("(Landroid/media/MediaCas$EventListener;Landroid/os/Handler;)V")
    setPrivateData = JavaMethod("([B)V")
    openSession = JavaMultipleMethod([("()Landroid/media/MediaCas$Session;", False, False), ("(II)Landroid/media/MediaCas$Session;", False, False)])
    processEmm = JavaMultipleMethod([("([BII)V", False, False), ("([B)V", False, False)])
    sendEvent = JavaMethod("(II[B)V")
    provision = JavaMethod("(Ljava/lang/String;)V")
    refreshEntitlements = JavaMethod("(I[B)V")
    close = JavaMethod("()V")
    finalize = JavaMethod("()V")

    class EventListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaCas/EventListener"
        onEvent = JavaMethod("(Landroid/media/MediaCas;II[B)V")
        onSessionEvent = JavaMethod("(Landroid/media/MediaCas;Landroid/media/MediaCas$Session;II[B)V")
        onPluginStatusUpdate = JavaMethod("(Landroid/media/MediaCas;II)V")
        onResourceLost = JavaMethod("(Landroid/media/MediaCas;)V")

    class PluginDescriptor(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaCas/PluginDescriptor"
        getSystemId = JavaMethod("()I")
        getName = JavaMethod("()Ljava/lang/String;")
        toString = JavaMethod("()Ljava/lang/String;")

    class Session(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaCas/Session"
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        setPrivateData = JavaMethod("([B)V")
        processEcm = JavaMultipleMethod([("([BII)V", False, False), ("([B)V", False, False)])
        sendSessionEvent = JavaMethod("(II[B)V")
        getSessionId = JavaMethod("()[B")
        close = JavaMethod("()V")