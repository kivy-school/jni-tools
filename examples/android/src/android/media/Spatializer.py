from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["Spatializer"]

class Spatializer(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/Spatializer"
    SPATIALIZER_IMMERSIVE_LEVEL_MULTICHANNEL = JavaStaticField("I")
    SPATIALIZER_IMMERSIVE_LEVEL_NONE = JavaStaticField("I")
    SPATIALIZER_IMMERSIVE_LEVEL_OTHER = JavaStaticField("I")
    isEnabled = JavaMethod("()Z")
    isAvailable = JavaMethod("()Z")
    isHeadTrackerAvailable = JavaMethod("()Z")
    addOnHeadTrackerAvailableListener = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/media/Spatializer$OnHeadTrackerAvailableListener;)V")
    removeOnHeadTrackerAvailableListener = JavaMethod("(Landroid/media/Spatializer$OnHeadTrackerAvailableListener;)V")
    getImmersiveAudioLevel = JavaMethod("()I")
    canBeSpatialized = JavaMethod("(Landroid/media/AudioAttributes;Landroid/media/AudioFormat;)Z")
    addOnSpatializerStateChangedListener = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/media/Spatializer$OnSpatializerStateChangedListener;)V")
    removeOnSpatializerStateChangedListener = JavaMethod("(Landroid/media/Spatializer$OnSpatializerStateChangedListener;)V")

    class OnHeadTrackerAvailableListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/Spatializer/OnHeadTrackerAvailableListener"
        onHeadTrackerAvailableChanged = JavaMethod("(Landroid/media/Spatializer;Z)V")

    class OnSpatializerStateChangedListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/Spatializer/OnSpatializerStateChangedListener"
        onSpatializerEnabledChanged = JavaMethod("(Landroid/media/Spatializer;Z)V")
        onSpatializerAvailableChanged = JavaMethod("(Landroid/media/Spatializer;Z)V")