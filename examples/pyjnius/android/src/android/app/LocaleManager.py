from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LocaleManager"]

class LocaleManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/LocaleManager"
    getSystemLocales = JavaMethod("()Landroid/os/LocaleList;")
    getApplicationLocales = JavaMultipleMethod([("(Ljava/lang/String;)Landroid/os/LocaleList;", False, False), ("()Landroid/os/LocaleList;", False, False)])
    getOverrideLocaleConfig = JavaMethod("()Landroid/app/LocaleConfig;")
    setApplicationLocales = JavaMethod("(Landroid/os/LocaleList;)V")
    setOverrideLocaleConfig = JavaMethod("(Landroid/app/LocaleConfig;)V")