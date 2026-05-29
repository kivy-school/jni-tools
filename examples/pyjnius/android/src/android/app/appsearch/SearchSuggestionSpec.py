from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SearchSuggestionSpec"]

class SearchSuggestionSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/SearchSuggestionSpec"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    SUGGESTION_RANKING_STRATEGY_DOCUMENT_COUNT = JavaStaticField("I")
    SUGGESTION_RANKING_STRATEGY_NONE = JavaStaticField("I")
    SUGGESTION_RANKING_STRATEGY_TERM_FREQUENCY = JavaStaticField("I")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")
    getFilterSchemas = JavaMethod("()Ljava/util/List;")
    getFilterDocumentIds = JavaMethod("()Ljava/util/Map;")
    getFilterNamespaces = JavaMethod("()Ljava/util/List;")
    getFilterProperties = JavaMethod("()Ljava/util/Map;")
    getMaximumResultCount = JavaMethod("()I")
    getRankingStrategy = JavaMethod("()I")
    getSearchStringParameters = JavaMethod("()Ljava/util/List;")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/SearchSuggestionSpec$Builder"
        __javaconstructor__ = [("(I)V", False)]
        addFilterDocumentIds = JavaMultipleMethod([("(Ljava/lang/String;Ljava/util/Collection;)Landroid/app/appsearch/SearchSuggestionSpec$Builder;", False, False), ("(Ljava/lang/String;[Ljava/lang/String;)Landroid/app/appsearch/SearchSuggestionSpec$Builder;", False, True)])
        addFilterNamespaces = JavaMultipleMethod([("(Ljava/util/Collection;)Landroid/app/appsearch/SearchSuggestionSpec$Builder;", False, False), ("([Ljava/lang/String;)Landroid/app/appsearch/SearchSuggestionSpec$Builder;", False, True)])
        addFilterProperties = JavaMethod("(Ljava/lang/String;Ljava/util/Collection;)Landroid/app/appsearch/SearchSuggestionSpec$Builder;")
        addFilterPropertyPaths = JavaMethod("(Ljava/lang/String;Ljava/util/Collection;)Landroid/app/appsearch/SearchSuggestionSpec$Builder;")
        addFilterSchemas = JavaMultipleMethod([("(Ljava/util/Collection;)Landroid/app/appsearch/SearchSuggestionSpec$Builder;", False, False), ("([Ljava/lang/String;)Landroid/app/appsearch/SearchSuggestionSpec$Builder;", False, True)])
        addSearchStringParameters = JavaMultipleMethod([("([Ljava/lang/String;)Landroid/app/appsearch/SearchSuggestionSpec$Builder;", False, True), ("(Ljava/util/List;)Landroid/app/appsearch/SearchSuggestionSpec$Builder;", False, False)])
        setRankingStrategy = JavaMethod("(I)Landroid/app/appsearch/SearchSuggestionSpec$Builder;")
        build = JavaMethod("()Landroid/app/appsearch/SearchSuggestionSpec;")