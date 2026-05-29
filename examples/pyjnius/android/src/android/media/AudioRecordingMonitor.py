from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AudioRecordingMonitor"]

class AudioRecordingMonitor(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/AudioRecordingMonitor"
    registerAudioRecordingCallback = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/media/AudioManager$AudioRecordingCallback;)V")
    unregisterAudioRecordingCallback = JavaMethod("(Landroid/media/AudioManager$AudioRecordingCallback;)V")
    getActiveRecordingConfiguration = JavaMethod("()Landroid/media/AudioRecordingConfiguration;")