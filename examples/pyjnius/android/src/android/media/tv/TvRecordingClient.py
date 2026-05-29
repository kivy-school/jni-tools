from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TvRecordingClient"]

class TvRecordingClient(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/tv/TvRecordingClient"
    __javaconstructor__ = [("(Landroid/content/Context;Ljava/lang/String;Landroid/media/tv/TvRecordingClient$RecordingCallback;Landroid/os/Handler;)V", False)]
    setTvInteractiveAppView = JavaMethod("(Landroid/media/tv/interactive/TvInteractiveAppView;Ljava/lang/String;)V")
    tune = JavaMultipleMethod([("(Ljava/lang/String;Landroid/net/Uri;)V", False, False), ("(Ljava/lang/String;Landroid/net/Uri;Landroid/os/Bundle;)V", False, False)])
    release = JavaMethod("()V")
    startRecording = JavaMultipleMethod([("(Landroid/net/Uri;)V", False, False), ("(Landroid/net/Uri;Landroid/os/Bundle;)V", False, False)])
    stopRecording = JavaMethod("()V")
    pauseRecording = JavaMultipleMethod([("()V", False, False), ("(Landroid/os/Bundle;)V", False, False)])
    resumeRecording = JavaMultipleMethod([("()V", False, False), ("(Landroid/os/Bundle;)V", False, False)])
    sendAppPrivateCommand = JavaMethod("(Ljava/lang/String;Landroid/os/Bundle;)V")

    class RecordingCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/tv/TvRecordingClient/RecordingCallback"
        __javaconstructor__ = [("()V", False)]
        onConnectionFailed = JavaMethod("(Ljava/lang/String;)V")
        onDisconnected = JavaMethod("(Ljava/lang/String;)V")
        onTuned = JavaMethod("(Landroid/net/Uri;)V")
        onRecordingStopped = JavaMethod("(Landroid/net/Uri;)V")
        onError = JavaMethod("(I)V")