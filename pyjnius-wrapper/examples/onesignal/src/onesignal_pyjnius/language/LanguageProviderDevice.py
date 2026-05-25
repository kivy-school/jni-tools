from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LanguageProviderDevice"]

class LanguageProviderDevice(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/onesignal/language/LanguageProviderDevice"
    __javaconstructor__ = [("()V", False)]
    getLanguage = JavaMethod("()Ljava/lang/String;")