from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LanguageProvider"]

class LanguageProvider(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/language/LanguageProvider"
    getLanguage = JavaMethod("()Ljava/lang/String;")