from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ContentProviderOperation"]

class ContentProviderOperation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/ContentProviderOperation"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    newInsert = JavaStaticMethod("(Landroid/net/Uri;)Landroid/content/ContentProviderOperation$Builder;")
    newUpdate = JavaStaticMethod("(Landroid/net/Uri;)Landroid/content/ContentProviderOperation$Builder;")
    newDelete = JavaStaticMethod("(Landroid/net/Uri;)Landroid/content/ContentProviderOperation$Builder;")
    newAssertQuery = JavaStaticMethod("(Landroid/net/Uri;)Landroid/content/ContentProviderOperation$Builder;")
    newCall = JavaStaticMethod("(Landroid/net/Uri;Ljava/lang/String;Ljava/lang/String;)Landroid/content/ContentProviderOperation$Builder;")
    getUri = JavaMethod("()Landroid/net/Uri;")
    isYieldAllowed = JavaMethod("()Z")
    isExceptionAllowed = JavaMethod("()Z")
    isInsert = JavaMethod("()Z")
    isDelete = JavaMethod("()Z")
    isUpdate = JavaMethod("()Z")
    isAssertQuery = JavaMethod("()Z")
    isCall = JavaMethod("()Z")
    isWriteOperation = JavaMethod("()Z")
    isReadOperation = JavaMethod("()Z")
    apply = JavaMethod("(Landroid/content/ContentProvider;[Landroid/content/ContentProviderResult;I)Landroid/content/ContentProviderResult;")
    resolveValueBackReferences = JavaMethod("([Landroid/content/ContentProviderResult;I)Landroid/content/ContentValues;")
    resolveExtrasBackReferences = JavaMethod("([Landroid/content/ContentProviderResult;I)Landroid/os/Bundle;")
    resolveSelectionArgsBackReferences = JavaMethod("([Landroid/content/ContentProviderResult;I)[Ljava/lang/String;")
    toString = JavaMethod("()Ljava/lang/String;")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/content/ContentProviderOperation/Builder"
        build = JavaMethod("()Landroid/content/ContentProviderOperation;")
        withValues = JavaMethod("(Landroid/content/ContentValues;)Landroid/content/ContentProviderOperation$Builder;")
        withValue = JavaMethod("(Ljava/lang/String;Ljava/lang/Object;)Landroid/content/ContentProviderOperation$Builder;")
        withValueBackReferences = JavaMethod("(Landroid/content/ContentValues;)Landroid/content/ContentProviderOperation$Builder;")
        withValueBackReference = JavaMultipleMethod([("(Ljava/lang/String;I)Landroid/content/ContentProviderOperation$Builder;", False, False), ("(Ljava/lang/String;ILjava/lang/String;)Landroid/content/ContentProviderOperation$Builder;", False, False)])
        withExtras = JavaMethod("(Landroid/os/Bundle;)Landroid/content/ContentProviderOperation$Builder;")
        withExtra = JavaMethod("(Ljava/lang/String;Ljava/lang/Object;)Landroid/content/ContentProviderOperation$Builder;")
        withExtraBackReference = JavaMultipleMethod([("(Ljava/lang/String;I)Landroid/content/ContentProviderOperation$Builder;", False, False), ("(Ljava/lang/String;ILjava/lang/String;)Landroid/content/ContentProviderOperation$Builder;", False, False)])
        withSelection = JavaMethod("(Ljava/lang/String;[Ljava/lang/String;)Landroid/content/ContentProviderOperation$Builder;")
        withSelectionBackReference = JavaMultipleMethod([("(II)Landroid/content/ContentProviderOperation$Builder;", False, False), ("(IILjava/lang/String;)Landroid/content/ContentProviderOperation$Builder;", False, False)])
        withExpectedCount = JavaMethod("(I)Landroid/content/ContentProviderOperation$Builder;")
        withYieldAllowed = JavaMethod("(Z)Landroid/content/ContentProviderOperation$Builder;")
        withExceptionAllowed = JavaMethod("(Z)Landroid/content/ContentProviderOperation$Builder;")