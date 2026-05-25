from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UiTranslationManager"]

class UiTranslationManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/translation/UiTranslationManager"
    registerUiTranslationStateCallback = JavaMethod("(Ljava/util/concurrent/Executor;Landroid/view/translation/UiTranslationStateCallback;)V")
    unregisterUiTranslationStateCallback = JavaMethod("(Landroid/view/translation/UiTranslationStateCallback;)V")