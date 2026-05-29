from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InputMethodInfo"]

class InputMethodInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inputmethod/InputMethodInfo"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/content/pm/ResolveInfo;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/CharSequence;Ljava/lang/String;)V", False)]
    ACTION_IME_LANGUAGE_SETTINGS = JavaStaticField("Ljava/lang/String;")
    ACTION_STYLUS_HANDWRITING_SETTINGS = JavaStaticField("Ljava/lang/String;")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getConfigChanges = JavaMethod("()I")
    getSubtypeAt = JavaMethod("(I)Landroid/view/inputmethod/InputMethodSubtype;")
    supportsConnectionlessStylusHandwriting = JavaMethod("()Z")
    supportsStylusHandwriting = JavaMethod("()Z")
    suppressesSpellChecker = JavaMethod("()Z")
    getSubtypeCount = JavaMethod("()I")
    createImeLanguageSettingsActivityIntent = JavaMethod("()Landroid/content/Intent;")
    createStylusHandwritingSettingsActivityIntent = JavaMethod("()Landroid/content/Intent;")
    getIsDefaultResourceId = JavaMethod("()I")
    shouldShowInInputMethodPicker = JavaMethod("()Z")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getPackageName = JavaMethod("()Ljava/lang/String;")
    getId = JavaMethod("()Ljava/lang/String;")
    dump = JavaMethod("(Landroid/util/Printer;Ljava/lang/String;)V")
    loadIcon = JavaMethod("(Landroid/content/pm/PackageManager;)Landroid/graphics/drawable/Drawable;")
    loadLabel = JavaMethod("(Landroid/content/pm/PackageManager;)Ljava/lang/CharSequence;")
    getServiceInfo = JavaMethod("()Landroid/content/pm/ServiceInfo;")
    getComponent = JavaMethod("()Landroid/content/ComponentName;")
    getServiceName = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getSettingsActivity = JavaMethod("()Ljava/lang/String;")