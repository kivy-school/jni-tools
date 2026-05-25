from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SearchSuggestionResult"]

class SearchSuggestionResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/SearchSuggestionResult"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getSuggestedResult = JavaMethod("()Ljava/lang/String;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/SearchSuggestionResult/Builder"
        __javaconstructor__ = [("()V", False)]
        setSuggestedResult = JavaMethod("(Ljava/lang/String;)Landroid/app/appsearch/SearchSuggestionResult$Builder;")
        build = JavaMethod("()Landroid/app/appsearch/SearchSuggestionResult;")