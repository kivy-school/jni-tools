from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SentenceSuggestionsInfo"]

class SentenceSuggestionsInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/textservice/SentenceSuggestionsInfo"
    __javaconstructor__ = [("(Landroid/os/Parcel;)V", False), ("([Landroid/view/textservice/SuggestionsInfo;[I[I)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getLengthAt = JavaMethod("(I)I")
    getOffsetAt = JavaMethod("(I)I")
    getSuggestionsCount = JavaMethod("()I")
    getSuggestionsInfoAt = JavaMethod("(I)Landroid/view/textservice/SuggestionsInfo;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")