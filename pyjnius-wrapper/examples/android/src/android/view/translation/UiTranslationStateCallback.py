from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UiTranslationStateCallback"]

class UiTranslationStateCallback(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/translation/UiTranslationStateCallback"
    onStarted = JavaMultipleMethod([("(Landroid/icu/util/ULocale;Landroid/icu/util/ULocale;)V", False, False), ("(Landroid/icu/util/ULocale;Landroid/icu/util/ULocale;Ljava/lang/String;)V", False, False)])
    onPaused = JavaMultipleMethod([("()V", False, False), ("(Ljava/lang/String;)V", False, False)])
    onResumed = JavaMultipleMethod([("(Landroid/icu/util/ULocale;Landroid/icu/util/ULocale;)V", False, False), ("(Landroid/icu/util/ULocale;Landroid/icu/util/ULocale;Ljava/lang/String;)V", False, False)])
    onFinished = JavaMultipleMethod([("()V", False, False), ("(Ljava/lang/String;)V", False, False)])