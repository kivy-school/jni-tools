from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ContentProviderOperation"]

class ContentProviderOperation(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/content/ContentProviderOperation"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    CONTENTS_FILE_DESCRIPTOR = JavaStaticField("I")
    PARCELABLE_WRITE_RETURN_VALUE = JavaStaticField("I")
    toString = JavaMethod("()Ljava/lang/String;")
    apply = JavaMethod("(Landroid/content/ContentProvider;[Landroid/content/ContentProviderResult;I)Landroid/content/ContentProviderResult;")
    getUri = JavaMethod("()Landroid/net/Uri;")
    newUpdate = JavaStaticMethod("(Landroid/net/Uri;)Landroid/content/ContentProviderOperation$Builder;")
    isCall = JavaMethod("()Z")
    isYieldAllowed = JavaMethod("()Z")
    isReadOperation = JavaMethod("()Z")
    isDelete = JavaMethod("()Z")
    isInsert = JavaMethod("()Z")
    isExceptionAllowed = JavaMethod("()Z")
    newInsert = JavaStaticMethod("(Landroid/net/Uri;)Landroid/content/ContentProviderOperation$Builder;")
    isUpdate = JavaMethod("()Z")
    newAssertQuery = JavaStaticMethod("(Landroid/net/Uri;)Landroid/content/ContentProviderOperation$Builder;")
    newDelete = JavaStaticMethod("(Landroid/net/Uri;)Landroid/content/ContentProviderOperation$Builder;")
    newCall = JavaStaticMethod("(Landroid/net/Uri;Ljava/lang/String;Ljava/lang/String;)Landroid/content/ContentProviderOperation$Builder;")
    isAssertQuery = JavaMethod("()Z")
    resolveExtrasBackReferences = JavaMethod("([Landroid/content/ContentProviderResult;I)Landroid/os/Bundle;")
    isWriteOperation = JavaMethod("()Z")
    resolveSelectionArgsBackReferences = JavaMethod("([Landroid/content/ContentProviderResult;I)[Ljava/lang/String;")
    resolveValueBackReferences = JavaMethod("([Landroid/content/ContentProviderResult;I)Landroid/content/ContentValues;")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/content/ContentProviderOperation$Builder"
        withExpectedCount = JavaMethod("(I)Landroid/content/ContentProviderOperation$Builder;")
        withExtra = JavaMethod("(Ljava/lang/String;Ljava/lang/Object;)Landroid/content/ContentProviderOperation$Builder;")
        withExceptionAllowed = JavaMethod("(Z)Landroid/content/ContentProviderOperation$Builder;")
        withExtraBackReference = JavaMultipleMethod([("(Ljava/lang/String;ILjava/lang/String;)Landroid/content/ContentProviderOperation$Builder;", False, False), ("(Ljava/lang/String;I)Landroid/content/ContentProviderOperation$Builder;", False, False)])
        withExtras = JavaMethod("(Landroid/os/Bundle;)Landroid/content/ContentProviderOperation$Builder;")
        withSelection = JavaMethod("(Ljava/lang/String;[Ljava/lang/String;)Landroid/content/ContentProviderOperation$Builder;")
        withSelectionBackReference = JavaMultipleMethod([("(IILjava/lang/String;)Landroid/content/ContentProviderOperation$Builder;", False, False), ("(II)Landroid/content/ContentProviderOperation$Builder;", False, False)])
        withValue = JavaMethod("(Ljava/lang/String;Ljava/lang/Object;)Landroid/content/ContentProviderOperation$Builder;")
        withValueBackReference = JavaMultipleMethod([("(Ljava/lang/String;ILjava/lang/String;)Landroid/content/ContentProviderOperation$Builder;", False, False), ("(Ljava/lang/String;I)Landroid/content/ContentProviderOperation$Builder;", False, False)])
        withValueBackReferences = JavaMethod("(Landroid/content/ContentValues;)Landroid/content/ContentProviderOperation$Builder;")
        withValues = JavaMethod("(Landroid/content/ContentValues;)Landroid/content/ContentProviderOperation$Builder;")
        withYieldAllowed = JavaMethod("(Z)Landroid/content/ContentProviderOperation$Builder;")
        build = JavaMethod("()Landroid/content/ContentProviderOperation;")