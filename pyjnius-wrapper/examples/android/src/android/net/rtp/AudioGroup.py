from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AudioGroup"]

class AudioGroup(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/rtp/AudioGroup"
    __javaconstructor__ = [("()V", False), ("(Landroid/content/Context;)V", False)]
    MODE_ECHO_SUPPRESSION = JavaStaticField("I")
    MODE_MUTED = JavaStaticField("I")
    MODE_NORMAL = JavaStaticField("I")
    MODE_ON_HOLD = JavaStaticField("I")
    getStreams = JavaMethod("()[Landroid/net/rtp/AudioStream;")
    getMode = JavaMethod("()I")
    setMode = JavaMethod("(I)V")
    sendDtmf = JavaMethod("(I)V")
    clear = JavaMethod("()V")
    finalize = JavaMethod("()V")