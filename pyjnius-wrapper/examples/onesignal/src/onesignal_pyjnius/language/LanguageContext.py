from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LanguageContext"]

class LanguageContext(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/language/LanguageContext"
    __javaconstructor__ = [("(Lcom/onesignal/OSSharedPreferences;)V", False)]
    getInstance = JavaStaticMethod("()Lcom/onesignal/language/LanguageContext;")
    setStrategy = JavaMethod("(Lcom/onesignal/language/LanguageProvider;)V")
    getLanguage = JavaMethod("()Ljava/lang/String;")