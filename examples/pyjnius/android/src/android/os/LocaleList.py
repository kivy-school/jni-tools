from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LocaleList"]

class LocaleList(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/os/LocaleList"
    __javaconstructor__ = [("([Ljava/util/Locale;)V", True)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    size = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    indexOf = JavaMethod("(Ljava/util/Locale;)I")
    isEmpty = JavaMethod("()Z")
    get = JavaMethod("(I)Ljava/util/Locale;")
    getDefault = JavaStaticMethod("()Landroid/os/LocaleList;")
    getFirstMatch = JavaMethod("([Ljava/lang/String;)Ljava/util/Locale;")
    forLanguageTags = JavaStaticMethod("(Ljava/lang/String;)Landroid/os/LocaleList;")
    getAdjustedDefault = JavaStaticMethod("()Landroid/os/LocaleList;")
    getEmptyLocaleList = JavaStaticMethod("()Landroid/os/LocaleList;")
    isPseudoLocale = JavaStaticMethod("(Landroid/icu/util/ULocale;)Z")
    matchesLanguageAndScript = JavaStaticMethod("(Ljava/util/Locale;Ljava/util/Locale;)Z")
    toLanguageTags = JavaMethod("()Ljava/lang/String;")
    setDefault = JavaStaticMethod("(Landroid/os/LocaleList;)V")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")