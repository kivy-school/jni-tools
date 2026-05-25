from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SearchResult"]

class SearchResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/SearchResult"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getGenericDocument = JavaMethod("()Landroid/app/appsearch/GenericDocument;")
    getMatchInfos = JavaMethod("()Ljava/util/List;")
    getPackageName = JavaMethod("()Ljava/lang/String;")
    getDatabaseName = JavaMethod("()Ljava/lang/String;")
    getRankingSignal = JavaMethod("()D")
    getJoinedResults = JavaMethod("()Ljava/util/List;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/SearchResult/Builder"
        __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;)V", False)]
        setGenericDocument = JavaMethod("(Landroid/app/appsearch/GenericDocument;)Landroid/app/appsearch/SearchResult$Builder;")
        addMatchInfo = JavaMethod("(Landroid/app/appsearch/SearchResult$MatchInfo;)Landroid/app/appsearch/SearchResult$Builder;")
        setRankingSignal = JavaMethod("(D)Landroid/app/appsearch/SearchResult$Builder;")
        addJoinedResult = JavaMethod("(Landroid/app/appsearch/SearchResult;)Landroid/app/appsearch/SearchResult$Builder;")
        build = JavaMethod("()Landroid/app/appsearch/SearchResult;")

    class MatchInfo(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/SearchResult/MatchInfo"
        CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
        getPropertyPath = JavaMethod("()Ljava/lang/String;")
        getPropertyPathObject = JavaMethod("()Landroid/app/appsearch/PropertyPath;")
        getFullText = JavaMethod("()Ljava/lang/String;")
        getExactMatchRange = JavaMethod("()Landroid/app/appsearch/SearchResult$MatchRange;")
        getExactMatch = JavaMethod("()Ljava/lang/CharSequence;")
        getSubmatchRange = JavaMethod("()Landroid/app/appsearch/SearchResult$MatchRange;")
        getSubmatch = JavaMethod("()Ljava/lang/CharSequence;")
        getSnippetRange = JavaMethod("()Landroid/app/appsearch/SearchResult$MatchRange;")
        getSnippet = JavaMethod("()Ljava/lang/CharSequence;")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
        describeContents = JavaMethod("()I")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/app/appsearch/SearchResult/MatchInfo/Builder"
            __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
            setExactMatchRange = JavaMethod("(Landroid/app/appsearch/SearchResult$MatchRange;)Landroid/app/appsearch/SearchResult$MatchInfo$Builder;")
            setSubmatchRange = JavaMethod("(Landroid/app/appsearch/SearchResult$MatchRange;)Landroid/app/appsearch/SearchResult$MatchInfo$Builder;")
            setSnippetRange = JavaMethod("(Landroid/app/appsearch/SearchResult$MatchRange;)Landroid/app/appsearch/SearchResult$MatchInfo$Builder;")
            build = JavaMethod("()Landroid/app/appsearch/SearchResult$MatchInfo;")

    class MatchRange(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/SearchResult/MatchRange"
        __javaconstructor__ = [("(II)V", False)]
        getStart = JavaMethod("()I")
        getEnd = JavaMethod("()I")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        toString = JavaMethod("()Ljava/lang/String;")
        hashCode = JavaMethod("()I")