from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TvRecordingClient"]

class TvRecordingClient(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/tv/TvRecordingClient"
    __javaconstructor__ = [("(Landroid/content/Context;Ljava/lang/String;Landroid/media/tv/TvRecordingClient$RecordingCallback;Landroid/os/Handler;)V", False)]
    sendAppPrivateCommand = JavaMethod("(Ljava/lang/String;Landroid/os/Bundle;)V")
    stopRecording = JavaMethod("()V")
    pauseRecording = JavaMultipleMethod([("()V", False, False), ("(Landroid/os/Bundle;)V", False, False)])
    startRecording = JavaMultipleMethod([("(Landroid/net/Uri;)V", False, False), ("(Landroid/net/Uri;Landroid/os/Bundle;)V", False, False)])
    setTvInteractiveAppView = JavaMethod("(Landroid/media/tv/interactive/TvInteractiveAppView;Ljava/lang/String;)V")
    tune = JavaMultipleMethod([("(Ljava/lang/String;Landroid/net/Uri;)V", False, False), ("(Ljava/lang/String;Landroid/net/Uri;Landroid/os/Bundle;)V", False, False)])
    release = JavaMethod("()V")
    resumeRecording = JavaMultipleMethod([("(Landroid/os/Bundle;)V", False, False), ("()V", False, False)])

    class RecordingCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/tv/TvRecordingClient$RecordingCallback"
        __javaconstructor__ = [("()V", False)]
        onDisconnected = JavaMethod("(Ljava/lang/String;)V")
        onConnectionFailed = JavaMethod("(Ljava/lang/String;)V")
        onRecordingStopped = JavaMethod("(Landroid/net/Uri;)V")
        onTuned = JavaMethod("(Landroid/net/Uri;)V")
        onError = JavaMethod("(I)V")