from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LanguageProviderAppDefined"]

class LanguageProviderAppDefined(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/language/LanguageProviderAppDefined"
    __javaconstructor__ = [("(Lcom/onesignal/OSSharedPreferences;)V", False)]
    PREFS_OS_LANGUAGE = JavaStaticField("Ljava/lang/String;")
    setLanguage = JavaMethod("(Ljava/lang/String;)V")
    getLanguage = JavaMethod("()Ljava/lang/String;")