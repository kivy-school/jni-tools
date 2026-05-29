from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SoundPool"]

class SoundPool(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/SoundPool"
    __javaconstructor__ = [("(III)V", False)]
    release = JavaMethod("()V")
    finalize = JavaMethod("()V")
    load = JavaMultipleMethod([("(Ljava/lang/String;I)I", False, False), ("(Landroid/content/Context;II)I", False, False), ("(Landroid/content/res/AssetFileDescriptor;I)I", False, False), ("(Ljava/io/FileDescriptor;JJI)I", False, False)])
    unload = JavaMethod("(I)Z")
    play = JavaMethod("(IFFIIF)I")
    pause = JavaMethod("(I)V")
    resume = JavaMethod("(I)V")
    autoPause = JavaMethod("()V")
    autoResume = JavaMethod("()V")
    stop = JavaMethod("(I)V")
    setVolume = JavaMethod("(IFF)V")
    setPriority = JavaMethod("(II)V")
    setLoop = JavaMethod("(II)V")
    setRate = JavaMethod("(IF)V")
    setOnLoadCompleteListener = JavaMethod("(Landroid/media/SoundPool$OnLoadCompleteListener;)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/SoundPool/Builder"
        __javaconstructor__ = [("()V", False)]
        setMaxStreams = JavaMethod("(I)Landroid/media/SoundPool$Builder;")
        setAudioAttributes = JavaMethod("(Landroid/media/AudioAttributes;)Landroid/media/SoundPool$Builder;")
        setAudioSessionId = JavaMethod("(I)Landroid/media/SoundPool$Builder;")
        setContext = JavaMethod("(Landroid/content/Context;)Landroid/media/SoundPool$Builder;")
        build = JavaMethod("()Landroid/media/SoundPool;")

    class OnLoadCompleteListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/SoundPool/OnLoadCompleteListener"
        onLoadComplete = JavaMethod("(Landroid/media/SoundPool;II)V")