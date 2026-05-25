from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SearchRecentSuggestionsProvider"]

class SearchRecentSuggestionsProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/SearchRecentSuggestionsProvider"
    __javaconstructor__ = [("()V", False)]
    DATABASE_MODE_2LINES = JavaStaticField("I")
    DATABASE_MODE_QUERIES = JavaStaticField("I")
    setupSuggestions = JavaMethod("(Ljava/lang/String;I)V")
    delete = JavaMethod("(Landroid/net/Uri;Ljava/lang/String;[Ljava/lang/String;)I")
    getType = JavaMethod("(Landroid/net/Uri;)Ljava/lang/String;")
    insert = JavaMethod("(Landroid/net/Uri;Landroid/content/ContentValues;)Landroid/net/Uri;")
    onCreate = JavaMethod("()Z")
    query = JavaMethod("(Landroid/net/Uri;[Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;)Landroid/database/Cursor;")
    update = JavaMethod("(Landroid/net/Uri;Landroid/content/ContentValues;Ljava/lang/String;[Ljava/lang/String;)I")