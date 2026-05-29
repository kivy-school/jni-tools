from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SpellCheckerSession"]

class SpellCheckerSession(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/textservice/SpellCheckerSession"
    SERVICE_META_DATA = JavaStaticField("Ljava/lang/String;")
    getSuggestions = JavaMultipleMethod([("(Landroid/view/textservice/TextInfo;I)V", False, False), ("([Landroid/view/textservice/TextInfo;IZ)V", False, False)])
    getSpellChecker = JavaMethod("()Landroid/view/textservice/SpellCheckerInfo;")
    getSentenceSuggestions = JavaMethod("([Landroid/view/textservice/TextInfo;I)V")
    isSessionDisconnected = JavaMethod("()Z")
    close = JavaMethod("()V")
    cancel = JavaMethod("()V")

    class SpellCheckerSessionParams(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/textservice/SpellCheckerSession$SpellCheckerSessionParams"
        getSupportedAttributes = JavaMethod("()I")
        shouldReferToSpellCheckerLanguageSettings = JavaMethod("()Z")
        getLocale = JavaMethod("()Ljava/util/Locale;")
        getExtras = JavaMethod("()Landroid/os/Bundle;")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/view/textservice/SpellCheckerSession$SpellCheckerSessionParams$Builder"
            __javaconstructor__ = [("()V", False)]
            setShouldReferToSpellCheckerLanguageSettings = JavaMethod("(Z)Landroid/view/textservice/SpellCheckerSession$SpellCheckerSessionParams$Builder;")
            setSupportedAttributes = JavaMethod("(I)Landroid/view/textservice/SpellCheckerSession$SpellCheckerSessionParams$Builder;")
            setExtras = JavaMethod("(Landroid/os/Bundle;)Landroid/view/textservice/SpellCheckerSession$SpellCheckerSessionParams$Builder;")
            build = JavaMethod("()Landroid/view/textservice/SpellCheckerSession$SpellCheckerSessionParams;")
            setLocale = JavaMethod("(Ljava/util/Locale;)Landroid/view/textservice/SpellCheckerSession$SpellCheckerSessionParams$Builder;")

    class SpellCheckerSessionListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/textservice/SpellCheckerSession$SpellCheckerSessionListener"
        onGetSuggestions = JavaMethod("([Landroid/view/textservice/SuggestionsInfo;)V")
        onGetSentenceSuggestions = JavaMethod("([Landroid/view/textservice/SentenceSuggestionsInfo;)V")