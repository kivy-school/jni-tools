from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SpellCheckerService"]

class SpellCheckerService(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/textservice/SpellCheckerService"
    __javaconstructor__ = [("()V", False)]
    SERVICE_INTERFACE = JavaStaticField("Ljava/lang/String;")
    onBind = JavaMethod("(Landroid/content/Intent;)Landroid/os/IBinder;")
    createSession = JavaMethod("()Landroid/service/textservice/SpellCheckerService$Session;")

    class Session(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/service/textservice/SpellCheckerService/Session"
        __javaconstructor__ = [("()V", False)]
        onCreate = JavaMethod("()V")
        onGetSuggestions = JavaMethod("(Landroid/view/textservice/TextInfo;I)Landroid/view/textservice/SuggestionsInfo;")
        onGetSuggestionsMultiple = JavaMethod("([Landroid/view/textservice/TextInfo;IZ)[Landroid/view/textservice/SuggestionsInfo;")
        onGetSentenceSuggestionsMultiple = JavaMethod("([Landroid/view/textservice/TextInfo;I)[Landroid/view/textservice/SentenceSuggestionsInfo;")
        onCancel = JavaMethod("()V")
        onClose = JavaMethod("()V")
        getLocale = JavaMethod("()Ljava/lang/String;")
        getBundle = JavaMethod("()Landroid/os/Bundle;")
        getSupportedAttributes = JavaMethod("()I")