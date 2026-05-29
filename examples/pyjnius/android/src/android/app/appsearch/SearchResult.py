from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SearchResult"]

class SearchResult(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/SearchResult"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    getDatabaseName = JavaMethod("()Ljava/lang/String;")
    getParentTypeMap = JavaMethod("()Ljava/util/Map;")
    getMatchInfos = JavaMethod("()Ljava/util/List;")
    getJoinedResults = JavaMethod("()Ljava/util/List;")
    getGenericDocument = JavaMethod("()Landroid/app/appsearch/GenericDocument;")
    getInformationalRankingSignals = JavaMethod("()Ljava/util/List;")
    getRankingSignal = JavaMethod("()D")
    getPackageName = JavaMethod("()Ljava/lang/String;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class MatchRange(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/SearchResult$MatchRange"
        __javaconstructor__ = [("(II)V", False)]
        getEnd = JavaMethod("()I")
        getStart = JavaMethod("()I")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        toString = JavaMethod("()Ljava/lang/String;")
        hashCode = JavaMethod("()I")

    class MatchInfo(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/SearchResult$MatchInfo"
        CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
        CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
        PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
        getExactMatchRange = JavaMethod("()Landroid/app/appsearch/SearchResult$MatchRange;")
        getFullText = JavaMethod("()Ljava/lang/String;")
        getExactMatch = JavaMethod("()Ljava/lang/CharSequence;")
        getPropertyPath = JavaMethod("()Ljava/lang/String;")
        getPropertyPathObject = JavaMethod("()Landroid/app/appsearch/PropertyPath;")
        getSnippet = JavaMethod("()Ljava/lang/CharSequence;")
        getSnippetRange = JavaMethod("()Landroid/app/appsearch/SearchResult$MatchRange;")
        getSubmatch = JavaMethod("()Ljava/lang/CharSequence;")
        getSubmatchRange = JavaMethod("()Landroid/app/appsearch/SearchResult$MatchRange;")
        writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
        describeContents = JavaMethod("()I")

        class Builder(JavaClass, metaclass=MetaJavaClass):
            __javaclass__ = "android/app/appsearch/SearchResult$MatchInfo$Builder"
            __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
            setExactMatchRange = JavaMethod("(Landroid/app/appsearch/SearchResult$MatchRange;)Landroid/app/appsearch/SearchResult$MatchInfo$Builder;")
            setSubmatchRange = JavaMethod("(Landroid/app/appsearch/SearchResult$MatchRange;)Landroid/app/appsearch/SearchResult$MatchInfo$Builder;")
            setSnippetRange = JavaMethod("(Landroid/app/appsearch/SearchResult$MatchRange;)Landroid/app/appsearch/SearchResult$MatchInfo$Builder;")
            build = JavaMethod("()Landroid/app/appsearch/SearchResult$MatchInfo;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/SearchResult$Builder"
        __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/String;)V", False)]
        addInformationalRankingSignal = JavaMethod("(D)Landroid/app/appsearch/SearchResult$Builder;")
        addJoinedResult = JavaMethod("(Landroid/app/appsearch/SearchResult;)Landroid/app/appsearch/SearchResult$Builder;")
        addMatchInfo = JavaMethod("(Landroid/app/appsearch/SearchResult$MatchInfo;)Landroid/app/appsearch/SearchResult$Builder;")
        setParentTypeMap = JavaMethod("(Ljava/util/Map;)Landroid/app/appsearch/SearchResult$Builder;")
        setGenericDocument = JavaMethod("(Landroid/app/appsearch/GenericDocument;)Landroid/app/appsearch/SearchResult$Builder;")
        setRankingSignal = JavaMethod("(D)Landroid/app/appsearch/SearchResult$Builder;")
        build = JavaMethod("()Landroid/app/appsearch/SearchResult;")