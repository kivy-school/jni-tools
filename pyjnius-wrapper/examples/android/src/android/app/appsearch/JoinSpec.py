from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["JoinSpec"]

class JoinSpec(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/app/appsearch/JoinSpec"
    AGGREGATION_SCORING_AVG_RANKING_SIGNAL = JavaStaticField("I")
    AGGREGATION_SCORING_MAX_RANKING_SIGNAL = JavaStaticField("I")
    AGGREGATION_SCORING_MIN_RANKING_SIGNAL = JavaStaticField("I")
    AGGREGATION_SCORING_OUTER_RESULT_RANKING_SIGNAL = JavaStaticField("I")
    AGGREGATION_SCORING_RESULT_COUNT = JavaStaticField("I")
    AGGREGATION_SCORING_SUM_RANKING_SIGNAL = JavaStaticField("I")
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    getNestedQuery = JavaMethod("()Ljava/lang/String;")
    getChildPropertyExpression = JavaMethod("()Ljava/lang/String;")
    getMaxJoinedResultCount = JavaMethod("()I")
    getNestedSearchSpec = JavaMethod("()Landroid/app/appsearch/SearchSpec;")
    getAggregationScoringStrategy = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/app/appsearch/JoinSpec/Builder"
        __javaconstructor__ = [("(Ljava/lang/String;)V", False)]
        setNestedSearch = JavaMethod("(Ljava/lang/String;Landroid/app/appsearch/SearchSpec;)Landroid/app/appsearch/JoinSpec$Builder;")
        setMaxJoinedResultCount = JavaMethod("(I)Landroid/app/appsearch/JoinSpec$Builder;")
        setAggregationScoringStrategy = JavaMethod("(I)Landroid/app/appsearch/JoinSpec$Builder;")
        build = JavaMethod("()Landroid/app/appsearch/JoinSpec;")