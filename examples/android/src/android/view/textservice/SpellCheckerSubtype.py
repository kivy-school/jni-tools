from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SpellCheckerSubtype"]

class SpellCheckerSubtype(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/textservice/SpellCheckerSubtype"
    __javaconstructor__ = [("(ILjava/lang/String;Ljava/lang/String;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getNameResId = JavaMethod("()I")
    getLocale = JavaMethod("()Ljava/lang/String;")
    getLanguageTag = JavaMethod("()Ljava/lang/String;")
    getExtraValue = JavaMethod("()Ljava/lang/String;")
    containsExtraValueKey = JavaMethod("(Ljava/lang/String;)Z")
    getExtraValueOf = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    getDisplayName = JavaMethod("(Landroid/content/Context;Ljava/lang/String;Landroid/content/pm/ApplicationInfo;)Ljava/lang/CharSequence;")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")