from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SettingsPreferenceServiceClient"]

class SettingsPreferenceServiceClient(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/settings/preferences/SettingsPreferenceServiceClient"
    __javaconstructor__ = [("(Landroid/content/Context;Ljava/lang/String;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V", False)]
    setPreferenceValue = JavaMethod("(Landroid/service/settings/preferences/SetValueRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    getAllPreferenceMetadata = JavaMethod("(Landroid/service/settings/preferences/MetadataRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    getPreferenceValue = JavaMethod("(Landroid/service/settings/preferences/GetValueRequest;Ljava/util/concurrent/Executor;Landroid/os/OutcomeReceiver;)V")
    close = JavaMethod("()V")