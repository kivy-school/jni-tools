from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AudioGroup"]

class AudioGroup(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/net/rtp/AudioGroup"
    __javaconstructor__ = [("()V", False), ("(Landroid/content/Context;)V", False)]
    MODE_ECHO_SUPPRESSION = JavaStaticField("I")
    MODE_MUTED = JavaStaticField("I")
    MODE_NORMAL = JavaStaticField("I")
    MODE_ON_HOLD = JavaStaticField("I")
    sendDtmf = JavaMethod("(I)V")
    getStreams = JavaMethod("()[Landroid/net/rtp/AudioStream;")
    clear = JavaMethod("()V")
    getMode = JavaMethod("()I")
    setMode = JavaMethod("(I)V")