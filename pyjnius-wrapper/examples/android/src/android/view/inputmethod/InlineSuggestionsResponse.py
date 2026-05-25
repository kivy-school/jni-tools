from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InlineSuggestionsResponse"]

class InlineSuggestionsResponse(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inputmethod/InlineSuggestionsResponse"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getInlineSuggestions = JavaMethod("()Ljava/util/List;")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")