from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["JetPlayer"]

class JetPlayer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/JetPlayer"
    getJetPlayer = JavaStaticMethod("()Landroid/media/JetPlayer;")
    clone = JavaMethod("()Ljava/lang/Object;")
    finalize = JavaMethod("()V")
    release = JavaMethod("()V")
    getMaxTracks = JavaStaticMethod("()I")
    loadJetFile = JavaMultipleMethod([("(Ljava/lang/String;)Z", False, False), ("(Landroid/content/res/AssetFileDescriptor;)Z", False, False)])
    closeJetFile = JavaMethod("()Z")
    play = JavaMethod("()Z")
    pause = JavaMethod("()Z")
    queueJetSegment = JavaMethod("(IIIIIB)Z")
    queueJetSegmentMuteArray = JavaMethod("(IIII[ZB)Z")
    setMuteFlags = JavaMethod("(IZ)Z")
    setMuteArray = JavaMethod("([ZZ)Z")
    setMuteFlag = JavaMethod("(IZZ)Z")
    triggerClip = JavaMethod("(I)Z")
    clearQueue = JavaMethod("()Z")
    setEventListener = JavaMultipleMethod([("(Landroid/media/JetPlayer$OnJetEventListener;)V", False, False), ("(Landroid/media/JetPlayer$OnJetEventListener;Landroid/os/Handler;)V", False, False)])

    class OnJetEventListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/JetPlayer/OnJetEventListener"
        onJetEvent = JavaMethod("(Landroid/media/JetPlayer;SBBBB)V")
        onJetUserIdUpdate = JavaMethod("(Landroid/media/JetPlayer;II)V")
        onJetNumQueuedSegmentUpdate = JavaMethod("(Landroid/media/JetPlayer;I)V")
        onJetPauseUpdate = JavaMethod("(Landroid/media/JetPlayer;I)V")