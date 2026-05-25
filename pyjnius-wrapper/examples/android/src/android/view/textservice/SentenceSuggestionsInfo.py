from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SentenceSuggestionsInfo"]

class SentenceSuggestionsInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/textservice/SentenceSuggestionsInfo"
    __javaconstructor__ = [("([Landroid/view/textservice/SuggestionsInfo;[I[I)V", False), ("(Landroid/os/Parcel;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getSuggestionsCount = JavaMethod("()I")
    getSuggestionsInfoAt = JavaMethod("(I)Landroid/view/textservice/SuggestionsInfo;")
    getOffsetAt = JavaMethod("(I)I")
    getLengthAt = JavaMethod("(I)I")