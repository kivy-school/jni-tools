from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SearchRecentSuggestions"]

class SearchRecentSuggestions(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/provider/SearchRecentSuggestions"
    __javaconstructor__ = [("(Landroid/content/Context;Ljava/lang/String;I)V", False)]
    QUERIES_PROJECTION_1LINE = JavaStaticField("[Ljava/lang/String;")
    QUERIES_PROJECTION_2LINE = JavaStaticField("[Ljava/lang/String;")
    QUERIES_PROJECTION_DATE_INDEX = JavaStaticField("I")
    QUERIES_PROJECTION_DISPLAY1_INDEX = JavaStaticField("I")
    QUERIES_PROJECTION_DISPLAY2_INDEX = JavaStaticField("I")
    QUERIES_PROJECTION_QUERY_INDEX = JavaStaticField("I")
    saveRecentQuery = JavaMethod("(Ljava/lang/String;Ljava/lang/String;)V")
    clearHistory = JavaMethod("()V")