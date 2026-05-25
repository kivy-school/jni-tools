from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SearchSuggestionSpec"]

class SearchSuggestionSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/SearchSuggestionSpec"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    SUGGESTION_RANKING_STRATEGY_DOCUMENT_COUNT = JavaStaticField("I")
    SUGGESTION_RANKING_STRATEGY_NONE = JavaStaticField("I")
    SUGGESTION_RANKING_STRATEGY_TERM_FREQUENCY = JavaStaticField("I")
    getMaximumResultCount = JavaMethod("()I")
    getFilterNamespaces = JavaMethod("()Ljava/util/List;")
    getRankingStrategy = JavaMethod("()I")
    getFilterSchemas = JavaMethod("()Ljava/util/List;")
    getFilterProperties = JavaMethod("()Ljava/util/Map;")
    getFilterDocumentIds = JavaMethod("()Ljava/util/Map;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/SearchSuggestionSpec/Builder"
        __javaconstructor__ = [("(I)V", False)]
        addFilterNamespaces = JavaMultipleMethod([("([Ljava/lang/String;)Landroid/app/appsearch/SearchSuggestionSpec$Builder;", False, True), ("(Ljava/util/Collection;)Landroid/app/appsearch/SearchSuggestionSpec$Builder;", False, False)])
        setRankingStrategy = JavaMethod("(I)Landroid/app/appsearch/SearchSuggestionSpec$Builder;")
        addFilterSchemas = JavaMultipleMethod([("([Ljava/lang/String;)Landroid/app/appsearch/SearchSuggestionSpec$Builder;", False, True), ("(Ljava/util/Collection;)Landroid/app/appsearch/SearchSuggestionSpec$Builder;", False, False)])
        addFilterProperties = JavaMethod("(Ljava/lang/String;Ljava/util/Collection;)Landroid/app/appsearch/SearchSuggestionSpec$Builder;")
        addFilterPropertyPaths = JavaMethod("(Ljava/lang/String;Ljava/util/Collection;)Landroid/app/appsearch/SearchSuggestionSpec$Builder;")
        addFilterDocumentIds = JavaMultipleMethod([("(Ljava/lang/String;[Ljava/lang/String;)Landroid/app/appsearch/SearchSuggestionSpec$Builder;", False, True), ("(Ljava/lang/String;Ljava/util/Collection;)Landroid/app/appsearch/SearchSuggestionSpec$Builder;", False, False)])
        build = JavaMethod("()Landroid/app/appsearch/SearchSuggestionSpec;")