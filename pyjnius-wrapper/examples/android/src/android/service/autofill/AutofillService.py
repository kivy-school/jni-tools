from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["AutofillService"]

class AutofillService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/autofill/AutofillService"
    __javaconstructor__ = [("()V", False)]
    EXTRA_FILL_RESPONSE = JavaStaticField("Ljava/lang/String;")
    SERVICE_INTERFACE = JavaStaticField("Ljava/lang/String;")
    SERVICE_META_DATA = JavaStaticField("Ljava/lang/String;")
    onCreate = JavaMethod("()V")
    onBind = JavaMethod("(Landroid/content/Intent;)Landroid/os/IBinder;")
    onConnected = JavaMethod("()V")
    onFillRequest = JavaMethod("(Landroid/service/autofill/FillRequest;Landroid/os/CancellationSignal;Landroid/service/autofill/FillCallback;)V")
    onSaveRequest = JavaMethod("(Landroid/service/autofill/SaveRequest;Landroid/service/autofill/SaveCallback;)V")
    onSavedDatasetsInfoRequest = JavaMethod("(Landroid/service/autofill/SavedDatasetsInfoCallback;)V")
    onDisconnected = JavaMethod("()V")
    getFillEventHistory = JavaMethod("()Landroid/service/autofill/FillEventHistory;")