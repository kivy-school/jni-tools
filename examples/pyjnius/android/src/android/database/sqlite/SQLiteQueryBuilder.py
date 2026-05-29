from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SQLiteQueryBuilder"]

class SQLiteQueryBuilder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/sqlite/SQLiteQueryBuilder"
    __javaconstructor__ = [("()V", False)]
    buildUnionQuery = JavaMethod("([Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;")
    appendWhere = JavaMethod("(Ljava/lang/CharSequence;)V")
    buildQueryString = JavaStaticMethod("(ZLjava/lang/String;[Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;")
    buildQuery = JavaMultipleMethod([("([Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;", False, False), ("([Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;", False, False)])
    appendWhereEscapeString = JavaMethod("(Ljava/lang/String;)V")
    appendColumns = JavaStaticMethod("(Ljava/lang/StringBuilder;[Ljava/lang/String;)V")
    buildUnionSubQuery = JavaMultipleMethod([("(Ljava/lang/String;[Ljava/lang/String;Ljava/util/Set;ILjava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;", False, False), ("(Ljava/lang/String;[Ljava/lang/String;Ljava/util/Set;ILjava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;", False, False)])
    appendWhereStandalone = JavaMethod("(Ljava/lang/CharSequence;)V")
    getCursorFactory = JavaMethod("()Landroid/database/sqlite/SQLiteDatabase$CursorFactory;")
    getProjectionGreylist = JavaMethod("()Ljava/util/Collection;")
    getProjectionMap = JavaMethod("()Ljava/util/Map;")
    getTables = JavaMethod("()Ljava/lang/String;")
    isDistinct = JavaMethod("()Z")
    isStrictColumns = JavaMethod("()Z")
    isStrictGrammar = JavaMethod("()Z")
    setCursorFactory = JavaMethod("(Landroid/database/sqlite/SQLiteDatabase$CursorFactory;)V")
    setDistinct = JavaMethod("(Z)V")
    setProjectionGreylist = JavaMethod("(Ljava/util/Collection;)V")
    setProjectionMap = JavaMethod("(Ljava/util/Map;)V")
    setStrict = JavaMethod("(Z)V")
    setStrictColumns = JavaMethod("(Z)V")
    setStrictGrammar = JavaMethod("(Z)V")
    setTables = JavaMethod("(Ljava/lang/String;)V")
    update = JavaMethod("(Landroid/database/sqlite/SQLiteDatabase;Landroid/content/ContentValues;Ljava/lang/String;[Ljava/lang/String;)I")
    insert = JavaMethod("(Landroid/database/sqlite/SQLiteDatabase;Landroid/content/ContentValues;)J")
    delete = JavaMethod("(Landroid/database/sqlite/SQLiteDatabase;Ljava/lang/String;[Ljava/lang/String;)I")
    query = JavaMultipleMethod([("(Landroid/database/sqlite/SQLiteDatabase;[Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Landroid/os/CancellationSignal;)Landroid/database/Cursor;", False, False), ("(Landroid/database/sqlite/SQLiteDatabase;[Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Landroid/database/Cursor;", False, False), ("(Landroid/database/sqlite/SQLiteDatabase;[Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Landroid/database/Cursor;", False, False)])
    isStrict = JavaMethod("()Z")