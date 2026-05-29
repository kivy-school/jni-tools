from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SearchSuggestionResult"]

class SearchSuggestionResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/SearchSuggestionResult"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    getSuggestedResult = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/SearchSuggestionResult$Builder"
        __javaconstructor__ = [("()V", False)]
        setSuggestedResult = JavaMethod("(Ljava/lang/String;)Landroid/app/appsearch/SearchSuggestionResult$Builder;")
        build = JavaMethod("()Landroid/app/appsearch/SearchSuggestionResult;")