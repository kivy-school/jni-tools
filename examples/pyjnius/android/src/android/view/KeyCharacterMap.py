from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getKeyboardType = JavaMethod("()I")
    deviceHasKey = JavaStaticMethod("(I)Z")
    deviceHasKeys = JavaStaticMethod("([I)[Z")
    getModifierBehavior = JavaMethod("()I")
    getEvents = JavaMethod("([C)[Landroid/view/KeyEvent;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    load = JavaStaticMethod("(I)Landroid/view/KeyCharacterMap;")
    get = JavaMethod("(II)I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getDeadChar = JavaStaticMethod("(II)I")
    getDisplayLabel = JavaMethod("(I)C")
    getKeyData = JavaMethod("(ILandroid/view/KeyCharacterMap$KeyData;)Z")
    getMatch = JavaMultipleMethod([("(I[C)C", False, False), ("(I[CI)C", False, False)])
    isPrintingKey = JavaMethod("(I)Z")
    getNumber = JavaMethod("(I)C")

    class UnavailableException(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/KeyCharacterMap$UnavailableException"
        __javaconstructor__ = [("(Ljava/lang/String;)V", False)]

    class KeyData(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/view/KeyCharacterMap$KeyData"
        __javaconstructor__ = [("()V", False)]
        META_LENGTH = JavaStaticField("I")
        displayLabel = JavaField("C")
        meta = JavaField("[C")
        number = JavaField("C")