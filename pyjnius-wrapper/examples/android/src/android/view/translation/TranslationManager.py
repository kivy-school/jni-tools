from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TranslationManager"]

class TranslationManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/translation/TranslationManager"
    createOnDeviceTranslator = JavaMethod("(Landroid/view/translation/TranslationContext;Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
    getOnDeviceTranslationCapabilities = JavaMethod("(II)Ljava/util/Set;")
    addOnDeviceTranslationCapabilityUpdateListener = JavaMethod("(Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
    removeOnDeviceTranslationCapabilityUpdateListener = JavaMethod("(Ljava/util/function/Consumer;)V")
    getOnDeviceTranslationSettingsActivityIntent = JavaMethod("()Landroid/app/PendingIntent;")