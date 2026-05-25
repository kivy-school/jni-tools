from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InlineSuggestionInfo"]

class InlineSuggestionInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inputmethod/InlineSuggestionInfo"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    SOURCE_AUTOFILL = JavaStaticField("Ljava/lang/String;")
    SOURCE_PLATFORM = JavaStaticField("Ljava/lang/String;")
    TYPE_ACTION = JavaStaticField("Ljava/lang/String;")
    TYPE_SUGGESTION = JavaStaticField("Ljava/lang/String;")
    getInlinePresentationSpec = JavaMethod("()Landroid/widget/inline/InlinePresentationSpec;")
    getSource = JavaMethod("()Ljava/lang/String;")
    getAutofillHints = JavaMethod("()[Ljava/lang/String;")
    getType = JavaMethod("()Ljava/lang/String;")
    isPinned = JavaMethod("()Z")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")