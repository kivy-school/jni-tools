from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SpellCheckerSubtype"]

class SpellCheckerSubtype(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/textservice/SpellCheckerSubtype"
    __javaconstructor__ = [("(ILjava/lang/String;Ljava/lang/String;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getLocale = JavaMethod("()Ljava/lang/String;")
    getDisplayName = JavaMethod("(Landroid/content/Context;Ljava/lang/String;Landroid/content/pm/ApplicationInfo;)Ljava/lang/CharSequence;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getExtraValue = JavaMethod("()Ljava/lang/String;")
    containsExtraValueKey = JavaMethod("(Ljava/lang/String;)Z")
    getExtraValueOf = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    getLanguageTag = JavaMethod("()Ljava/lang/String;")
    getNameResId = JavaMethod("()I")