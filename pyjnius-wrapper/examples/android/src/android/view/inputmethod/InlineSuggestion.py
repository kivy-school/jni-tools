from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["InlineSuggestion"]

class InlineSuggestion(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/inputmethod/InlineSuggestion"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    inflate = JavaMethod("(Landroid/content/Context;Landroid/util/Size;Ljava/util/concurrent/Executor;Ljava/util/function/Consumer;)V")
    getInfo = JavaMethod("()Landroid/view/inputmethod/InlineSuggestionInfo;")
    toString = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")