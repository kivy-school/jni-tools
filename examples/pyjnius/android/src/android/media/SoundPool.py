from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SoundPool"]

class SoundPool(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/SoundPool"
    __javaconstructor__ = [("(III)V", False)]
    setVolume = JavaMethod("(IFF)V")
    autoResume = JavaMethod("()V")
    load = JavaMultipleMethod([("(Ljava/lang/String;I)I", False, False), ("(Ljava/io/FileDescriptor;JJI)I", False, False), ("(Landroid/content/res/AssetFileDescriptor;I)I", False, False), ("(Landroid/content/Context;II)I", False, False)])
    setPriority = JavaMethod("(II)V")
    release = JavaMethod("()V")
    pause = JavaMethod("(I)V")
    resume = JavaMethod("(I)V")
    unload = JavaMethod("(I)Z")
    stop = JavaMethod("(I)V")
    play = JavaMethod("(IFFIIF)I")
    autoPause = JavaMethod("()V")
    setLoop = JavaMethod("(II)V")
    setOnLoadCompleteListener = JavaMethod("(Landroid/media/SoundPool$OnLoadCompleteListener;)V")
    setRate = JavaMethod("(IF)V")

    class OnLoadCompleteListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/SoundPool$OnLoadCompleteListener"
        onLoadComplete = JavaMethod("(Landroid/media/SoundPool;II)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/SoundPool$Builder"
        __javaconstructor__ = [("()V", False)]
        setContext = JavaMethod("(Landroid/content/Context;)Landroid/media/SoundPool$Builder;")
        setAudioSessionId = JavaMethod("(I)Landroid/media/SoundPool$Builder;")
        setMaxStreams = JavaMethod("(I)Landroid/media/SoundPool$Builder;")
        build = JavaMethod("()Landroid/media/SoundPool;")
        setAudioAttributes = JavaMethod("(Landroid/media/AudioAttributes;)Landroid/media/SoundPool$Builder;")