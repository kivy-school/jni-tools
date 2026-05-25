from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InputMethodSubtype"]

class InputMethodSubtype(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inputmethod/InputMethodSubtype"
    __javaconstructor__ = [("(IILjava/lang/String;Ljava/lang/String;Ljava/lang/String;ZZ)V", False), ("(IILjava/lang/String;Ljava/lang/String;Ljava/lang/String;ZZI)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getNameResId = JavaMethod("()I")
    getNameOverride = JavaMethod("()Ljava/lang/CharSequence;")
    getPhysicalKeyboardHintLanguageTag = JavaMethod("()Landroid/icu/util/ULocale;")
    getPhysicalKeyboardHintLayoutType = JavaMethod("()Ljava/lang/String;")
    getIconResId = JavaMethod("()I")
    getLocale = JavaMethod("()Ljava/lang/String;")
    getLanguageTag = JavaMethod("()Ljava/lang/String;")
    getMode = JavaMethod("()Ljava/lang/String;")
    getExtraValue = JavaMethod("()Ljava/lang/String;")
    isAuxiliary = JavaMethod("()Z")
    overridesImplicitlyEnabledSubtype = JavaMethod("()Z")
    isAsciiCapable = JavaMethod("()Z")
    getDisplayName = JavaMethod("(Landroid/content/Context;Ljava/lang/String;Landroid/content/pm/ApplicationInfo;)Ljava/lang/CharSequence;")
    containsExtraValueKey = JavaMethod("(Ljava/lang/String;)Z")
    getExtraValueOf = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    describeContents = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")

    class InputMethodSubtypeBuilder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/inputmethod/InputMethodSubtype/InputMethodSubtypeBuilder"
        __javaconstructor__ = [("()V", False)]
        setIsAuxiliary = JavaMethod("(Z)Landroid/view/inputmethod/InputMethodSubtype$InputMethodSubtypeBuilder;")
        setOverridesImplicitlyEnabledSubtype = JavaMethod("(Z)Landroid/view/inputmethod/InputMethodSubtype$InputMethodSubtypeBuilder;")
        setIsAsciiCapable = JavaMethod("(Z)Landroid/view/inputmethod/InputMethodSubtype$InputMethodSubtypeBuilder;")
        setSubtypeIconResId = JavaMethod("(I)Landroid/view/inputmethod/InputMethodSubtype$InputMethodSubtypeBuilder;")
        setSubtypeNameResId = JavaMethod("(I)Landroid/view/inputmethod/InputMethodSubtype$InputMethodSubtypeBuilder;")
        setSubtypeNameOverride = JavaMethod("(Ljava/lang/CharSequence;)Landroid/view/inputmethod/InputMethodSubtype$InputMethodSubtypeBuilder;")
        setPhysicalKeyboardHint = JavaMethod("(Landroid/icu/util/ULocale;Ljava/lang/String;)Landroid/view/inputmethod/InputMethodSubtype$InputMethodSubtypeBuilder;")
        setSubtypeId = JavaMethod("(I)Landroid/view/inputmethod/InputMethodSubtype$InputMethodSubtypeBuilder;")
        setSubtypeLocale = JavaMethod("(Ljava/lang/String;)Landroid/view/inputmethod/InputMethodSubtype$InputMethodSubtypeBuilder;")
        setLanguageTag = JavaMethod("(Ljava/lang/String;)Landroid/view/inputmethod/InputMethodSubtype$InputMethodSubtypeBuilder;")
        setSubtypeMode = JavaMethod("(Ljava/lang/String;)Landroid/view/inputmethod/InputMethodSubtype$InputMethodSubtypeBuilder;")
        setSubtypeExtraValue = JavaMethod("(Ljava/lang/String;)Landroid/view/inputmethod/InputMethodSubtype$InputMethodSubtypeBuilder;")
        build = JavaMethod("()Landroid/view/inputmethod/InputMethodSubtype;")