from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SuggestionsInfo"]

class SuggestionsInfo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/textservice/SuggestionsInfo"
    __javaconstructor__ = [("(I[Ljava/lang/String;)V", False), ("(I[Ljava/lang/String;II)V", False), ("(Landroid/os/Parcel;)V", False)]
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    RESULT_ATTR_DONT_SHOW_UI_FOR_SUGGESTIONS = JavaStaticField("I")
    RESULT_ATTR_HAS_RECOMMENDED_SUGGESTIONS = JavaStaticField("I")
    RESULT_ATTR_IN_THE_DICTIONARY = JavaStaticField("I")
    RESULT_ATTR_LOOKS_LIKE_GRAMMAR_ERROR = JavaStaticField("I")
    RESULT_ATTR_LOOKS_LIKE_TYPO = JavaStaticField("I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    setCookieAndSequence = JavaMethod("(II)V")
    getCookie = JavaMethod("()I")
    getSequence = JavaMethod("()I")
    getSuggestionsAttributes = JavaMethod("()I")
    getSuggestionsCount = JavaMethod("()I")
    getSuggestionAt = JavaMethod("(I)Ljava/lang/String;")
    describeContents = JavaMethod("()I")