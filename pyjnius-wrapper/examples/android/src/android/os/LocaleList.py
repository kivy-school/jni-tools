from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LocaleList"]

class LocaleList(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/LocaleList"
    __javaconstructor__ = [("([Ljava/util/Locale;)V", True)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    get = JavaMethod("(I)Ljava/util/Locale;")
    isEmpty = JavaMethod("()Z")
    size = JavaMethod("()I")
    indexOf = JavaMethod("(Ljava/util/Locale;)I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    toLanguageTags = JavaMethod("()Ljava/lang/String;")
    getEmptyLocaleList = JavaStaticMethod("()Landroid/os/LocaleList;")
    forLanguageTags = JavaStaticMethod("(Ljava/lang/String;)Landroid/os/LocaleList;")
    isPseudoLocale = JavaStaticMethod("(Landroid/icu/util/ULocale;)Z")
    matchesLanguageAndScript = JavaStaticMethod("(Ljava/util/Locale;Ljava/util/Locale;)Z")
    getFirstMatch = JavaMethod("([Ljava/lang/String;)Ljava/util/Locale;")
    getDefault = JavaStaticMethod("()Landroid/os/LocaleList;")
    getAdjustedDefault = JavaStaticMethod("()Landroid/os/LocaleList;")
    setDefault = JavaStaticMethod("(Landroid/os/LocaleList;)V")