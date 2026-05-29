from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["JetPlayer"]

class JetPlayer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/JetPlayer"
    setEventListener = JavaMultipleMethod([("(Landroid/media/JetPlayer$OnJetEventListener;)V", False, False), ("(Landroid/media/JetPlayer$OnJetEventListener;Landroid/os/Handler;)V", False, False)])
    getJetPlayer = JavaStaticMethod("()Landroid/media/JetPlayer;")
    closeJetFile = JavaMethod("()Z")
    getMaxTracks = JavaStaticMethod("()I")
    loadJetFile = JavaMultipleMethod([("(Ljava/lang/String;)Z", False, False), ("(Landroid/content/res/AssetFileDescriptor;)Z", False, False)])
    queueJetSegment = JavaMethod("(IIIIIB)Z")
    clearQueue = JavaMethod("()Z")
    queueJetSegmentMuteArray = JavaMethod("(IIII[ZB)Z")
    setMuteArray = JavaMethod("([ZZ)Z")
    setMuteFlag = JavaMethod("(IZZ)Z")
    setMuteFlags = JavaMethod("(IZ)Z")
    triggerClip = JavaMethod("(I)Z")
    clone = JavaMethod("()Ljava/lang/Object;")
    release = JavaMethod("()V")
    pause = JavaMethod("()Z")
    play = JavaMethod("()Z")

    class OnJetEventListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/JetPlayer$OnJetEventListener"
        onJetEvent = JavaMethod("(Landroid/media/JetPlayer;SBBBB)V")
        onJetNumQueuedSegmentUpdate = JavaMethod("(Landroid/media/JetPlayer;I)V")
        onJetPauseUpdate = JavaMethod("(Landroid/media/JetPlayer;I)V")
        onJetUserIdUpdate = JavaMethod("(Landroid/media/JetPlayer;II)V")