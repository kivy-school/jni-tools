from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SpellCheckerSession"]

class SpellCheckerSession(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/textservice/SpellCheckerSession"
    SERVICE_META_DATA = JavaStaticField("Ljava/lang/String;")
    isSessionDisconnected = JavaMethod("()Z")
    getSpellChecker = JavaMethod("()Landroid/view/textservice/SpellCheckerInfo;")
    cancel = JavaMethod("()V")
    close = JavaMethod("()V")
    getSentenceSuggestions = JavaMethod("([Landroid/view/textservice/TextInfo;I)V")
    getSuggestions = JavaMultipleMethod([("(Landroid/view/textservice/TextInfo;I)V", False, False), ("([Landroid/view/textservice/TextInfo;IZ)V", False, False)])
    finalize = JavaMethod("()V")

    class SpellCheckerSessionListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/textservice/SpellCheckerSession/SpellCheckerSessionListener"
        onGetSuggestions = JavaMethod("([Landroid/view/textservice/SuggestionsInfo;)V")
        onGetSentenceSuggestions = JavaMethod("([Landroid/view/textservice/SentenceSuggestionsInfo;)V")

    class SpellCheckerSessionParams(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/textservice/SpellCheckerSession/SpellCheckerSessionParams"
        getLocale = JavaMethod("()Ljava/util/Locale;")
        shouldReferToSpellCheckerLanguageSettings = JavaMethod("()Z")
        getSupportedAttributes = JavaMethod("()I")
        getExtras = JavaMethod("()Landroid/os/Bundle;")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/view/textservice/SpellCheckerSession/SpellCheckerSessionParams/Builder"
            __javaconstructor__ = [("()V", False)]
            build = JavaMethod("()Landroid/view/textservice/SpellCheckerSession$SpellCheckerSessionParams;")
            setLocale = JavaMethod("(Ljava/util/Locale;)Landroid/view/textservice/SpellCheckerSession$SpellCheckerSessionParams$Builder;")
            setShouldReferToSpellCheckerLanguageSettings = JavaMethod("(Z)Landroid/view/textservice/SpellCheckerSession$SpellCheckerSessionParams$Builder;")
            setSupportedAttributes = JavaMethod("(I)Landroid/view/textservice/SpellCheckerSession$SpellCheckerSessionParams$Builder;")
            setExtras = JavaMethod("(Landroid/os/Bundle;)Landroid/view/textservice/SpellCheckerSession$SpellCheckerSessionParams$Builder;")