from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaCas"]

class MediaCas(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/MediaCas"
    __javaconstructor__ = [("(Landroid/content/Context;ILjava/lang/String;I)V", False), ("(Landroid/content/Context;ILjava/lang/String;ILandroid/os/Handler;Landroid/media/MediaCas$EventListener;)V", False), ("(I)V", False)]
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
    enumeratePlugins = JavaStaticMethod("()[Landroid/media/MediaCas$PluginDescriptor;")
    isSystemIdSupported = JavaStaticMethod("(I)Z")
    processEmm = JavaMultipleMethod([("([B)V", False, False), ("([BII)V", False, False)])
    provision = JavaMethod("(Ljava/lang/String;)V")
    refreshEntitlements = JavaMethod("(I[B)V")
    setEventListener = JavaMethod("(Landroid/media/MediaCas$EventListener;Landroid/os/Handler;)V")
    setPrivateData = JavaMethod("([B)V")
    close = JavaMethod("()V")
    openSession = JavaMultipleMethod([("(II)Landroid/media/MediaCas$Session;", False, False), ("()Landroid/media/MediaCas$Session;", False, False)])
    sendEvent = JavaMethod("(II[B)V")

    class Session(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaCas$Session"
        setPrivateData = JavaMethod("([B)V")
        sendSessionEvent = JavaMethod("(II[B)V")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        close = JavaMethod("()V")
        processEcm = JavaMultipleMethod([("([B)V", False, False), ("([BII)V", False, False)])
        getSessionId = JavaMethod("()[B")

    class PluginDescriptor(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaCas$PluginDescriptor"
        getSystemId = JavaMethod("()I")
        getName = JavaMethod("()Ljava/lang/String;")
        toString = JavaMethod("()Ljava/lang/String;")

    class EventListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaCas$EventListener"
        onPluginStatusUpdate = JavaMethod("(Landroid/media/MediaCas;II)V")
        onResourceLost = JavaMethod("(Landroid/media/MediaCas;)V")
        onSessionEvent = JavaMethod("(Landroid/media/MediaCas;Landroid/media/MediaCas$Session;II[B)V")
        onEvent = JavaMethod("(Landroid/media/MediaCas;II[B)V")