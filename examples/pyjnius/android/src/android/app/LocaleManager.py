from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LocaleManager"]

class LocaleManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/LocaleManager"
    setApplicationLocales = JavaMethod("(Landroid/os/LocaleList;)V")
    getApplicationLocales = JavaMultipleMethod([("()Landroid/os/LocaleList;", False, False), ("(Ljava/lang/String;)Landroid/os/LocaleList;", False, False)])
    getSystemLocales = JavaMethod("()Landroid/os/LocaleList;")
    setOverrideLocaleConfig = JavaMethod("(Landroid/app/LocaleConfig;)V")
    getOverrideLocaleConfig = JavaMethod("()Landroid/app/LocaleConfig;")