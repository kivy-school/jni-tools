from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AudioRecordingMonitor"]

class AudioRecordingMonitor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/AudioRecordingMonitor"
    getActiveRecordingConfiguration = JavaMethod("()Landroid/media/AudioRecordingConfiguration;")
    registerAudioRecordingCallback = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/media/AudioManager$AudioRecordingCallback;)V")
    unregisterAudioRecordingCallback = JavaMethod("(Landroid/media/AudioManager$AudioRecordingCallback;)V")