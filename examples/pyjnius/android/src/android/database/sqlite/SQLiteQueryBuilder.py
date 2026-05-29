from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["SQLiteQueryBuilder"]

class SQLiteQueryBuilder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/database/sqlite/SQLiteQueryBuilder"
    __javaconstructor__ = [("()V", False)]
    setDistinct = JavaMethod("(Z)V")
    isDistinct = JavaMethod("()Z")
    getTables = JavaMethod("()Ljava/lang/String;")
    setTables = JavaMethod("(Ljava/lang/String;)V")
    appendWhere = JavaMethod("(Ljava/lang/CharSequence;)V")
    appendWhereEscapeString = JavaMethod("(Ljava/lang/String;)V")
    appendWhereStandalone = JavaMethod("(Ljava/lang/CharSequence;)V")
    setProjectionMap = JavaMethod("(Ljava/util/Map;)V")
    getProjectionMap = JavaMethod("()Ljava/util/Map;")
    setProjectionGreylist = JavaMethod("(Ljava/util/Collection;)V")
    getProjectionGreylist = JavaMethod("()Ljava/util/Collection;")
    setCursorFactory = JavaMethod("(Landroid/database/sqlite/SQLiteDatabase$CursorFactory;)V")
    getCursorFactory = JavaMethod("()Landroid/database/sqlite/SQLiteDatabase$CursorFactory;")
    setStrict = JavaMethod("(Z)V")
    isStrict = JavaMethod("()Z")
    setStrictColumns = JavaMethod("(Z)V")
    isStrictColumns = JavaMethod("()Z")
    setStrictGrammar = JavaMethod("(Z)V")
    isStrictGrammar = JavaMethod("()Z")
    buildQueryString = JavaStaticMethod("(ZLjava/lang/String;[Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;")
    appendColumns = JavaStaticMethod("(Ljava/lang/StringBuilder;[Ljava/lang/String;)V")
    query = JavaMultipleMethod([("(Landroid/database/sqlite/SQLiteDatabase;[Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Landroid/database/Cursor;", False, False), ("(Landroid/database/sqlite/SQLiteDatabase;[Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Landroid/database/Cursor;", False, False), ("(Landroid/database/sqlite/SQLiteDatabase;[Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Landroid/os/CancellationSignal;)Landroid/database/Cursor;", False, False)])
    insert = JavaMethod("(Landroid/database/sqlite/SQLiteDatabase;Landroid/content/ContentValues;)J")
    update = JavaMethod("(Landroid/database/sqlite/SQLiteDatabase;Landroid/content/ContentValues;Ljava/lang/String;[Ljava/lang/String;)I")
    delete = JavaMethod("(Landroid/database/sqlite/SQLiteDatabase;Ljava/lang/String;[Ljava/lang/String;)I")
    buildQuery = JavaMultipleMethod([("([Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;", False, False), ("([Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;", False, False)])
    buildUnionSubQuery = JavaMultipleMethod([("(Ljava/lang/String;[Ljava/lang/String;Ljava/util/Set;ILjava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;", False, False), ("(Ljava/lang/String;[Ljava/lang/String;Ljava/util/Set;ILjava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;", False, False)])
    buildUnionQuery = JavaMethod("([Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;")