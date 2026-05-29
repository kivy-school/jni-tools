from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["FillRequest"]

class FillRequest(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/service/autofill/FillRequest"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    FLAG_COMPATIBILITY_MODE_REQUEST = JavaStaticField("I")
    FLAG_MANUAL_REQUEST = JavaStaticField("I")
    FLAG_SUPPORTS_FILL_DIALOG = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getHints = JavaMethod("()Ljava/util/List;")
    getClientState = JavaMethod("()Landroid/os/Bundle;")
    getFillContexts = JavaMethod("()Ljava/util/List;")
    getDelayedFillIntentSender = JavaMethod("()Landroid/content/IntentSender;")
    getInlineSuggestionsRequest = JavaMethod("()Landroid/view/inputmethod/InlineSuggestionsRequest;")
    toString = JavaMethod("()Ljava/lang/String;")
    getId = JavaMethod("()I")
    getFlags = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")