from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LocaleConfig"]

class LocaleConfig(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/LocaleConfig"
    __javaconstructor__ = [("(Landroid/content/Context;)V", False), ("(Landroid/os/LocaleList;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    STATUS_NOT_SPECIFIED = JavaStaticField("I")
    STATUS_PARSING_FAILED = JavaStaticField("I")
    STATUS_SUCCESS = JavaStaticField("I")
    TAG_LOCALE = JavaStaticField("Ljava/lang/String;")
    TAG_LOCALE_CONFIG = JavaStaticField("Ljava/lang/String;")
    fromContextIgnoringOverride = JavaStaticMethod("(Landroid/content/Context;)Landroid/app/LocaleConfig;")
    getSupportedLocales = JavaMethod("()Landroid/os/LocaleList;")
    getDefaultLocale = JavaMethod("()Ljava/util/Locale;")
    getStatus = JavaMethod("()I")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")