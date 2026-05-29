from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TranslationManager"]

class TranslationManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/translation/TranslationManager"
    addOnDeviceTranslationCapabilityUpdateListener = JavaMethod("(Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
    createOnDeviceTranslator = JavaMethod("(Landroid/view/translation/TranslationContext;Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
    getOnDeviceTranslationCapabilities = JavaMethod("(II)Ljava/util/Set;")
    getOnDeviceTranslationSettingsActivityIntent = JavaMethod("()Landroid/app/PendingIntent;")
    removeOnDeviceTranslationCapabilityUpdateListener = JavaMethod("(Ljava/util/function/Consumer;)V")