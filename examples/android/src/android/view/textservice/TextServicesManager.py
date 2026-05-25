from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["TextServicesManager"]

class TextServicesManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/textservice/TextServicesManager"
    newSpellCheckerSession = JavaMultipleMethod([("(Landroid/os/Bundle;Ljava/util/Locale;Landroid/view/textservice/SpellCheckerSession$SpellCheckerSessionListener;Z)Landroid/view/textservice/SpellCheckerSession;", False, False), ("(Landroid/view/textservice/SpellCheckerSession$SpellCheckerSessionParams;Ljava/util/concurrent/Executor;Landroid/view/textservice/SpellCheckerSession$SpellCheckerSessionListener;)Landroid/view/textservice/SpellCheckerSession;", False, False)])
    getEnabledSpellCheckerInfos = JavaMethod("()Ljava/util/List;")
    getCurrentSpellCheckerInfo = JavaMethod("()Landroid/view/textservice/SpellCheckerInfo;")
    isSpellCheckerEnabled = JavaMethod("()Z")