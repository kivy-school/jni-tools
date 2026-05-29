from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InlineSuggestionInfo"]

class InlineSuggestionInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inputmethod/InlineSuggestionInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    SOURCE_AUTOFILL = JavaStaticField("Ljava/lang/String;")
    SOURCE_PLATFORM = JavaStaticField("Ljava/lang/String;")
    TYPE_ACTION = JavaStaticField("Ljava/lang/String;")
    TYPE_SUGGESTION = JavaStaticField("Ljava/lang/String;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getInlinePresentationSpec = JavaMethod("()Landroid/widget/inline/InlinePresentationSpec;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    toString = JavaMethod("()Ljava/lang/String;")
    hashCode = JavaMethod("()I")
    getType = JavaMethod("()Ljava/lang/String;")
    isPinned = JavaMethod("()Z")
    getAutofillHints = JavaMethod("()[Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getSource = JavaMethod("()Ljava/lang/String;")