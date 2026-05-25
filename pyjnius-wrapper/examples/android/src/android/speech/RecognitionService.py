from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RecognitionService"]

class RecognitionService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/speech/RecognitionService"
    __javaconstructor__ = [("()V", False)]
    SERVICE_INTERFACE = JavaStaticField("Ljava/lang/String;")
    SERVICE_META_DATA = JavaStaticField("Ljava/lang/String;")
    onStartListening = JavaMethod("(Landroid/content/Intent;Landroid/speech/RecognitionService$Callback;)V")
    onCancel = JavaMethod("(Landroid/speech/RecognitionService$Callback;)V")
    onStopListening = JavaMethod("(Landroid/speech/RecognitionService$Callback;)V")
    onCheckRecognitionSupport = JavaMultipleMethod([("(Landroid/content/Intent;Landroid/speech/RecognitionService$SupportCallback;)V", False, False), ("(Landroid/content/Intent;Landroid/content/AttributionSource;Landroid/speech/RecognitionService$SupportCallback;)V", False, False)])
    onTriggerModelDownload = JavaMultipleMethod([("(Landroid/content/Intent;)V", False, False), ("(Landroid/content/Intent;Landroid/content/AttributionSource;)V", False, False), ("(Landroid/content/Intent;Landroid/content/AttributionSource;Landroid/speech/ModelDownloadListener;)V", False, False)])
    createContext = JavaMethod("(Landroid/content/ContextParams;)Landroid/content/Context;")
    onBind = JavaMethod("(Landroid/content/Intent;)Landroid/os/IBinder;")
    onDestroy = JavaMethod("()V")
    getMaxConcurrentSessionsCount = JavaMethod("()I")

    class Callback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/speech/RecognitionService/Callback"
        beginningOfSpeech = JavaMethod("()V")
        bufferReceived = JavaMethod("([B)V")
        endOfSpeech = JavaMethod("()V")
        error = JavaMethod("(I)V")
        partialResults = JavaMethod("(Landroid/os/Bundle;)V")
        readyForSpeech = JavaMethod("(Landroid/os/Bundle;)V")
        results = JavaMethod("(Landroid/os/Bundle;)V")
        rmsChanged = JavaMethod("(F)V")
        segmentResults = JavaMethod("(Landroid/os/Bundle;)V")
        endOfSegmentedSession = JavaMethod("()V")
        languageDetection = JavaMethod("(Landroid/os/Bundle;)V")
        getCallingUid = JavaMethod("()I")
        getCallingAttributionSource = JavaMethod("()Landroid/content/AttributionSource;")

    class SupportCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/speech/RecognitionService/SupportCallback"
        onSupportResult = JavaMethod("(Landroid/speech/RecognitionSupport;)V")
        onError = JavaMethod("(I)V")