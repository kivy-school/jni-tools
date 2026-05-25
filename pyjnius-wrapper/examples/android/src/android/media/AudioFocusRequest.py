from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AudioFocusRequest"]

class AudioFocusRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/AudioFocusRequest"
    getAudioAttributes = JavaMethod("()Landroid/media/AudioAttributes;")
    getFocusGain = JavaMethod("()I")
    willPauseWhenDucked = JavaMethod("()Z")
    acceptsDelayedFocusGain = JavaMethod("()Z")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/AudioFocusRequest/Builder"
        __javaconstructor__ = [("(I)V", False), ("(Landroid/media/AudioFocusRequest;)V", False)]
        setFocusGain = JavaMethod("(I)Landroid/media/AudioFocusRequest$Builder;")
        setOnAudioFocusChangeListener = JavaMultipleMethod([("(Landroid/media/AudioManager$OnAudioFocusChangeListener;)Landroid/media/AudioFocusRequest$Builder;", False, False), ("(Landroid/media/AudioManager$OnAudioFocusChangeListener;Landroid/os/Handler;)Landroid/media/AudioFocusRequest$Builder;", False, False)])
        setAudioAttributes = JavaMethod("(Landroid/media/AudioAttributes;)Landroid/media/AudioFocusRequest$Builder;")
        setWillPauseWhenDucked = JavaMethod("(Z)Landroid/media/AudioFocusRequest$Builder;")
        setAcceptsDelayedFocusGain = JavaMethod("(Z)Landroid/media/AudioFocusRequest$Builder;")
        setForceDucking = JavaMethod("(Z)Landroid/media/AudioFocusRequest$Builder;")
        build = JavaMethod("()Landroid/media/AudioFocusRequest;")