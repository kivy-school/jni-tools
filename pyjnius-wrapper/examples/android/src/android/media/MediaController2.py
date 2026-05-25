from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaController2"]

class MediaController2(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/MediaController2"
    close = JavaMethod("()V")
    getConnectedToken = JavaMethod("()Landroid/media/Session2Token;")
    isPlaybackActive = JavaMethod("()Z")
    sendSessionCommand = JavaMethod("(Landroid/media/Session2Command;Landroid/os/Bundle;)Ljava/lang/Object;")
    cancelSessionCommand = JavaMethod("(Ljava/lang/Object;)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaController2/Builder"
        __javaconstructor__ = [("(Landroid/content/Context;Landroid/media/Session2Token;)V", False)]
        setConnectionHints = JavaMethod("(Landroid/os/Bundle;)Landroid/media/MediaController2$Builder;")
        setControllerCallback = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/media/MediaController2$ControllerCallback;)Landroid/media/MediaController2$Builder;")
        build = JavaMethod("()Landroid/media/MediaController2;")

    class ControllerCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaController2/ControllerCallback"
        __javaconstructor__ = [("()V", False)]
        onConnected = JavaMethod("(Landroid/media/MediaController2;Landroid/media/Session2CommandGroup;)V")
        onDisconnected = JavaMethod("(Landroid/media/MediaController2;)V")
        onPlaybackActiveChanged = JavaMethod("(Landroid/media/MediaController2;Z)V")
        onSessionCommand = JavaMethod("(Landroid/media/MediaController2;Landroid/media/Session2Command;Landroid/os/Bundle;)Landroid/media/Session2Command$Result;")
        onCommandResult = JavaMethod("(Landroid/media/MediaController2;Ljava/lang/Object;Landroid/media/Session2Command;Landroid/media/Session2Command$Result;)V")