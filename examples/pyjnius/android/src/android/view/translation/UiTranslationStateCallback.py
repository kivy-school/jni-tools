from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["UiTranslationStateCallback"]

class UiTranslationStateCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/translation/UiTranslationStateCallback"
    onFinished = JavaMultipleMethod([("()V", False, False), ("(Ljava/lang/String;)V", False, False)])
    onPaused = JavaMultipleMethod([("(Ljava/lang/String;)V", False, False), ("()V", False, False)])
    onResumed = JavaMultipleMethod([("(Landroid/icu/util/ULocale;Landroid/icu/util/ULocale;Ljava/lang/String;)V", False, False), ("(Landroid/icu/util/ULocale;Landroid/icu/util/ULocale;)V", False, False)])
    onStarted = JavaMultipleMethod([("(Landroid/icu/util/ULocale;Landroid/icu/util/ULocale;)V", False, False), ("(Landroid/icu/util/ULocale;Landroid/icu/util/ULocale;Ljava/lang/String;)V", False, False)])