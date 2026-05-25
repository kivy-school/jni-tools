from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["KeyCharacterMap"]

class KeyCharacterMap(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/KeyCharacterMap"
    ALPHA = JavaStaticField("I")
    BUILT_IN_KEYBOARD = JavaStaticField("I")
    COMBINING_ACCENT = JavaStaticField("I")
    COMBINING_ACCENT_MASK = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    FULL = JavaStaticField("I")
    HEX_INPUT = JavaStaticField("C")
    MODIFIER_BEHAVIOR_CHORDED = JavaStaticField("I")
    MODIFIER_BEHAVIOR_CHORDED_OR_TOGGLED = JavaStaticField("I")
    NUMERIC = JavaStaticField("I")
    PICKER_DIALOG_INPUT = JavaStaticField("C")
    PREDICTIVE = JavaStaticField("I")
    SPECIAL_FUNCTION = JavaStaticField("I")
    VIRTUAL_KEYBOARD = JavaStaticField("I")
    finalize = JavaMethod("()V")
    load = JavaStaticMethod("(I)Landroid/view/KeyCharacterMap;")
    get = JavaMethod("(II)I")
    getNumber = JavaMethod("(I)C")
    getMatch = JavaMultipleMethod([("(I[C)C", False, False), ("(I[CI)C", False, False)])
    getDisplayLabel = JavaMethod("(I)C")
    getDeadChar = JavaStaticMethod("(II)I")
    getKeyData = JavaMethod("(ILandroid/view/KeyCharacterMap$KeyData;)Z")
    getEvents = JavaMethod("([C)[Landroid/view/KeyEvent;")
    isPrintingKey = JavaMethod("(I)Z")
    getKeyboardType = JavaMethod("()I")
    getModifierBehavior = JavaMethod("()I")
    deviceHasKey = JavaStaticMethod("(I)Z")
    deviceHasKeys = JavaStaticMethod("([I)[Z")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")

    class KeyData(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/KeyCharacterMap/KeyData"
        __javaconstructor__ = [("()V", False)]
        META_LENGTH = JavaStaticField("I")
        displayLabel = JavaField("C")
        meta = JavaField("[C")
        number = JavaField("C")

    class UnavailableException(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/KeyCharacterMap/UnavailableException"
        __javaconstructor__ = [("(Ljava/lang/String;)V", False)]