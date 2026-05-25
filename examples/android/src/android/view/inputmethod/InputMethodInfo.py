from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InputMethodInfo"]

class InputMethodInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inputmethod/InputMethodInfo"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/content/pm/ResolveInfo;)V", False), ("(Ljava/lang/String;Ljava/lang/String;Ljava/lang/CharSequence;Ljava/lang/String;)V", False)]
    ACTION_STYLUS_HANDWRITING_SETTINGS = JavaStaticField("Ljava/lang/String;")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getId = JavaMethod("()Ljava/lang/String;")
    getPackageName = JavaMethod("()Ljava/lang/String;")
    getServiceName = JavaMethod("()Ljava/lang/String;")
    getServiceInfo = JavaMethod("()Landroid/content/pm/ServiceInfo;")
    getComponent = JavaMethod("()Landroid/content/ComponentName;")
    loadLabel = JavaMethod("(Landroid/content/pm/PackageManager;)Ljava/lang/CharSequence;")
    loadIcon = JavaMethod("(Landroid/content/pm/PackageManager;)Landroid/graphics/drawable/Drawable;")
    getSettingsActivity = JavaMethod("()Ljava/lang/String;")
    getSubtypeCount = JavaMethod("()I")
    getSubtypeAt = JavaMethod("(I)Landroid/view/inputmethod/InputMethodSubtype;")
    getIsDefaultResourceId = JavaMethod("()I")
    getConfigChanges = JavaMethod("()I")
    supportsStylusHandwriting = JavaMethod("()Z")
    supportsConnectionlessStylusHandwriting = JavaMethod("()Z")
    createStylusHandwritingSettingsActivityIntent = JavaMethod("()Landroid/content/Intent;")
    dump = JavaMethod("(Landroid/util/Printer;Ljava/lang/String;)V")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    suppressesSpellChecker = JavaMethod("()Z")
    shouldShowInInputMethodPicker = JavaMethod("()Z")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")